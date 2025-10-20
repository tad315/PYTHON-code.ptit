import sqlite3

def init_db():
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()

    # Tạo bảng khách hàng
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        address TEXT,
        phone TEXT,
        email TEXT
    )
    """)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
