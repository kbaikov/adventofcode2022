import argparse
from collections import deque
from pathlib import Path
import re
import itertools


import pytest


INPUT_TXT = Path("input.txt")


class Interpreter:
    def __init__(self, initial_state):
        self.stacks = [None] * (len(initial_state) + 1)
        for stack in initial_state:
            *letters, stack_number = stack
            self.stacks[int(stack_number)] = deque(
                [letter for letter in letters[::-1] if letter.isalnum()]
            )

    def value_move(self, crates, from_, to):
        to_move = []
        for _ in range(crates):
            to_move.append(self.stacks[from_].pop())
        self.stacks[to].extend(to_move[::-1])

    def current_crates_on_top(self):
        return "".join([letter[-1] for letter in self.stacks if letter is not None])

    def run_code(self, what_to_execute):
        instrs = what_to_execute["instructions"]

        for each_step in instrs:
            instruction, crates, from_, to = each_step
            if instruction == "MOVE":
                self.value_move(crates, from_, to)


def compute(s: str) -> str:
    initial_state, moves = s.split("\n\n")
    init = itertools.zip_longest(*initial_state.splitlines(), fillvalue=" ")
    init = filter(lambda x: x[-1].isdigit(), init)
    interpreter = Interpreter(list(init))
    what_to_execute: dict[str, list] = {"instructions": []}
    for move in moves.splitlines():
        m = re.match(r"^move (\d+) from (\d+) to (\d+)", move)
        if m:
            crates, from_, to = m.groups()
            what_to_execute["instructions"].append(("MOVE", int(crates), int(from_), int(to)))

    interpreter.run_code(what_to_execute)

    return interpreter.current_crates_on_top()


INPUT_S = """\
    [D]
[N] [C]
[Z] [M] [P]
 1   2   3

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""
EXPECTED = "MCD"


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
