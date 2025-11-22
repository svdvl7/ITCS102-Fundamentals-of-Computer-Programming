# STUDENT INFORMATION SYSTEM


print("STUDENT INFORMATION SYSTEM")
print("-------------------------------------")

student_records = []  

while True:
    print("\nSELECT FROM THE FOLLOWING OPTIONS")
    print("A - ADD STUDENT RECORD")
    print("B - PRINT ALL STUDENT RECORDS")
    print("C - SEARCH STUDENT RECORD")
    print("D - DELETE STUDENT RECORD")
    print("E - EDIT STUDENT RECORD")
    print("F - EXPORT STUDENT RECORD")
    print("G - EXIT SYSTEM")

    choice = input("\nSELECT FROM THE OPTIONS ABOVE ------> ").upper()


    if choice == "A":
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        gender = input("Enter student gender: ")
        section = input("Enter student section: ")
        
        student = [student_id, name, age, gender, section]
        student_records.append(student)
        print(f"{name} added successfully!")


    elif choice == "B":
        if len(student_records) == 0:
            print("No student records found.")
        else:
            print("\nSTUDENT RECORDS:")
            for i, student in enumerate(student_records, start=1):
                print(f"{i}. ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Gender: {student[3]}, Section: {student[4]}")


    elif choice == "C":
        search_id = input("Enter Student ID to search: ")
        found = False
        for student in student_records:
            if student[0] == search_id:
                print(f"Found: ID: {student[0]},\n Name: {student[1]},\n Age: {student[2]},\n Gender: {student[3]}, \n Section: {student[4]}")
                found = True
        if not found:
            print("Student not found.")


    elif choice == "D":
        delete_id = input("Enter Student ID to delete: ")
        found = False
        for student in student_records:
            if student[0] == delete_id:
                confirm = input(f"Are you sure you want to delete {student[1]}? (Y/N): ").upper()
                if confirm == "Y":
                    student_records.remove(student)
                    print("Student removed successfully!")
                found = True
                break
        if not found:
            print("Student not found.")


    elif choice == "E":
        edit_id = input("Enter Student ID to edit: ")
        found = False
        for student in student_records:
            if student[0] == edit_id:
                print("Enter new details:")
                student[1] = input("New name: ")
                student[2] = input("New age: ")
                student[3] = input("New gender: ")
                student[4] = input("New section: ")
                print("Student record updated successfully!")
                found = True
                break
        if not found:
            print("Student not found.")


    elif choice == "F":
        if len(student_records) == 0:
            print("No records to export.")
        else:
            with open("students.txt", "w") as f:
                for student in student_records:
                    f.write(f"ID: {student[0]}, Name: {student[1]}, Age: {student[2]}, Gender: {student[3]}, Section: {student[4]}\n")
            print("Records exported to students.txt.")


    elif choice == "G":
        print("Exiting system...")
        break

    else:
        print("INVALID INPUT")
