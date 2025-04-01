# Task Tracker CLI

Task Tracker is a command-line application for managing tasks.
This is a project for the [task-tracker](https://roadmap.sh/projects/task-tracker) of [roadmap.sh](https://roadmap.sh/).

## Features

- **Add Tasks**: Add a task to your list.
- **Delete Task**: Remove a task from your list.
- **Update Task**: Update the description of the existing task.
- **Mark Task**: Mark task as `done`, `in-progress`, or back to `todo`.
- **List Tasks**: List all the tasks, wether you only want to list `done`, `in-progress`, or `todo` tasks.

## Requirements:

- Python 3.7 or higher
- pytest==8.3.5 only for testing, not required to run the cli

## Installation:

1. Clone the repository:

   ```bash
   git clone https://github.com/ljlsison/task-tracker-cli.git
   ```

2. Navigate to the project directory:

   ```bash
   cd task-tracker-cli
   ```

## Usage:

### Add:

- **add** Adds a new task

  ```bash
  python task_tracker.py add "New task"
  ```

### Delete:

- **add** Deletes a task

  ```bash
  python task_tracker.py delete <task_id>
  ```

### Update:

- **update** Updates the description of an existing task

  ```bash
  python task_tracker.py update <task_id>
  ```

### Mark:

- **mark** Updates the status of a task

  ```bash
  python task_tracker.py mark <task_id> <done|completed|todo>
  ```

### List:
- **list** Lists all the existing tasks, or add the optional arguments to only get the selected status
  
   ```bash
   python task_tracker.py list [done|completed|todo]
   ```
