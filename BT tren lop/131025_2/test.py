import re
import math
import asyncio
import aiohttp
import aiosqlite
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
from contextlib import asynccontextmanager

BASE = "https://hoanghamobile.com/"
DB_PATH = "hoangha.sqlite3"

CONN_LIMIT = 32                 # tổng số kết nối HTTP tối đa
DETAIL_CONCURRENCY = 24         # số request trang chi tiết chạy song song
LISTING_CONCURRENCY = 6         # crawl song song các danh mục (vừa phải)
READ_TIMEOUT = aiohttp.ClientTimeout(total=25)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
                  "KHTML, like Gecko) Chrome/124.0 Safari/537.36",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

MAX_CATEGORY_PAGES_PER_CAT = 60
MAX_PRODUCTS = 5000

# --- Regex compile sẵn ---
RE_MONEY = re.compile(r"(\d[\d\.\, ]{4,})\s*(?:đ|₫)", re.I)
RE_DIGITS = re.compile(r"[^\d]")
RE_PCT = re.compile(r"(\d+(?:[\.,]\d+)?)\s*%")
RE_MEMBER = re.compile(r"(giá\s*thành\s*viên|member)", re.I)
RE_OLD_HINT = re.compile(r"(?:giá\s*gốc|giá\s*cũ|niêm yết)[^\d]{0,20}(\d[\d\.\, ]{4,})\s*(?:đ|₫)", re.I)
RE_CAT_HINT = re.compile(r"(dien-thoai|iphone|samsung|may-tinh|laptop|tablet|phu-kien|smartwatch|am-thanh|gia-dung|phu-kien)")

PRICE_SELECTORS = [".price", ".product-price", ".special-price", ".final-price", ".price-new", ".giaban"]
CARD_SELECTORS = [".product-item", ".item", ".product", ".box-item", ".prd-item", ".prd", ".product-card", "li[data-id]", "div[data-sku]", ".hh-product-item"]
OLD_SELECTORS = [".old-price", ".price-old", ".original-price", ".gia-goc", "del", "s.old-price"]
PROMO_BOX_SELECTORS = ["#promotion", ".promotion", ".box-promotion", ".offer", ".uu-dai", ".khuyenmai", "#khuyenmai"]

SEED_CATEGORIES = [
    "https://hoanghamobile.com/dien-thoai-di-dong",
    "https://hoanghamobile.com/laptop",
    "https://hoanghamobile.com/may-tinh-bang",
    "https://hoanghamobile.com/phu-kien",
    "https://hoanghamobile.com/dong-ho-thong-minh",
    "https://hoanghamobile.com/am-thanh",
    "https://hoanghamobile.com/gia-dung",
]

def textnum_to_int(s: str):
    if not s:
        return None
    digits = RE_DIGITS.sub("", s.strip())
    if not digits:
        return None
    try:
        return int(digits)
    except Exception:
        return None

def percent_to_float(s: str):
    if not s:
        return None
    m = RE_PCT.search(s)
    if m:
        return float(m.group(1).replace(",", "."))
    return None

def infer_discount_pct(price, old_price):
    if price and old_price and old_price > 0 and price < old_price:
        return round((old_price - price) * 100.0 / old_price, 2)
    return None

def is_internal(url):
    host = urlparse(url).netloc
    return (not host) or host.endswith("hoanghamobile.com")

def bs(html):
    return BeautifulSoup(html, "lxml")

@asynccontextmanager
async def get_session():
    conn = aiohttp.TCPConnector(limit=CONN_LIMIT, ttl_dns_cache=300)
    async with aiohttp.ClientSession(connector=conn, timeout=READ_TIMEOUT, headers=HEADERS) as sess:
        yield sess

async def fetch_html(session: aiohttp.ClientSession, url: str):
    async with session.get(url) as resp:
        resp.raise_for_status()
        return await resp.text()

async def discover_category_urls(session):
    urls = set(SEED_CATEGORIES)
    try:
        html = await fetch_html(session, BASE)
        soup = bs(html)
        for a in soup.select("a[href]"):
            href = a.get("href")
            if not href:
                continue
            full = urljoin(BASE, href)
            if not is_internal(full):
                continue
            if RE_CAT_HINT.search(full):
                urls.add(full)
    except Exception:
        pass
    return list(urls)

def parse_listing_for_product_cards(soup):
    for sel in CARD_SELECTORS:
        found = soup.select(sel)
        if len(found) >= 6:
            return found
    # fallback nhẹ
    candidates = []
    for d in soup.find_all(["div", "li"], recursive=True):
        a = d.find("a", href=True)
        priceish = d.find(string=RE_MONEY)
        if a and priceish:
            candidates.append(d)
    return candidates

def extract_from_card(card, base_url):
    a = card.select_one("a[title]") or card.find("a", href=True)
    name, link, price, discount_percent = None, None, None, None
    if a:
        name = (a.get("title") or a.get_text(" ", strip=True) or "").strip()
        href = a.get("href")
        if href:
            link = urljoin(base_url, href)
    for sel in PRICE_SELECTORS:
        el = card.select_one(sel)
        if el:
            price = textnum_to_int(el.get_text(" ", strip=True))
            if price:
                break
    if price is None:
        txt = card.get_text(" ", strip=True)
        m = RE_MONEY.search(txt)
        if m:
            price = textnum_to_int(m.group(1))
    # badge %
    for s in card.find_all(string=RE_PCT):
        pct = percent_to_float(str(s))
        if pct:
            discount_percent = pct
            break
    return {"name": name, "price": price, "url": link, "discount_percent": discount_percent}

def find_next_page(soup, current_url):
    # common rel next
    el = soup.select_one('a[rel="next"]') \
         or soup.select_one(".pagination a.next") \
         or soup.select_one(".pager a.next") \
         or soup.select_one("a.page-link[aria-label='Next']")
    if el and el.get("href"):
        return urljoin(current_url, el["href"])
    # heuristic fallback
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if re.search(r"(\?|&)p=\d+", href) or re.search(r"/trang/\d+/?", href):
            return urljoin(current_url, href)
    return None

def parse_detail_sync(html):
    soup = bs(html)
    # Member price/discount
    member_discount = None
    mt = soup.find(string=RE_MEMBER)
    if mt:
        context = getattr(mt, "parent", soup)
        nearby = context.get_text(" ", strip=True)
        m = RE_MONEY.search(nearby)
        if m:
            member_discount = textnum_to_int(m.group(1))
    # Promo count
    cnt = 0
    for sel in PROMO_BOX_SELECTORS:
        for box in soup.select(sel):
            cnt += len(box.find_all("li"))
    promo_count = cnt if cnt > 0 else None
    # Old price
    old_price = None
    for sel in OLD_SELECTORS:
        el = soup.select_one(sel)
        if el:
            old_price = textnum_to_int(el.get_text(" ", strip=True))
            if old_price:
                break
    if old_price is None:
        m = RE_OLD_HINT.search(soup.get_text(" ", strip=True))
        if m:
            old_price = textnum_to_int(m.group(1))
    # extra %
    extra_pct = None
    hit = soup.find(string=RE_PCT)
    if hit:
        extra_pct = percent_to_float(str(hit))
    return {"member_discount": member_discount, "promo_count": promo_count, "old_price": old_price, "extra_pct": extra_pct}

async def parse_product_detail(session, url, sem: asyncio.Semaphore):
    try:
        async with sem:
            html = await fetch_html(session, url)
        return parse_detail_sync(html)
    except Exception:
        return {"member_discount": None, "promo_count": None, "old_price": None, "extra_pct": None}

async def init_db():
    db = await aiosqlite.connect(DB_PATH)
    await db.execute("PRAGMA journal_mode=WAL;")
    await db.execute("PRAGMA synchronous=OFF;")
    await db.execute("PRAGMA temp_store=MEMORY;")
    await db.execute("PRAGMA cache_size=-80000;")  # ~80MB page cache
    await db.execute("""
        CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            price INTEGER,
            discount_percent REAL,
            member_discount INTEGER,
            promo_count INTEGER,
            url TEXT UNIQUE,
            scraped_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    await db.execute("CREATE INDEX IF NOT EXISTS idx_products_price ON products(price)")
    await db.execute("CREATE INDEX IF NOT EXISTS idx_products_discount ON products(discount_percent)")
    await db.commit()
    return db

async def bulk_upsert(db, batch):
    if not batch:
        return
    # UPSERT theo url
    sql = """
    INSERT INTO products(name, price, discount_percent, member_discount, promo_count, url)
    VALUES(?,?,?,?,?,?)
    ON CONFLICT(url) DO UPDATE SET
        name=excluded.name,
        price=excluded.price,
        discount_percent=excluded.discount_percent,
        member_discount=excluded.member_discount,
        promo_count=excluded.promo_count,
        scraped_at=CURRENT_TIMESTAMP
    """
    await db.executemany(sql, [
        (r["name"], r["price"], r["discount_percent"], r["member_discount"], r["promo_count"], r["url"])
        for r in batch
    ])
    await db.commit()

async def crawl_category(session, db, cat_url, product_seen: set, product_counter: list):
    page_url = cat_url
    pages_crawled = 0
    detail_sem = asyncio.Semaphore(DETAIL_CONCURRENCY)

    while page_url and pages_crawled < MAX_CATEGORY_PAGES_PER_CAT and product_counter[0] < MAX_PRODUCTS:
        try:
            html = await fetch_html(session, page_url)
        except Exception:
            break

        soup = bs(html)
        cards = parse_listing_for_product_cards(soup)

        # --- Thu thập core info + chuẩn bị detail tasks ---
        core_items = []
        detail_tasks = []
        for card in cards:
            core = extract_from_card(card, page_url)
            name = (core.get("name") or "").strip()
            link = core.get("url")
            price = core.get("price")
            discount_pct = core.get("discount_percent")

            if not link or not name:
                continue
            if link in product_seen:
                continue
            product_seen.add(link)

            core_items.append((name, price, discount_pct, link))
            detail_tasks.append(asyncio.create_task(parse_product_detail(session, link, detail_sem)))

            if len(product_seen) >= MAX_PRODUCTS:
                break

        # --- Đợi detail xong theo lô ---
        details = await asyncio.gather(*detail_tasks, return_exceptions=False)
        batch = []
        for (name, price, discount_pct, link), detail in zip(core_items, details):
            if not discount_pct:
                discount_pct = detail.get("extra_pct")
            if not discount_pct:
                discount_pct = infer_discount_pct(price, detail.get("old_price"))

            rec = {
                "name": name,
                "price": price,
                "discount_percent": discount_pct,
                "member_discount": detail.get("member_discount"),
                "promo_count": detail.get("promo_count"),
                "url": link
            }
            batch.append(rec)

        await bulk_upsert(db, batch)
        product_counter[0] += len(batch)

        pages_crawled += 1
        if product_counter[0] >= MAX_PRODUCTS:
            break
        page_url = find_next_page(soup, page_url)

async def query_and_print_filtered(db):
    sql = """
        SELECT name, price, discount_percent, member_discount, promo_count, url
        FROM products
        WHERE price IS NOT NULL
          AND discount_percent IS NOT NULL
          AND price < 20000000
          AND discount_percent > 13
        ORDER BY discount_percent DESC, price ASC
        LIMIT 200
    """
    async with db.execute(sql) as cur:
        idx = 1
        async for name, price, pct, mem, promos, url in cur:
            pstr = f"{price:,}".replace(",", ".")
            print(f"{idx:>3}. {name} | {pstr} ₫ | -{pct}% | Member: {mem if mem else 'N/A'} | Ưu đãi: {promos if promos is not None else 'N/A'} | {url}")
            idx += 1

async def main():
    async with get_session() as session:
        db = await init_db()

        cats = await discover_category_urls(session)
        print(f"Tìm thấy {len(cats)} danh mục (bao gồm seed).")

        product_seen = set()
        product_counter = [0]

        # chạy danh mục song song ở mức vừa phải
        sem_cat = asyncio.Semaphore(LISTING_CONCURRENCY)
        async def crawl_one(cat):
            async with sem_cat:
                try:
                    await crawl_category(session, db, cat, product_seen, product_counter)
                except Exception as e:
                    print("  Lỗi danh mục:", cat, e)

        await asyncio.gather(*(crawl_one(c) for c in cats))

        print(f"Đã thu thập ~{product_counter[0]} sản phẩm. DB: {DB_PATH}\n")
        print("Các sản phẩm giá < 20 triệu và khuyến mãi > 13%:")
        await query_and_print_filtered(db)
        await db.close()

if __name__ == "__main__":
    asyncio.run(main())