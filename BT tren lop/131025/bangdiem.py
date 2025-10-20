import pandas as pd
import sqlite3

bangdiem = pd.read_csv("bangdiem.csv", encoding="latin1")
thangdiem = pd.read_csv("thangdiem.csv", encoding="latin1")

bangdiem.rename(columns={
    "Student code": "MaSV",
    "Name": "HoTen",
    "?i?m thuy?t tr\x8dnh": "DiemThuyetTrinh",
    "B?i t?p l?n": "DiemBaiTapLon"
}, inplace=True)

print(bangdiem.head())

conn = sqlite3.connect("bangdiem_lophoc.db")
bangdiem.to_sql("bangdiem", conn, if_exists="replace", index=False)
thangdiem.to_sql("thangdiem", conn, if_exists="replace", index=False)

bangdiem = bangdiem.merge(thangdiem, left_on="DiemThuyetTrinh", right_on="Alphabet", how="left")
bangdiem.rename(columns={"10 scale": "DiemThuyetTrinh_10"}, inplace=True)
bangdiem.drop(columns=["Alphabet"], inplace=True)

bangdiem = bangdiem.merge(thangdiem, left_on="DiemBaiTapLon", right_on="Alphabet", how="left")
bangdiem.rename(columns={"10 scale": "DiemBaiTapLon_10"}, inplace=True)
bangdiem.drop(columns=["Alphabet"], inplace=True)

bangdiem["DiemTB"] = (0.2 * bangdiem["DiemThuyetTrinh_10"] + 0.8 * bangdiem["DiemBaiTapLon_10"]).round(1)

bang3 = bangdiem[["MaSV", "HoTen", "DiemThuyetTrinh_10", "DiemBaiTapLon_10", "DiemTB"]]
bang3.to_sql("bang3", conn, if_exists="replace", index=False)

query_join = """
SELECT b.MaSV, b.HoTen, b.DiemThuyetTrinh, b.DiemBaiTapLon,
       b3.DiemThuyetTrinh_10, b3.DiemBaiTapLon_10, b3.DiemTB
FROM bangdiem b
JOIN bang3 b3 ON b.MaSV = b3.MaSV
"""
joined = pd.read_sql_query(query_join, conn)

joined_sorted = joined.sort_values(by="DiemTB", ascending=False)

def xep_loai(tb):
    if tb >= 8.0:
        return "Giỏi"
    elif tb >= 6.5:
        return "Khá"
    elif tb >= 5.0:
        return "Trung bình"
    else:
        return "Trượt"

joined_sorted["XepLoai"] = joined_sorted["DiemTB"].apply(xep_loai)

thongke = joined_sorted["XepLoai"].value_counts().reset_index()
thongke.columns = ["XepLoai", "SoLuong"]

joined_sorted.to_csv("danhsach_xephang.csv", index=False, encoding="utf-8-sig")
joined_sorted.to_csv("danhsach_xeploai.csv", index=False, encoding="utf-8-sig")
thongke.to_csv("thongke_hang.csv", index=False, encoding="utf-8-sig")

print("✅ Đã tạo xong CSDL + file CSV kết quả")
print("\nDANH SÁCH XẾP HẠNG:")
print(joined_sorted)
print("\nTHỐNG KÊ:")
print(thongke)

conn.close()