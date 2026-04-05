from db import connect_db

class Student:

    def add_student(self, name, roll, dept):
        conn = connect_db()
        cursor = conn.cursor()
        query = "INSERT INTO students (name, roll_no, department) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, roll, dept))
        conn.commit()
        print("Student added successfully!")
        conn.close()

    def view_students(self):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students")
        for row in cursor.fetchall():
            print(row)
        conn.close()

    def update_student(self, student_id, name, roll, dept):
        conn = connect_db()
        cursor = conn.cursor()
        query = "UPDATE students SET name=%s, roll_no=%s, department=%s WHERE student_id=%s"
        cursor.execute(query, (name, roll, dept, student_id))
        conn.commit()
        print("Student updated successfully!")
        conn.close()

    def delete_student(self, student_id):
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE student_id=%s", (student_id,))
        conn.commit()
        print("Student deleted successfully!")
        conn.close()