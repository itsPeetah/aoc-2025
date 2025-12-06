import re


def parse(path: str):
    with open(path) as file:
        txt = re.sub(r" +", " ", file.read())
    return [
        [c if c in ("*", "+") else int(c) for c in line]
        for line in [line.strip().split(" ") for line in txt.split("\n")]
    ]


def part1(data: list[list]):
    def add(a, b):
        return a + b

    def mul(a, b):
        return a * b

    cum_sum = 0
    for x in range(len(data[0])):
        op = add if data[-1][x] == "+" else mul
        res = data[0][x]
        for y in range(1, len(data) - 1):
            res = op(res, data[y][x])
        cum_sum += res
    return cum_sum


data = parse("input/day6.txt")
p1 = part1(data)

print("Grand total for part 1:", p1)
