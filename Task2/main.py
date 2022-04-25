import argparse
from src.ui.consistent import Consistent
from src.ui.parallel import Parallel
from src.ui.research import Research


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="overlay face with a mask")
    parser.add_argument(
        "-t",
        "--type",
        type=str,
        help="app type: c - consistent, p - parallel, r - research",
    )

    args = parser.parse_args()

    if args.type == "c":
        app = Consistent()
    elif args.type == "p":
        app = Parallel()
    elif args.type == "r":
        app = Research()
    else:
        raise Exception(f"WRONG FLAG: {args.type}")

    app.mainloop()
