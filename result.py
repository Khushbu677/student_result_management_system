from db import connect_db

class Result:

    def add_result(self, student_id, subject, marks):
        conn = connect_db()
        cursor = conn.cursor()
        query = "INSERT INTO results (student_id, subject, marks) VALUES (%s, %s, %s)"
        cursor.execute(query, (student_id, subject, marks))
        conn.commit()
        print("Result added successfully!")
        conn.close()

    def view_results(self):
        conn = connect_db()
        cursor = conn.cursor()
        query = """
        SELECT students.name, students.roll_no, results.subject, results.marks
        FROM students
        JOIN results ON students.student_id = results.student_id
        """
        cursor.execute(query)

        for name, roll, subject, marks in cursor.fetchall():
            if marks >= 90:
                grade = "A"
            elif marks >= 75:
                grade = "B"
            elif marks >= 60:
                grade = "C"
            else:
                grade = "D"

            print(name, roll, subject, marks, "Grade:", grade)

        conn.close()