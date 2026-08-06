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
        employee_id VARCHAR(100) UNIQUE,
        name VARCHAR(100),
        department VARCHAR(100)
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

    cur.execute("""
    SELECT id, employee_id, name, department
    FROM employees
    ORDER BY id
    """)

    employees = cur.fetchall()

    cur.close()
    conn.close()

    return render_template("index.html", employees=employees)

@app.route("/edit/<int:id>")
def edit_employee(id):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, employee_id, name, department
        FROM employees
        WHERE id = %s
        """,
        (id,)
    )

    employee = cur.fetchone()

    cur.close()
    conn.close()

    return render_template(
        "edit.html",
        employee=employee
    )

@app.route("/update/<int:id>", methods=["POST"])
def update_employee(id):

    employee_id = request.form.get("employee_id")
    name = request.form.get("employee_name")
    department = request.form.get("department")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE employees
        SET employee_id = %s,
            name = %s,
            department = %s
        WHERE id = %s
        """,
        (
            employee_id,
            name,
            department,
            id
        )
    )

    conn.commit()

    cur.close()
    conn.close()

    return redirect("/")

@app.route("/add_employee", methods=["POST"])
def add_employee():

    employee_id = request.form.get("employee_id")
    name = request.form.get("employee_name")
    department = request.form.get("department")

    if not employee_id or not name or not department:
        return "All fields are required", 400

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO employees
        (employee_id, name, department)
        VALUES (%s, %s, %s)
        """,
        (employee_id, name, department)
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