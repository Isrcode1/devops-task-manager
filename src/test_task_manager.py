import json
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from task_manager import add_task, list_tasks, complete_task, load_tasks, save_tasks

# Setup: use a test file
import task_manager
task_manager.TASKS_FILE = "src/test_tasks.json"

def test_add_task():
    save_tasks([])
    add_task("Test task 1")
    tasks = load_tasks()
    assert len(tasks) == 1
    assert tasks[0]["title"] == "Test task 1"
    print("PASS: test_add_task")

def test_complete_task():
    save_tasks([])
    add_task("Test task 2")
    complete_task(1)
    tasks = load_tasks()
    assert tasks[0]["done"] == True
    print("PASS: test_complete_task")

def test_empty_task_rejected():
    save_tasks([])
    add_task("")
    tasks = load_tasks()
    assert len(tasks) == 0
    print("PASS: test_empty_task_rejected")

if __name__ == "__main__":
    test_add_task()
    test_complete_task()
    test_empty_task_rejected()
    print("\nAll tests passed!")
    if os.path.exists("src/test_tasks.json"):
        os.remove("src/test_tasks.json")
