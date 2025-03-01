FILE_NAME = "student_records.txt"
students = []

while True:
    print("\nMENU:")
    print("1. Open File")
    print("2. Save File")
    print("3. Save As File")
    print("4. Show All Students Record")
    print("5. Show Student Record")
    print("6. Add Record")
    print("7. Edit Record")
    print("8. Delete Record")
    print("9. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        try:
            with open(FILE_NAME, "r") as f:
                students = [eval(line.strip()) for line in f]
            print("Records loaded successfully!")
        except FileNotFoundError:
            print("File not found.")
            
    elif choice == "2":
        with open(FILE_NAME, "w") as f:
            for student in students:
                f.write(str(student) + "\n")
        print("Records saved.")
        
    elif choice == "3":
        FILE_NAME = input("Enter new filename: ")
        with open(FILE_NAME, "w") as f:
            for student in students:
                f.write(str(student) + "\n")
        print("Saved as", FILE_NAME)
        
    elif choice == "4":
        order_choice = input("Order by (1) Last Name or (2) Grade? ")
        if order_choice == "1":
            students.sort(key=lambda x: x[1][1])
        elif order_choice == "2":
            students.sort(key=lambda x: (x[2] * 0.6 + x[3] * 0.4), reverse=True)
        else:
            print("Invalid choice.")
            continue
        
        for student in students:
            print(student)
            
    elif choice == "5":
        student_id = input("Enter Student ID: ")
        for student in students:
            if student[0] == student_id:
                print(student)
                break
        else:
            print("Student not found.")
            
    elif choice == "6":
        student_id = input("Enter Student ID (6 digits): ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        class_standing = float(input("Enter Class Standing Grade: "))
        major_exam = float(input("Enter Major Exam Grade: "))
        students.append((student_id, (first_name, last_name), class_standing, major_exam))
        print("Record added successfully.")
        
    elif choice == "7":
        student_id = input("Enter Student ID: ")
        for i, student in enumerate(students):
            if student[0] == student_id:
                first_name = input("Enter First Name: ")
                last_name = input("Enter Last Name: ")
                class_standing = float(input("Enter Class Standing Grade: "))
                major_exam = float(input("Enter Major Exam Grade: "))
                students[i] = (student_id, (first_name, last_name), class_standing, major_exam)
                print("Record updated successfully.")
                break
        else:
            print("Student not found.")
            
    elif choice == "8":
        student_id = input("Enter Student ID: ")
        students = [student for student in students if student[0] != student_id]
        print("Record deleted successfully.")
        
    elif choice == "9":
        break
    else:
        print("Invalid choice, try again.")
