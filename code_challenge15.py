# STUDENT INFORMATION SYSTEM
print("STUDENT INFORMATION SYSTEM")
print("-------------------------------------")
student_record = []

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

    if choice == 'A':
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        gender = input("Enter student gender: ")
        section = input("Enter student section: ")
        student_record.append({"name": name, "age": age, "gender": gender, "section": section})
        print(f"{name} added successfully!")

    elif choice == 'B':
        if student_record:
            print("\nSTUDENT RECORDS:")
            num = 1
            for s in student_record:
                print(f"{num}. Name: {s['name']}, Age: {s['age']}, Gender: {s['gender']}, Section: {s['section']}")
                num += 1
        else:
            print("No student records found.")

    elif choice == 'C':
        name = input("Enter name to search: ")
        found = False
        for s in student_record:
            if s['name'].lower() == name.lower():
                print(f"Found: Name: {s['name']}, Age: {s['age']}, Gender: {s['gender']}, Section: {s['section']}")
                found = True
        if not found:
            print("Student not found.")

    elif choice == 'D':
        name = input("Enter name to delete: ")
        found = False
        for s in student_record:
            if s['name'].lower() == name.lower():
                confirm = input(f"Are you sure you want to delete {s['name']}? (Y/N): ").upper()
                if confirm == 'Y':
                    student_record.remove(s)
                    print(f"{name} removed successfully!")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == 'E':
        name = input("Enter name to edit: ")
        found = False
        for s in student_record:
            if s['name'].lower() == name.lower():
                s['name'] = input("Enter new name: ")
                s['age'] = input("Enter new age: ")
                s['gender'] = input("Enter new gender: ")
                s['section'] = input("Enter new section: ")
                print("Student record updated.")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == 'F':
        if student_record:
            with open("students.txt", "w") as f:
                for s in student_record:
                    f.write(f"Name: {s['name']}, Age: {s['age']}, Gender: {s['gender']}, Section: {s['section']}\n")
            print("Records exported to students.txt.")
        else:
            print("No records to export.")

    elif choice == 'G':
        print("Exiting system...")
        break

    else:
        print("INVALID INPUT")
