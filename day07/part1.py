import argparse
import os.path
from pathlib import Path

import pytest

INPUT_TXT = Path("input.txt")


MAX_SIZE = 100_000


def size(dirname, files):
    size = 0
    for f, s in files.items():
        if f.startswith(f"{dirname}\\"):
            size += s

    if size > MAX_SIZE:
        return 0
    else:
        return size


def parse_tree(s: str):
    """
    Taken from https://github.com/anthonywritescode/aoc2022/blob/main/day07/part1.py
    """
    files = {}
    dirs = {"\\"}

    cwd = "/"
    for line in s.splitlines():
        part1, part2, *the_rest = line.split(" ")
        if part2 == "cd":
            change_dir = the_rest[0]
            if change_dir == "..":
                cwd = os.path.dirname(cwd) or "/"
            else:
                cwd = os.path.join(cwd, change_dir)
                dirs.add(os.path.normpath(cwd))
        elif part1.isdigit():
            files[os.path.normpath(os.path.join(cwd, part2))] = int(part1)

    return files, dirs


def compute(s: str) -> int:
    files, dirs = parse_tree(s)
    root_size = sum(files.values())
    if root_size > MAX_SIZE:
        root_size = 0
    return root_size + sum(size(dirname, files) for dirname in dirs)


INPUT_S = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
EXPECTED = 95437


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
