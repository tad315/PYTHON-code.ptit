import os
import re
import requests
from bs4 import BeautifulSoup
import pandas as pd

URLS = [
    "https://xoso.com.vn/xsmb-22-09-2025.html",
    "https://xoso.com.vn/xsmb-23-09-2025.html",
    "https://xoso.com.vn/xsmb-24-09-2025.html",
    "https://xoso.com.vn/xsmb-25-09-2025.html",
    "https://xoso.com.vn/xsmb-26-09-2025.html",
    "https://xoso.com.vn/xsmb-27-09-2025.html",
    "https://xoso.com.vn/xsmb-28-09-2025.html",
]

HEADERS = {"User-Agent": "Mozilla/5.0"}

def parse_page(url: str):
    # Lấy ngày từ URL
    m = re.search(r"xsmb-(\d{2})-(\d{2})-(\d{4})", url)
    ngay_str = f"{m.group(1)}-{m.group(2)}-{m.group(3)}" if m else "unknown"

    html = requests.get(url, headers=HEADERS, timeout=20)
    html.encoding = "utf-8"
    soup = BeautifulSoup(html.text, "html.parser")

    # Tìm bảng có chữ "ĐB"
    table = None
    for t in soup.find_all("table"):
        if "ĐB" in t.get_text():
            table = t
            break
    if table is None:
        raise RuntimeError(f"Không tìm thấy bảng trong {url}")

    rows = []
    for tr in table.find_all("tr"):
        tds = tr.find_all("td")
        if not tds:
            continue

        label = tds[0].get_text(strip=True)
        if re.search(r"đb|đặc\s*biệt", label, flags=re.I):
            key = "ĐB"
        elif re.fullmatch(r"[1-7]", label):
            key = label
        else:
            continue  # bỏ header "2NM 3NM..."

        # Với hàng này: gom các số lại (mỗi số riêng một cột)
        nums = []
        for td in tds[1:]:
            txt = td.get_text(" ", strip=True)
            nums.extend(re.findall(r"\d{2,6}", txt))

        rows.append([key] + nums)

    if not rows:
        raise RuntimeError(f"Không lấy được dữ liệu số trong {url}")

    # Cân cột (mỗi hàng số lượng khác nhau)
    max_len = max(len(r) for r in rows)
    for r in rows:
        r += [""] * (max_len - len(r))

    # Giữ đúng thứ tự giải
    order = {"ĐB": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7}
    rows.sort(key=lambda r: order.get(r[0], 99))

    cols = ["Giải"] + [f"Số{i}" for i in range(1, max_len)]
    df = pd.DataFrame(rows, columns=cols)

    # Lưu file
    os.makedirs("ketqua_xsmb", exist_ok=True)
    out_path = os.path.join("ketqua_xsmb", f"{ngay_str}.xlsx")
    df.to_excel(out_path, index=False)
    print(f"✅ Đã lưu: {out_path}")

for u in URLS:
    parse_page(u)
