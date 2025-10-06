import requests
import pandas as pd
import xml.etree.ElementTree as ET

url = "https://portal.vietcombank.com.vn/Usercontrols/TVPortal.TyGia/pXML.aspx"

res = requests.get(url)
res.encoding = "utf-8"

root = ET.fromstring(res.text)

data = []
for exrate in root.findall("Exrate"):
    currency_code = exrate.get("CurrencyCode")
    currency_name = exrate.get("CurrencyName")
    buy = exrate.get("Buy")
    transfer = exrate.get("Transfer")
    sell = exrate.get("Sell")
    data.append([currency_code, currency_name, buy, transfer, sell])
    df = pd.DataFrame(data, columns=["Mã ngoại tệ", "Tên ngoại tệ", "Mua tiền mặt", "Mua chuyển khoản", "Bán"])

df.to_excel("ty_gia_vcb.xlsx", index=False)
print("Done")
