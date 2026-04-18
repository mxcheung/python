"""Hello script with a CLI."""

from argparse import ArgumentParser

def print_message(msg: str = "This line will be printed.") -> None:
    #/ This function prints the given message to stdout.
    print(msg)

def main() -> None:
    #/ Parse command-line arguments to get the message to print.
    p = ArgumentParser(description="Print a message.")
    p.add_argument("-m", "--message", default="This line will be printed.")
    args = p.parse_args()
    print_message(args.message)

if __name__ == "__main__":
    main()