import json
import os

TASKS_FILE = "src/tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                print("Warning: tasks file corrupted. Starting fresh.")
                return []
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(title):
    if not title.strip():
        print("Error: Task title cannot be empty.")
        return
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "title": title.strip(), "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {title}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "✓" if task["done"] else "✗"
        print(f"[{status}] {task['id']}. {task['title']}")

def complete_task(task_id):
    if task_id <= 0:
        print("Error: Invalid task ID.")
        return
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            if task["done"]:
                print("Task already completed.")
                return
            task["done"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked complete!")
            return
    print("Error: Task not found.")

def delete_task(task_id):
    tasks = load_tasks()
    updated = [t for t in tasks if t["id"] != task_id]
    if len(updated) == len(tasks):
        print("Error: Task not found.")
        return
    save_tasks(updated)
    print(f"Task {task_id} deleted.")

def main():
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose: ")
        if choice == "1":
            title = input("Task title: ")
            add_task(title)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Task ID: "))
                complete_task(task_id)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == "4":
            try:
                task_id = int(input("Task ID to delete: "))
                delete_task(task_id)
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == "5":
            break

if __name__ == "__main__":
    main()
