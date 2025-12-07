TILE_START = -1
TILE_SPLITTER = -2
TILE_VOID = 0
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
    """solves both part 1 and 2"""
    splits_counter = 0  # part 1: just count the number of splits
    current_line = world[current_line_index]
    for i in range(len(current_line)):
        above = world[current_line_index - 1][i]
        if above == TILE_START:
            current_line[i] = TILE_BEAM
        elif above > 0:
            if current_line[i] == TILE_SPLITTER:
                # instead of using any recursion or memoization, we can just
                # duplicate the value of the beam above to the left and the right
                # the value of our beam is the number of timelines, and when we split
                # we duplicate it left and right, indicating that there are two timelines
                # starting from this point which had the same common history
                current_line[i - 1] += above
                current_line[i + 1] += above
                splits_counter += 1  # increase split counter for every split
            elif current_line[i] >= TILE_VOID:  # if void or beam
                current_line[i] += above  # extend the void or the beam above

    return splits_counter


def part1(world: list[list[int]]):
    cum_sum = 0
    for i in range(1, len(world)):
        cum_sum += advance_beams(i, world)
    return cum_sum


def part2(world: list[list[int]]) -> int:
    for i in range(1, len(world)):
        advance_beams(i, world)
    return sum(
        world[-1]
    )  # the number of timelines is the sum of the beam value on the last row


p1 = part1(parse("input/day7.txt"))
p2 = part2(parse("input/day7.txt"))
print("Total splits for part 1:", p1)
print("Total timelines for part 2:", p2)
