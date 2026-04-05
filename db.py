import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="khushbu@123.",
        database="student_b1"
    )