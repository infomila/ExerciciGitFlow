import argparse

from taskflow.storage import Storage

_storage = Storage()


def build_parser():
    parser = argparse.ArgumentParser(prog="taskflow", description="Manage your TaskFlow tasks")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title of the task")

    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="ID of the task to delete")

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        task = _storage.add(args.title)
        print(f"Added task #{task.id}: {task.title}")
    elif args.command == "delete":
        _storage.remove(args.task_id)
        print(f"Deleted task #{args.task_id}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
