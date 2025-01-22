"""Make my code pretty."""

import sys
from pathlib import Path

from black import patched_main as black_main
from isort.main import main as isort_main
from loguru import logger


def main() -> None:
    """Lint and format the codebase."""
    repo_root = Path(__file__).parent.parent

    # set up CLI args as if we ran it targeting the repo root
    sys.argv = [sys.executable, str(repo_root)]

    logger.info("running isort")
    isort_main()

    logger.info("running black")
    try:
        black_main()
    except SystemExit:
        pass  # black calls system exit when running the main for some reason

    logger.info("finished linting")


if __name__ == "__main__":
    main()
