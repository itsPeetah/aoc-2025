TILE_VOID = 0
TILE_START = 1
TILE_SPLITTER = 2
TILE_BEAM = 3


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


def advance_line(current_line_index: int, world: list[list[int]]) -> int:
    def update_cell(line_idx: int, cell_idx: int, value: int) -> None:
        if 0 <= cell_idx < len(world[line_idx]):
            world[line_idx][cell_idx] = value

    splits_counter = 0
    previous_line = world[current_line_index - 1]
    current_line = world[current_line_index]
    for i in range(len(current_line)):
        p = previous_line[i]
        c = current_line[i]
        if p == TILE_START:
            update_cell(current_line_index, i, TILE_BEAM)
        elif p == TILE_BEAM:
            if c == TILE_VOID:
                update_cell(current_line_index, i, TILE_BEAM)
            elif c == TILE_SPLITTER:
                update_cell(current_line_index, i - 1, TILE_BEAM)
                update_cell(current_line_index, i + 1, TILE_BEAM)
                splits_counter += 2
    return splits_counter


def part1(world: list[list[int]]):
    cum_sum = 0
    for i in range(1, len(world)):
        cum_sum += advance_line(i, world)
    return cum_sum


world = parse("input/day7.txt")
p1 = part1(world)
print("Total splits for part 1:", p1)
