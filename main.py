# Study Planner App
# Author: Parth Chavan

subjects = {}

def add_subject():
    name = input("Enter subject name: ")
    time = input("Enter study time (hours): ")
    subjects[name] = time
    print("Subject added successfully!")

def view_plan():
    print("\n--- Daily Study Plan ---")
    if not subjects:
        print("No subjects added yet.")
    else:
        for sub, time in subjects.items():
            print(f"{sub} : {time} hours")

while True:
    print("\n1. Add Subject")
    print("2. View Study Plan")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_subject()
    elif choice == "2":
        view_plan()
    elif choice == "3":
        print("Exiting... Study hard 💪")
        break
    else:
        print("Invalid choice. Try again.")
