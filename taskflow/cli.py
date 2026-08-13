import argparse

from taskflow.storage import Storage

_storage = Storage()


def build_parser():
    parser = argparse.ArgumentParser(prog="taskflow", description="List and manage your tasks")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Title of the task")

    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument(
        "--status",
        choices=["all", "done", "pending"],
        default="all",
        help="Filter tasks by status",
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "add":
        task = _storage.add(args.title)
        print(f"Added task #{task.id}: {task.title}")
    elif args.command == "list":
        for task in _storage.all():
            if args.status == "done" and not task.done:
                continue
            if args.status == "pending" and task.done:
                continue
            marker = "x" if task.done else " "
            print(f"[{marker}] #{task.id} {task.title}")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
