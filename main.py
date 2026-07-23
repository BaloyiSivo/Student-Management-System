# Student Management System

students = []

def add_student():
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")

    student = {
        "Name": name,
        "Age": age,
        "Course": course
    }

    students.append(student)
    print("\nStudent added successfully!\n")


def view_students():
    if len(students) == 0:
        print("\nNo students found.\n")
        return

    print("\n----- Student List -----")
    for i, student in enumerate(students, start=1):
        print(f"\nStudent {i}")
        print(f"Name   : {student['Name']}")
        print(f"Age    : {student['Age']}")
        print(f"Course : {student['Course']}")


def search_student():
    name = input("Enter student name to search: ")

    for student in students:
        if student["Name"].lower() == name.lower():
            print("\nStudent Found!")
            print(student)
            return

    print("Student not found.")


def delete_student():
    name = input("Enter student name to delete: ")

    for student in students:
        if student["Name"].lower() == name.lower():
            students.remove(student)
            print("Student deleted successfully!")
            return

    print("Student not found.")


while True:
    print("\n====== Student Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        print("Thank you for using the Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")