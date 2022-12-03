import argparse
from pathlib import Path
import pytest


INPUT_TXT = Path("input.txt")


def compute(s: str) -> int:
    lines = s.splitlines()
    priorities = []
    for line in lines:
        half_len_line = len(line) // 2
        half1, half2 = line[half_len_line:], line[:half_len_line]
        unique = next(filter(lambda x: x in half2, half1))
        if unique.islower():
            priorities.append(ord(unique) - 96)
        else:
            priorities.append(ord(unique) - 38)

    return sum(priorities)


INPUT_S = """\
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""
EXPECTED = 157


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
