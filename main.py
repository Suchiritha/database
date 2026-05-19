from fastapi import FastAPI
import psycopg2

app = FastAPI()

# =========================
# CONNECT TO POSTGRESQL
# =========================

conn = psycopg2.connect(
    host="localhost",
    database="studentdb",
    user="postgres",
    password="$Cooby04",
    port="5432"
)

cursor = conn.cursor()
print(" Connected to PostgreSQL database")

# =========================
# CREATE TABLE
# =========================

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER
)
""")

conn.commit()
print("Table created successfully")
# =========================
# CREATE OPERATION
# =========================

@app.post("/students")
def create_student(name: str, age: int):

    query = "INSERT INTO students (name, age) VALUES (%s, %s)"

    cursor.execute(query, (name, age))

    conn.commit()

    return {"message": "Student Added"}

# =========================
# READ OPERATION
# =========================

@app.get("/students")
def get_students():

    query = "SELECT * FROM students"

    cursor.execute(query)

    data = cursor.fetchall()

    return {"students": data}

# =========================
# UPDATE OPERATION
# =========================

@app.put("/students/{student_id}")
def update_student(student_id: int, name: str):

    query = "UPDATE students SET name = %s WHERE id = %s"

    cursor.execute(query, (name, student_id))

    conn.commit()

    return {"message": "Student Updated"}

# =========================
# DELETE OPERATION
# =========================

@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    query = "DELETE FROM students WHERE id = %s"

    cursor.execute(query, (student_id,))

    conn.commit()

    return {"message": "Student Deleted"}