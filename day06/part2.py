import argparse
from pathlib import Path
from collections import deque
import pytest


INPUT_TXT = Path("input.txt")


def compute(s: str) -> int:
    unique_characters = 14
    d = deque(maxlen=unique_characters)
    for n, element in enumerate(s, start=1):
        d.append(element)
        if n >= unique_characters:
            if len(set(d)) == len(d):
                return n


INPUT_S = """\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""
EXPECTED = 19


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (
        (INPUT_S, EXPECTED),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    ),
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
