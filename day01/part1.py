import argparse
from pathlib import Path
import pytest


INPUT_TXT = Path("input.txt")


def compute(s: str) -> int:
    elves = s.strip().split("\n\n")
    calories = []
    for elf_numbers in elves:
        calories.append(sum(int(number.strip()) for number in elf_numbers.splitlines()))
    return max(calories)


INPUT_S = """\
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""
EXPECTED = 24000


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
