import json
import os
import pytest
from task_tracker import (
    add_task,
    delete_task,
    list_tasks,
    load_tasks,
    mark_task,
    save_tasks,
    update_task,
)

DATABASE_PATH = "test_tasks.json"


@pytest.fixture(scope="session", autouse=True)
def clean_db():
    with open(DATABASE_PATH, "w") as file:
        json.dump([], file, indent=4)

    yield

    if os.path.exists(DATABASE_PATH):
        os.remove(DATABASE_PATH)


def test_load_tasks():
    tasks = load_tasks(DATABASE_PATH)
    assert isinstance(tasks, list)


def test_save_tasks():
    sometasks = [
        {
            "id": 1,
            "task": "Camping",
            "status": "todo",
            "created_at": "2025-04-01 15:00:28.051650",
            "updated_at": "2025-04-01 15:00:28.070330",
        }
    ]
    save_tasks(sometasks, DATABASE_PATH)

    tasks = load_tasks(DATABASE_PATH)

    assert sometasks == tasks
    assert isinstance(tasks, list)


def test_add_tasks():
    add_task("Go to mall", DATABASE_PATH)
    add_task("Jogging", DATABASE_PATH)

    tasks = load_tasks(DATABASE_PATH)

    assert len(tasks) == 3
    assert tasks[1]["task"] == "Go to mall" and tasks[1]["id"] == 2
    assert tasks[2]["task"] == "Jogging" and tasks[2]["id"] == 3


def test_delete_task(capsys):
    delete_task(10, DATABASE_PATH)
    no_task = capsys.readouterr().out.strip()

    delete_task(2, DATABASE_PATH)
    deleted = capsys.readouterr().out.strip()

    tasks = load_tasks(DATABASE_PATH)

    assert no_task == "Task not found"
    assert deleted == "Task with ID 2 successfully deleted"
    assert len(tasks) == 2


def test_update_task(capsys):
    update_task(10, "Swimming", DATABASE_PATH)
    no_task = capsys.readouterr().out.strip()

    update_task(1, "Swimming", DATABASE_PATH)
    updated = capsys.readouterr().out.strip()

    tasks = load_tasks(DATABASE_PATH)

    assert no_task == "Task not found"
    assert updated == "Task with ID 1 successfully updated"
    assert tasks[0]["task"] == "Swimming"


def test_mark_task(capsys):
    mark_task(10, "done", DATABASE_PATH)
    no_task = capsys.readouterr().out.strip()

    mark_task(1, "done", DATABASE_PATH)
    updated = capsys.readouterr().out.strip()

    tasks = load_tasks(DATABASE_PATH)

    assert no_task == "Task not found"
    assert updated == "Task with ID 1 successfully updated"
    assert tasks[0]["status"] == "done"


def test_list_tasks(capsys):
    list_tasks("todo", DATABASE_PATH)
    tasks = capsys.readouterr().out.strip()

    # Check if it prints out something
    assert tasks != None
