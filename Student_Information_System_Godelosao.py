import csv

students = {}
def add_student(student_id, name, age, *grades):  
    
    student_tuple = (student_id, name)
    
   
    grades_list = list(grades)
    
 # Store in dictionary
    students[student_id] = {"name": name, "age": age, "grades": grades_list}
    print(f"Added student {student_tuple}")


def display_students(from_file=False):
    if from_file:
        load_from_file()
        print("Displaying students loaded from file:")
    else:
        print("Displaying students in memory:")
    
    for sid, info in students.items():
        print(f"ID: {sid}, Name: {info['name']}, Age: {info['age']}")
        print("Grades:", end=" ")
        for g in info["grades"]:  # nested loop for grades
            print(g, end=" ")
        print("\n")


def update_student(student_id, **kwargs):  
    if student_id in students:
        for key, value in kwargs.items():
            if key in students[student_id]:
                students[student_id][key] = value
        print(f"Updated student {student_id}")
    else:
        print("Student not found.")


def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        print(f"Deleted student {student_id}")
    else:
        print("Student not found.")


def save_to_file(filename="students.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        for sid, info in students.items():
            writer.writerow([sid, info["name"], info["age"], *info["grades"]])
    print("Data saved to file.")


def load_from_file(filename="students.csv"):
    global students
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            students = {}
            for row in reader:
                sid, name, age, *grades = row
                students[sid] = {"name": name, "age": int(age), "grades": list(map(int, grades))}
        print("Data loaded from file.")
    except FileNotFoundError:
        print("File not found.")




average = lambda grades: sum(grades)/len(grades) if grades else 0


def modify_list(grades):
    grades.append(100) 
    return grades

# ===== Main Menu =====
def main():
    load_from_file()  
    
    while True:
        print("\n===== Student Information System =====")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sid = input("Enter ID: ")
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grades = input("Enter grades separated by space: ").split()
            grades = [int(g) for g in grades]
            add_student(sid, name, age, *grades)

        elif choice == "2":
            display_students()

        elif choice == "3":
            sid = input("Enter student ID to update: ")
            field = input("Enter field to update (name/age/grades): ")
            if field == "grades":
                new_grades = input("Enter new grades (space-separated): ").split()
                update_student(sid, grades=[int(g) for g in new_grades])
            elif field == "age":
                update_student(sid, age=int(input("Enter new age: ")))
            else:
                update_student(sid, name=input("Enter new name: "))

        elif choice == "4":
            sid = input("Enter student ID to delete: ")
            delete_student(sid)

        elif choice == "5":
            save_to_file()

        elif choice == "6":
            load_from_file()

        elif choice == "7":
            print("Exiting program.")
            break  
        else:
            print("Invalid choice, try again.")
            continue  

if __name__ == "__main__":
    main()
