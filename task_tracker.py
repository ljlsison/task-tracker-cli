import sys
import json
from datetime import datetime

ADD = "add"
DELETE = "delete"
LIST = "list"
UPDATE = "update"
MARK = "mark"
COMMANDS = [ADD, DELETE, LIST, UPDATE, MARK]

IN_PROGRESS = "in-progress"
DONE = "done"
TODO = "todo"

TASK_STATUS = [IN_PROGRESS, DONE, TODO]


DATABASE_PATH = "tasks.json"


def load_tasks(database=DATABASE_PATH):
    try:
        with open(database, "r") as file:
            return json.load(file)
    except:
        save_tasks([], database)

    return []


def save_tasks(tasks, database=DATABASE_PATH):
    with open(database, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(task, database=DATABASE_PATH):
    tasks = load_tasks(database)
    task_id = tasks[-1]["id"] + 1 if tasks else 1

    tasks.append(
        {
            "id": task_id,
            "task": task,
            "status": TODO,
            "created_at": str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            "updated_at": None,
        }
    )
    save_tasks(tasks, database)
    print(f'Task "{task}" added successfully (ID: {task_id})')


def delete_task(task_id, database=DATABASE_PATH):
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


def update_task(task_id, new_task, database):
    tasks = load_tasks(database)

    if not tasks:
        print("No tasks to update")
        return

    for task in tasks:
        updated = True
        if task["id"] == task_id:
            task["task"] = new_task
            task["updated_at"] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            break
        else:
            updated = False
    else:
        print("Task not found")

    if updated:
        print(f"Task with ID {task_id} successfully updated")

    save_tasks(tasks, database)


def mark_task(task_id, status, database=DATABASE_PATH):
    tasks = load_tasks(database)

    if not tasks:
        print("No tasks to update")
        return

    for task in tasks:
        updated = True
        if task["id"] == task_id:
            task["status"] = status
            task["updated_at"] = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            break
        else:
            updated = False
    else:
        print("Task not found")

    if updated:
        print(f"Task with ID {task_id} successfully updated")

    save_tasks(tasks, database)


def list_tasks(status, database=DATABASE_PATH):
    tasks = load_tasks(database)

    if not tasks:
        print("No tasks to update")
        return

    print(
        f"{'id':<2}|{'description'.center(20)}|{"status".center(15)}|{"created_at".center(20)}|{"updated_at".center(20)}"
    )
    for task in tasks:
        if status:
            if task["status"] != status:
                continue
        print(
            f"{task["id"]:<2}| {task["task"].ljust(19)}|{task["status"].center(15)}|{task["created_at"].center(20)}|{task["updated_at"]}"
        )


def show_usage():
    commands = {
        ADD: ("<task>", "Add a new task"),
        DELETE: ("<task_id>", "Delete a task by ID"),
        UPDATE: ("<task_id> <new task>", "Update a task by ID"),
        MARK: ("<task_id> <done|completed|todo>", "Mark a task as done or completed"),
        LIST: ("[todo|done|completed]", "List all tasks"),
    }

    print("Usage: task_tracker.py [command] [options]\n")
    print("Commands:")
    for cmd, (args, desc) in commands.items():
        print(f"  {cmd:<10} {args:<30} {desc}")

    print("\nOptions:")
    print("  --help                Show this help message")


def main():
    arg_len = len(sys.argv)

    if arg_len < 2 or sys.argv[1] == "--help":
        show_usage()
        return

    app_name = sys.argv[0]
    command = sys.argv[1]

    if command not in COMMANDS:
        show_usage()
        return

    if command == ADD:
        if arg_len < 3:
            print("Error: Please provide a task.")
            return
        add_task(" ".join(sys.argv[2:]))

    elif command == DELETE:
        if arg_len != 3 or not sys.argv[2].isnumeric():
            print(f"Error Usage: {app_name} {DELETE} <task_id>")
            return
        delete_task(int(sys.argv[2]))

    elif command == UPDATE:
        if arg_len < 4 or not sys.argv[2].isnumeric():
            print(f"Error Usage: {app_name} {UPDATE} <task_id> <new task>")
            return
        update_task(int(sys.argv[2]), " ".join(sys.argv[3:]))

    elif command == MARK:
        if (
            arg_len != 4
            or not sys.argv[2].isnumeric()
            or sys.argv[3] not in TASK_STATUS
        ):
            print(f"Error Usage: {app_name} {UPDATE} <task_id> [done|in-progress]")
            return
        mark_task(int(sys.argv[2]), sys.argv[3])

    elif command == LIST:
        if arg_len not in [2, 3]:
            print(f"Error Usage: {app_name} {LIST} [todo|done|in-progress]")
            return

        status = None
        if arg_len == 3:
            if sys.argv[2] in TASK_STATUS:
                status = sys.argv[2]
            else:
                print(f"Error Usage: {app_name} {LIST} [todo|done|in-progress]")
                return

        list_tasks(status)


if __name__ == "__main__":
    main()
