from helpers import get_text_input


def parse(text: str) -> tuple[list[int], int]:
    line_length = 0
    paper_rolls = []

    for line in text.split("\n"):
        line_length = len(line)
        paper_rolls.extend([0 if c == "." else 1 for c in line])
    return paper_rolls, line_length


def find_accessible_rolls(rolls: list[int], columns: int) -> tuple[int, list[int]]:
    rows = len(rolls) // columns

    def get_value_at(col: int, row: int) -> int:
        valid_col = col >= 0 and col < columns
        valid_row = row >= 0 and row < rows
        if not valid_col or not valid_row:
            return 0
        return rolls[columns * row + col]

    def convolute(center_col: int, center_row: int) -> int:
        neighbours = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                neighbours += get_value_at(center_col + i, center_row + j)
        return neighbours

    cum_sum = 0
    rows = len(rolls) // columns
    new_gen = []
    for y in range(rows):
        for x in range(columns):
            roll_value = get_value_at(x, y)
            if roll_value > 0 and convolute(x, y) < 4:
                cum_sum += 1
                roll_value = 0
            new_gen.append(roll_value)
    return cum_sum, new_gen


def find_and_remove_accessible_rolls(
    rolls: list[int], columns: int, max_depth: int
) -> int:
    depth = 0
    cum_sum = 0
    curr_gen = rolls
    while max_depth < 0 or depth < max_depth:
        found, new_gen = find_accessible_rolls(curr_gen, columns)
        if found == 0:
            break
        curr_gen = new_gen
        cum_sum += found
        depth += 1

    return cum_sum


text_input = get_text_input(4, False)
rolls, row_len = parse(text_input)
p1 = find_and_remove_accessible_rolls(rolls, row_len, 1)
p2 = find_and_remove_accessible_rolls(rolls, row_len, -1)
print(
    "Accessible rolls for part 1:",
    p1,
)

print(
    "Accessible rolls for part 2:",
    p2,
)
