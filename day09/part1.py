import argparse
import math
from pathlib import Path

import pytest

INPUT_TXT = Path("input.txt")


class End:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = {(x, y)}

    def move(self, direction):
        if direction == "U":
            self.y -= 1
            self.visited.add((self.x, self.y))
        elif direction == "D":
            self.y += 1
            self.visited.add((self.x, self.y))
        elif direction == "L":
            self.x -= 1
            self.visited.add((self.x, self.y))
        elif direction == "R":
            self.x += 1
            self.visited.add((self.x, self.y))

    def diagonal_move(self, head_x, head_y):
        current_distance_x = head_x - self.x
        current_distance_y = head_y - self.y
        if abs(current_distance_x) == 2:
            self.y = head_y
            if current_distance_x > 0:
                self.x += 1
            else:
                self.x -= 1
        if abs(current_distance_y) == 2:
            self.x = head_x
            if current_distance_y > 0:
                self.y += 1
            else:
                self.y -= 1

        self.visited.add((self.x, self.y))


def compute(s: str) -> int:
    head = End(0, 0)
    tail = End(0, 0)

    lines = s.splitlines()
    for line in lines:
        direction, how_far = line.split(" ")
        for _ in range(int(how_far)):
            head.move(direction)
            current_distance = math.hypot(head.x - tail.x, head.y - tail.y)
            if current_distance == 2.0:
                tail.move(direction)
            elif current_distance > 2.2:
                tail.diagonal_move(head.x, head.y)

    return len(tail.visited)


INPUT_S = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
EXPECTED = 13


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
