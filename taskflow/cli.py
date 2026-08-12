import argparse

from taskflow.storage import Storage

_storage = Storage()


def build_parser():
    parser = argparse.ArgumentParser(prog="taskflow")
    subparsers = parser.add_subparsers(dest="command")
    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    parser.print_help()


if __name__ == "__main__":
    main()
