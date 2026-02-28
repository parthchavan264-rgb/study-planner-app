# Study Planner App - Master Version
# Author: Parth Chavan

import json
import os

FILENAME = "study_plan.json"

def load_plan():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return {}

def save_plan(plan):
    with open(FILENAME, "w") as f:
        json.dump(plan, f, indent=2)

def add_subject(plan):
    name = input("Enter subject name: ")
    if name in plan:
        print("Subject already exists!")
        return
    time = input("Enter study time (hours): ")
    plan[name] = time
    save_plan(plan)
    print("Subject added successfully!")

def view_plan(plan):
    print("\n--- Daily Study Plan ---")
    if not plan:
        print("No subjects added yet.")
    else:
        for sub, time in plan.items():
            print(f"{sub} : {time} hours")

def delete_subject(plan):
    name = input("Enter subject name to delete: ")
    if name in plan:
        del plan[name]
        save_plan(plan)
        print("Subject deleted!")
    else:
        print("Subject not found.")

def edit_subject(plan):
    name = input("Enter subject name to edit: ")
    if name in plan:
        time = input("Enter new study time (hours): ")
        plan[name] = time
        save_plan(plan)
        print("Subject updated!")
    else:
        print("Subject not found.")

plan = load_plan()

while True:
    print("\n1. Add Subject")
    print("2. View Study Plan")
    print("3. Edit Subject")
    print("4. Delete Subject")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_subject(plan)
    elif choice == "2":
        view_plan(plan)
    elif choice == "3":
        edit_subject(plan)
    elif choice == "4":
        delete_subject(plan)
    elif choice == "5":
        print("Exiting... Study hard 💪")
        break
    else:
        print("Invalid choice. Try again.")
