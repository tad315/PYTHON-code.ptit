from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Hàm tiện ích: query DB
def query_db(query, args=(), one=False):
    conn = sqlite3.connect("customers.db")
    cursor = conn.cursor()
    cursor.execute(query, args)
    rows = cursor.fetchall()
    conn.commit()
    conn.close()
    return (rows[0] if rows else None) if one else rows

# POST API: thêm khách hàng
@app.route("/add", methods=["POST"])
def add_customer():
    data = request.get_json()
    name = data.get("name")
    age = data.get("age")
    address = data.get("address")
    phone = data.get("phone")
    email = data.get("email")

    query_db("INSERT INTO customers (name, age, address, phone, email) VALUES (?, ?, ?, ?, ?)",
             (name, age, address, phone, email))
    return jsonify({"message": "Customer added successfully!"})

# GET API: tìm kiếm khách hàng
@app.route("/search", methods=["GET"])
def search_customer():
    name = request.args.get("name", "")
    age = request.args.get("age", "")
    address = request.args.get("address", "")
    phone = request.args.get("phone", "")
    email = request.args.get("email", "")

    query = "SELECT * FROM customers WHERE 1=1"
    params = []

    if name:
        query += " AND name LIKE ?"
        params.append(f"%{name}%")
    if age:
        query += " AND age=?"
        params.append(age)
    if address:
        query += " AND address LIKE ?"
        params.append(f"%{address}%")
    if phone:
        query += " AND phone LIKE ?"
        params.append(f"%{phone}%")
    if email:
        query += " AND email LIKE ?"
        params.append(f"%{email}%")

    results = query_db(query, params)

    customers = [
        {"id": r[0], "name": r[1], "age": r[2], "address": r[3], "phone": r[4], "email": r[5]}
        for r in results
    ]
    return jsonify(customers)

if __name__ == "__main__":
    app.run(debug=True)
