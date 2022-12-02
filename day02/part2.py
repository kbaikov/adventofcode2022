import argparse
from pathlib import Path
import pytest


INPUT_TXT = Path("input.txt")

VARIANT = {
    # rock
    "A X": 3 + 0,
    "A Y": 1 + 3,
    "A Z": 2 + 6,
    # paper
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    # scissors
    "C X": 2 + 0,
    "C Y": 3 + 3,
    "C Z": 1 + 6,
}


def compute(s: str) -> int:
    lines = s.splitlines()
    score = 0
    for line in lines:
        score += VARIANT[line]

    return score


INPUT_S = """\
A Y
B X
C Z
"""
EXPECTED = 12


@pytest.mark.parametrize(
    ("input_s", "expected"),
    ((INPUT_S, EXPECTED),),
)
def test(input_s: str, expected: int) -> None:
    assert compute(input_s) == expected


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("data_file", nargs="?", default=INPUT_TXT)
    args = parser.parse_args()

    with open(args.data_file, encoding="utf-8") as f:
        print(compute(f.read()))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
