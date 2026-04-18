"""Hello script with a CLI."""

from argparse import ArgumentParser

def print_message(msg: str = "This line will be printed.") -> None:
    print(msg)

def main() -> None:
    p = ArgumentParser(description="Print a message.")
    p.add_argument("-m", "--message", default="This line will be printed.")
    args = p.parse_args()
    print_message(args.message)

if __name__ == "__main__":
    main()