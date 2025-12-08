from helpers import get_text_input


def parse(text: str):
    lines = []
    lines.extend([line.strip() for line in text.split("\n")])
    return [(line[0], int(line[1:])) for line in lines]


def part1(lines):
    turns = [x[1] if x[0] == "R" else -x[1] for x in lines]
    val = 50
    count = 0
    for t in turns:
        val += t
        if val % 100 == 0:
            count += 1
    return count


def part2(lines):
    turns = [(1 if x[0] == "R" else -1, x[1]) for x in lines]
    val = 50
    count = 0
    for dir, clicks in turns:
        # I'm doing it very bad for now because I'm in bed
        # and it is 1030 pm I'm going to come back to this lol
        for x in range(clicks):
            val += dir
            if val % 100 == 0:
                count += 1
    return count


text_input = get_text_input(1, False)
lines = parse(text_input)
p1 = part1(lines)
p2 = part2(lines)


print("Password for part 1 is:", p1)
print("Password for part 2 is:", p2)
