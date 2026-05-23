import json
import os

TASKS_FILE = "src/tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(title):
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "title": title, "done": False}
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
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked complete!")
            return
    print("Task not found.")

def main():
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Exit")
        choice = input("Choose: ")
        if choice == "1":
            title = input("Task title: ")
            add_task(title)
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            task_id = int(input("Task ID: "))
            complete_task(task_id)
        elif choice == "4":
            break

if __name__ == "__main__":
    main()
