import json
import os
from datetime import datetime

FILE_NAME = "tasks.json"


# ---------------------- FILE FUNCTIONS ----------------------

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# ---------------------- DISPLAY ----------------------

def title(text):
    print("\n" + "=" * 50)
    print(text.center(50))
    print("=" * 50)


def menu():
    title("PYTHON TO-DO LIST")

    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Completed")
    print("4. Edit Task")
    print("5. Delete Task")
    print("6. Search Task")
    print("7. Statistics")
    print("8. Exit")


# ---------------------- ADD ----------------------

def add_task(tasks):
    title("ADD TASK")

    name = input("Task Name: ").strip()

    if not name:
        print("Task cannot be empty.")
        return

    print("\nPriority")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    p = input("Choose: ")

    priorities = {
        "1": "High",
        "2": "Medium",
        "3": "Low"
    }

    priority = priorities.get(p, "Medium")

    task = {
        "name": name,
        "priority": priority,
        "completed": False,
        "created": datetime.now().strftime("%d-%m-%Y %H:%M")
    }

    tasks.append(task)

    save_tasks(tasks)

    print("\nTask Added Successfully!")


# ---------------------- VIEW ----------------------

def view_tasks(tasks):
    title("YOUR TASKS")

    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):

        status = "✓" if task["completed"] else " "

        print(
            f"{i}. [{status}] {task['name']}"
        )

        print(f"   Priority : {task['priority']}")
        print(f"   Created  : {task['created']}")
        print()
        # ---------------------- COMPLETE ----------------------

def mark_completed(tasks):
    title("MARK TASK COMPLETED")

    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        choice = int(input("\nEnter task number: ")) - 1

        if 0 <= choice < len(tasks):
            tasks[choice]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed!")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# ---------------------- EDIT ----------------------

def edit_task(tasks):
    title("EDIT TASK")

    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        choice = int(input("\nEnter task number: ")) - 1

        if 0 <= choice < len(tasks):

            new_name = input("New task name: ").strip()

            if new_name:
                tasks[choice]["name"] = new_name

            print("\nPriority")
            print("1. High")
            print("2. Medium")
            print("3. Low")

            p = input("Choose priority (Enter to keep current): ").strip()

            priorities = {
                "1": "High",
                "2": "Medium",
                "3": "Low"
            }

            if p in priorities:
                tasks[choice]["priority"] = priorities[p]

            save_tasks(tasks)

            print("Task updated successfully!")

        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# ---------------------- DELETE ----------------------

def delete_task(tasks):
    title("DELETE TASK")

    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        choice = int(input("\nEnter task number to delete: ")) - 1

        if 0 <= choice < len(tasks):
            deleted = tasks.pop(choice)
            save_tasks(tasks)
            print(f"Deleted: {deleted['name']}")
        else:
            print("Invalid task number.")

    except ValueError:
        print("Please enter a valid number.")


# ---------------------- SEARCH ----------------------

def search_task(tasks):
    title("SEARCH TASK")

    keyword = input("Enter keyword: ").lower().strip()

    found = False

    for i, task in enumerate(tasks, start=1):

        if keyword in task["name"].lower():

            status = "✓" if task["completed"] else " "

            print(f"\n{i}. [{status}] {task['name']}")
            print(f"Priority : {task['priority']}")
            print(f"Created  : {task['created']}")

            found = True

    if not found:
        print("No matching task found.")


# ---------------------- STATS ----------------------

def statistics(tasks):
    title("STATISTICS")

    total = len(tasks)
    completed = sum(task["completed"] for task in tasks)
    pending = total - completed

    print(f"Total Tasks     : {total}")
    print(f"Completed Tasks : {completed}")
    print(f"Pending Tasks   : {pending}")

    if total:
        percent = completed / total * 100
        print(f"Completion Rate : {percent:.1f}%")
        # ---------------------- MAIN PROGRAM ----------------------

def main():
    tasks = load_tasks()

    while True:
        menu()

        choice = input("\nEnter your choice (1-8): ").strip()

        if choice == "1":
            add_task(tasks)

        elif choice == "2":
            view_tasks(tasks)

        elif choice == "3":
            mark_completed(tasks)

        elif choice == "4":
            edit_task(tasks)

        elif choice == "5":
            delete_task(tasks)

        elif choice == "6":
            search_task(tasks)

        elif choice == "7":
            statistics(tasks)

        elif choice == "8":
            print("\nThank you for using Python To-Do List!")
            break

        else:
            print("\nInvalid choice! Please try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()