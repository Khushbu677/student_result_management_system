from student import Student
from result import Result

student = Student()
result = Result()

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Add Result")
    print("4. View Results")
    print("5. Update Student")
    print("6. Delete Student")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Name: ")
        roll = input("Roll No: ")
        dept = input("Department: ")
        student.add_student(name, roll, dept)

    elif choice == 2:
        student.view_students()

    elif choice == 3:
        sid = int(input("Student ID: "))
        subject = input("Subject: ")
        marks = int(input("Marks: "))
        result.add_result(sid, subject, marks)

    elif choice == 4:
        result.view_results()

    elif choice == 5:
        sid = int(input("Student ID: "))
        name = input("New Name: ")
        roll = input("New Roll No: ")
        dept = input("New Department: ")
        student.update_student(sid, name, roll, dept)

    elif choice == 6:
        sid = int(input("Student ID to delete: "))
        student.delete_student(sid)

    elif choice == 7:
        break