import json
import os
from datetime import datetime

FILE_NAME = 'tasks.json'

def load_tasks():
    if os.path.exists(FILE_NAME) and os.path.getsize(FILE_NAME) > 0:
        try:
            with open(FILE_NAME, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f, indent=4)

def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def add_task(tasks):
    while True:
        date = input("Enter due date (YYYY-MM-DD): ").strip()
        if is_valid_date(date):
            break
        print("Invalid date format. Please use YYYY-MM-DD.")

    task = input("Enter task description: ").strip()
    if task:
        tasks.append({"date": date, "task": task, "completed": False})
        save_tasks(tasks)
        print("Task added successfully.")
    else:
        print("Task description cannot be empty.")

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!")
        return

    tasks.sort(key=lambda x: datetime.strptime(x["date"], '%Y-%m-%d'))

    print("\n--- TO-DO LIST ---")
    for i, item in enumerate(tasks):
        status = "✓" if item["completed"] else " "
        print(f"[{i+1}] [{status}] Due: {item['date']} | Task: {item['task']}")
    print("------------------")

def mark_task_complete(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    while True:
        try:
            task_index = int(input("Enter the number of the task to mark as complete: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["completed"] = True
                save_tasks(tasks)
                print(f"Task {task_index + 1} marked as complete.")
                break
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return

    while True:
        try:
            task_index = int(input("Enter the number of the task to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                deleted_task = tasks.pop(task_index)
                save_tasks(tasks)
                print(f"Task '{deleted_task['task']}' deleted.")
                break
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def display_menu():
    print("\n--- Console To-Do App ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("-------------------------")

def main():
    tasks = load_tasks()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_task_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting To-Do App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()