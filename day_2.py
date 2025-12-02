import re


def parse():
    res = []
    with open("input/day2.txt") as file:
        ranges = [r.split("-") for r in file.read().strip().split(",")]
        res.extend([(int(r[0]), int(r[1])) for r in ranges])
    return res


def repeated_twice(number: int) -> bool:
    as_string = str(number)
    l = len(as_string)
    if l % 2 != 0:
        return False
    hl = l // 2
    return as_string[:hl] == as_string[hl:]


def repeated_multiple(number: int) -> bool:
    m = re.fullmatch(r"(\d+)\1+", str(number))
    return m != None


# again I'm doing the idiot solution because I'm in uni and
# I need to make my thesis presentation for the 10th lol
def part1():
    cum_sum = 0
    ranges = parse()
    for a, b in ranges:
        for x in range(a, b + 1):
            if repeated_twice(x):
                cum_sum += x
    return cum_sum


def part2():
    cum_sum = 0
    ranges = parse()
    for a, b in ranges:
        for x in range(a, b + 1):
            if repeated_multiple(x):
                cum_sum += x
    return cum_sum


print("The sum for part 1 is:", part1())
print("The sum for part 2 is:", part2())
