import tkinter as tk
from tkinter import messagebox
import requests

API_BASE = "http://127.0.0.1:5000"

def submit():
    data = {
        "name": entry_name.get(),
        "age": entry_age.get(),
        "address": entry_address.get(),
        "phone": entry_phone.get(),
        "email": entry_email.get()
    }
    try:
        response = requests.post(f"{API_BASE}/add", json=data)
        if response.status_code == 200:
            messagebox.showinfo("Success", "Customer added successfully!")
        else:
            messagebox.showerror("Error", "Failed to add customer")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search():
    params = {}
    if entry_name.get(): params["name"] = entry_name.get()
    if entry_age.get(): params["age"] = entry_age.get()
    if entry_address.get(): params["address"] = entry_address.get()
    if entry_phone.get(): params["phone"] = entry_phone.get()
    if entry_email.get(): params["email"] = entry_email.get()

    try:
        response = requests.get(f"{API_BASE}/search", params=params)
        if response.status_code == 200:
            results = response.json()
            if results:
                first = results[0]  # lấy kết quả đầu tiên
                msg = f"ID: {first['id']}\nTên: {first['name']}\nTuổi: {first['age']}\nĐịa chỉ: {first['address']}\nSĐT: {first['phone']}\nEmail: {first['email']}"
                messagebox.showinfo("Search Result", msg)
            else:
                messagebox.showinfo("Search Result", "Không tìm thấy khách hàng")
        else:
            messagebox.showerror("Error", "Search request failed")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI
root = tk.Tk()
root.title("Quản lý khách hàng")

tk.Label(root, text="Tên").grid(row=0, column=0)
tk.Label(root, text="Tuổi").grid(row=1, column=0)
tk.Label(root, text="Địa chỉ").grid(row=2, column=0)
tk.Label(root, text="SĐT").grid(row=3, column=0)
tk.Label(root, text="Email").grid(row=4, column=0)

entry_name = tk.Entry(root); entry_name.grid(row=0, column=1)
entry_age = tk.Entry(root); entry_age.grid(row=1, column=1)
entry_address = tk.Entry(root); entry_address.grid(row=2, column=1)
entry_phone = tk.Entry(root); entry_phone.grid(row=3, column=1)
entry_email = tk.Entry(root); entry_email.grid(row=4, column=1)

btn_submit = tk.Button(root, text="Submit", command=submit)
btn_submit.grid(row=5, column=0, pady=10)

btn_search = tk.Button(root, text="Search", command=search)
btn_search.grid(row=5, column=1, pady=10)

root.mainloop()
