import argparse
from pathlib import Path

import pytest

INPUT_TXT = Path("input.txt")


def is_visible(y, x, grid):
    """
    True if visible else False
    """
    LENGHT = len(grid)
    if x == 0 or y == 0 or x == LENGHT - 1 or y == LENGHT - 1:
        return True
    point_value = grid[y][x]

    if all(grid[y][r] < point_value for r in range(x)):
        return True
    if all(grid[y][r] < point_value for r in range(x + 1, LENGHT)):
        return True

    if all(grid[r][x] < point_value for r in range(y)):
        return True
    if all(grid[r][x] < point_value for r in range(y + 1, LENGHT)):
        return True

    return False


@pytest.mark.parametrize(
    ("y", "x", "expected"),
    (
        (2, 2, False),
        (1, 3, False),
        (3, 1, False),
        (3, 3, False),
        (2, 1, True),
        (0, 0, True),
        (2, 0, True),
        (2, 4, True),
        (0, 2, True),
        (4, 1, True),
        (4, 4, True),
    ),
)
def test_is_visible(x, y, expected) -> None:
    grid = [list(map(int, line)) for line in INPUT_S.splitlines()]
    assert is_visible(x, y, grid) == expected


def compute(s: str) -> int:
    lines = s.splitlines()

    grid = [list(map(int, line)) for line in lines]
    LENGHT = len(grid)
    # num = 0
    # for y in range(LENGHT):
    #     for x in range(LENGHT):
    #         if is_visible(y, x, grid):
    #             num += 1
    sum(is_visible(y, x, grid) for y in range(LENGHT) for x in range(LENGHT))
    return sum(is_visible(y, x, grid) for y in range(LENGHT) for x in range(LENGHT))


INPUT_S = """\
30373
25512
65332
33549
35390
"""
EXPECTED = 21


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
