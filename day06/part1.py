import argparse
from pathlib import Path
from collections import deque
import pytest


INPUT_TXT = Path("input.txt")


def compute(s: str) -> int:
    d = deque(maxlen=4)
    for n, element in enumerate(s, start=1):
        d.append(element)
        if n >= 4:
            if len(set(d)) == len(d):
                return n


INPUT_S = """\
mjqjpqmgbljsphdztnvjfqwrcgsmlb
"""
EXPECTED = 7


@pytest.mark.parametrize(
    ("input_s", "expected"),
    (
        (INPUT_S, EXPECTED),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
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
