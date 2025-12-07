TILE_VOID = 0
TILE_START = -1
TILE_SPLITTER = -2
TILE_BEAM = 1


def parse(path: str) -> list[list[int]]:
    def map_character(char: str) -> int:
        match char:
            case "S":
                return TILE_START
            case "^":
                return TILE_SPLITTER
            case _:
                return TILE_VOID

    world = []
    with open(path) as file:
        for line in file:
            world.append([map_character(c) for c in line.strip()])
    return world


def advance_beams(current_line_index: int, world: list[list[int]]) -> int:
    splits_counter = 0
    previous_line = world[current_line_index - 1]
    current_line = world[current_line_index]
    for i in range(len(current_line)):
        p = previous_line[i]
        if p == TILE_START:
            current_line[i] = TILE_BEAM
        elif p > 0:
            if current_line[i] == TILE_SPLITTER:
                splits_counter += 1
                current_line[i - 1] += previous_line[i]
                current_line[i + 1] += previous_line[i]
            elif current_line[i] == TILE_VOID or current_line[i] >= TILE_BEAM:
                current_line[i] += previous_line[i]

    return splits_counter


def part1(world: list[list[int]]):
    cum_sum = 0
    for i in range(1, len(world)):
        cum_sum += advance_beams(i, world)
    return cum_sum


def part2(world: list[list[int]]) -> int:
    for i in range(1, len(world)):
        advance_beams(i, world)
    return sum(world[-1])


p1 = part1(parse("input/day7.txt"))
p2 = part2(parse("input/day7.txt"))
print("Total splits for part 1:", p1)
print("Total timelines for part 2:", p2)
