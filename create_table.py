import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="employee",
    user="postgres",
    password="password"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
)
""")

conn.commit()

print("Table created successfully!")

cur.close()
conn.close()