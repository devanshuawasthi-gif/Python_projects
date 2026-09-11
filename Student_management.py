# PYTHON PROGRAM OF STUDENT MANAGEMENT SYSYTEM 
# DATA STORED IN SQL AND  FILE 


import sqlite3
import csv

# Connect to SQLite database
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    roll_no TEXT PRIMARY KEY,
    name TEXT,
    course TEXT,
    branch TEXT,
    semester TEXT,
    marks REAL
)
""")

conn.commit()

# Main student list
students = []


# Add Student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    branch = input("Enter Branch: ")
    semester = input("Enter Semester: ")
    marks = float(input("Enter Marks: "))

    student = [roll, name, course, branch, semester, marks]
    students.append(student)

    # Store in SQL database
    cursor.execute("""
    INSERT INTO students
    VALUES (?, ?, ?, ?, ?, ?)
    """, student)

    conn.commit()

    # Store in CSV file
    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(student)

    print("Student added successfully!")


# Display Students
def display_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    if len(records) == 0:
        print("No student records found.")
    else:
        print("\n===== STUDENT RECORDS =====")

        for student in records:
            print("\nRoll Number:", student[0])
            print("Name:", student[1])
            print("Course:", student[2])
            print("Branch:", student[3])
            print("Semester:", student[4])
            print("Marks:", student[5])


# Search Student
def search_student():
    roll = input("Enter Roll Number: ")

    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll,)
    )

    student = cursor.fetchone()

    if student:
        print("\nStudent Found!")
        print("Roll Number:", student[0])
        print("Name:", student[1])
        print("Course:", student[2])
        print("Branch:", student[3])
        print("Semester:", student[4])
        print("Marks:", student[5])
    else:
        print("Student not found.")


# Update Student
def update_student():
    roll = input("Enter Roll Number to update: ")

    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll,)
    )

    student = cursor.fetchone()

    if student:
        name = input("Enter New Name: ")
        course = input("Enter New Course: ")
        branch = input("Enter New Branch: ")
        semester = input("Enter New Semester: ")
        marks = float(input("Enter New Marks: "))

        cursor.execute("""
        UPDATE students
        SET name = ?, course = ?, branch = ?,
            semester = ?, marks = ?
        WHERE roll_no = ?
        """, (name, course, branch, semester, marks, roll))

        conn.commit()

        print("Student updated successfully!")

    else:
        print("Student not found.")


# Delete Student
def delete_student():
    roll = input("Enter Roll Number to delete: ")

    cursor.execute(
        "SELECT * FROM students WHERE roll_no = ?",
        (roll,)
    )

    student = cursor.fetchone()

    if student:
        cursor.execute(
            "DELETE FROM students WHERE roll_no = ?",
            (roll,)
        )

        conn.commit()

        print("Student deleted successfully!")

    else:
        print("Student not found.")


# Main Menu
while True:

    print("\n===== COLLEGE STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        conn.close()
        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice!")