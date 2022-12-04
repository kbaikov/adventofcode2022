import argparse
from pathlib import Path
import pytest


INPUT_TXT = Path("input.txt")


def compute(s: str) -> int:
    lines = s.splitlines()
    count = 0
    for line in lines:
        assignment1, assignment2 = line.split(",")
        a1, _, b1 = assignment1.partition("-")
        a2, _, b2 = assignment2.partition("-")
        sections1 = set(range(int(a1), int(b1) + 1))
        sections2 = set(range(int(a2), int(b2) + 1))
        if sections1.intersection(sections2) or sections2.intersection(sections1):
            count += 1

    return count


INPUT_S = """\
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""
EXPECTED = 4


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
