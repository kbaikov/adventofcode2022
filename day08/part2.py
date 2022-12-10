import argparse
from pathlib import Path

import pytest

INPUT_TXT = Path("input.txt")


def scenic_score(y, x, grid):
    """
    Scenic score
    """
    LENGHT = len(grid)
    point_value = grid[y][x]

    left = 0
    for r in reversed(range(x)):
        if grid[y][r] < point_value:
            left += 1
        elif grid[y][r] >= point_value:
            left += 1
            break

    right = 0
    for r in range(x + 1, LENGHT):
        if grid[y][r] < point_value:
            right += 1
        elif grid[y][r] >= point_value:
            right += 1
            break

    up = 0
    for r in reversed(range(y)):
        if grid[r][x] < point_value:
            up += 1
        elif grid[r][x] >= point_value:
            up += 1
            break
    down = 0
    for r in range(y + 1, LENGHT):
        if grid[r][x] < point_value:
            down += 1
        elif grid[r][x] >= point_value:
            down += 1
            break

    return left * right * up * down


@pytest.mark.parametrize(
    ("y", "x", "score"),
    (
        (1, 2, 4),
        (3, 2, 8),
    ),
)
def test_scenic_score(y, x, score) -> None:
    grid = [list(map(int, line)) for line in INPUT_S.splitlines()]
    assert scenic_score(y, x, grid) == score


def compute(s: str) -> int:
    lines = s.splitlines()

    grid = [list(map(int, line)) for line in lines]
    LENGHT = len(grid)

    return max(scenic_score(y, x, grid) for y in range(LENGHT) for x in range(LENGHT))


INPUT_S = """\
30373
25512
65332
33549
35390
"""
EXPECTED = 8


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
