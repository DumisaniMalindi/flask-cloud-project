from flask import Flask, render_template, request, redirect
import psycopg2
import os

app = Flask(__name__)

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "employee"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "password")
    )

def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100)
    )
    """)

    conn.commit()

    cur.close()
    conn.close()

@app.route("/")
def home():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100)
    )
    """)

    conn.commit()

    cur.execute("SELECT id, name FROM employees ORDER BY id")

    employees = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("index.html", employees=employees)

@app.route("/add_employee", methods=["POST"])
def add_employee():

    name = request.form.get("employee_name")

    if not name:
        return "Name is required", 400

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO employees (name) VALUES (%s)",
        (name,)
    )

    conn.commit()

    cur.close()
    conn.close()

    return redirect("/")

@app.route("/delete/<int:id>")
def delete_employee(id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM employees WHERE id = %s",
        (id,)
    )

    conn.commit()

    cur.close()
    conn.close()

    return redirect("/")

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    create_table()
    app.run(host="0.0.0.0", port=5000, debug=True)