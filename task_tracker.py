import sys
import json
from datetime import datetime

ADD = "add"
DELETE = "delete"
LIST = "list"
UPDATE = "update"
MARK = "mark"

COMMANDS = [ADD, DELETE, LIST, UPDATE]

DATABASE_PATH = "tasks.json"


def load_tasks(database=None):
    if not database:
        database = DATABASE_PATH
    try:
        with open(database, "r") as file:
            return json.load(file)
    except:
        save_tasks([], database)

    return []


def save_tasks(tasks, database=None):
    if not database:
        database = DATABASE_PATH
    with open(database, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(task, database=None):
    if not database:
        database = DATABASE_PATH

    tasks = load_tasks(database)
    task_id = tasks[-1]["id"] + 1 if tasks else 1

    tasks.append(
        {
            "id": task_id,
            "task": task,
            "status": "todo",
            "created_at": str(datetime.now()),
            "updated_at": None,
        }
    )
    save_tasks(tasks, database)
    print(f'Task "{task}" added successfully (ID: {task_id})')


def delete_task(task_id, database=None):
    if not database:
        database = DATABASE_PATH

    tasks = load_tasks(database)

    if not tasks:
        print("No tasks to delete")
        return

    for i, task in enumerate(tasks):
        deleted = True
        if task["id"] == task_id:
            del tasks[i]
            break
        else:
            deleted = False
    else:
        print("Task not found")

    if deleted:
        print(f"Task with ID {task_id} successfully deleted")

    save_tasks(tasks, database)


def update_task(task_id, new_task, database=None):
    if not database:
        database = DATABASE_PATH

    tasks = load_tasks(database)

    if not tasks:
        print("No tasks to update")
        return

    for task in tasks:
        updated = True
        if task["id"] == task_id:
            task["task"] = new_task
            task["updated_at"] = str(datetime.now())
            break
        else:
            updated = False
    else:
        print("Task not found")

    if updated:
        print(f"Task with ID {task_id} successfully updated")

    save_tasks(tasks, database)


def show_usage():
    commands = {
        ADD: ("<task>", "Add a new task"),
        DELETE: ("<task_id>", "Delete a task by ID"),
        UPDATE: ("<task_id> <new task>", "Update a task by ID"),
        MARK: ("<task_id> [done|completed]", "Mark a task as done or completed"),
        LIST: ("[done|completed]", "List all tasks"),
    }

    print("Usage: task-tracker.py [command] [options]\n")
    print("Commands:")
    for cmd, (args, desc) in commands.items():
        print(f"  {cmd:<10} {args:<30} {desc}")

    print("\nOptions:")
    print("  --help                Show this help message")


def main():
    if len(sys.argv) < 2 or sys.argv[1] == "--help":
        show_usage()
        return

    command = sys.argv[1]

    if command not in COMMANDS:
        show_usage()
        return

    if command == ADD:
        if len(sys.argv) < 3:
            print("Error: Please provide a task.")
            return
        add_task(" ".join(sys.argv[2:]))

    elif command == DELETE:
        if len(sys.argv) != 3 or not sys.argv[2].isnumeric():
            print(f"Error Usage: task-tracker.py {DELETE} <task_id>")
        delete_task(int(sys.argv[2]))

    if command == UPDATE:
        if len(sys.argv) < 4 or not sys.argv[2].isnumeric():
            print(f"Error Usage: task-tracker.py {UPDATE} <task_id> <new task>")
            return
        update_task(int(sys.argv[2]), " ".join(sys.argv[3:]))


if __name__ == "__main__":
    main()
