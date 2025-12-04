def parse(path: str) -> tuple[list[int], int]:
    line_length = 0
    paper_rolls = []
    with open(path) as file:
        for line in file:
            line = line.strip()
            line_length = len(line)
            paper_rolls.extend([0 if c == "." else 1 for c in line])
    return paper_rolls, line_length

def one_line_no_parsing(rolls: list[int], columns: int) -> int:
    # return sum([
    #     1 if (rolls[columns * y + x] if (x >= 0 and x < columns) and (y >= 0 and y < len(rolls) // columns) else 0) > 0
    #     and sum([(rolls[columns * (y+j) + (x+i)] if ((x+i) >= 0 and (x+i) < columns) and ((y+j) >= 0 and (y+j) < len(rolls) // columns) else 0) for i, j in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]]) < 4
    #     else 0 for y, x in [ (y, x) for x in [x for x in range(columns )] for y in range(len(rolls) // columns)]
    # ])
    return sum([1 if (rolls[columns * y + x] if (x >= 0 and x < columns) and (y >= 0 and y < len(rolls) // columns) else 0) > 0 and sum([(rolls[columns * (y+j) + (x+i)] if ((x+i) >= 0 and (x+i) < columns) and ((y+j) >= 0 and (y+j) < len(rolls) // columns) else 0) for i, j in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]]) < 4 else 0 for y, x in [ (y, x) for x in [x for x in range(columns )] for y in range(len(rolls) // columns)]])

rolls, row_len = parse("input/day4.txt")
print(
    "One line no parsing:",
    one_line_no_parsing(rolls, row_len) == 1480 # real solution
)

def one_line_with_parsing() -> int:
    # return [sum([
    #     1 if (rolls[columns * y + x] if (x >= 0 and x < columns) and (y >= 0 and y < len(rolls) // columns) else 0) > 0
    #     and sum([(rolls[columns * (y+j) + (x+i)] if ((x+i) >= 0 and (x+i) < columns) and ((y+j) >= 0 and (y+j) < len(rolls) // columns) else 0) for i, j in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]]) < 4
    #     else 0 for y, x in [ (y, x) for x in [x for x in range(columns )] for y in range(len(rolls) // columns)]
    # ]) for rolls, columns in [([0 if c == "." else 1 for c in open("input/day4.txt").read().strip() if c != "\n"], open("input/day4.txt").read().find("\n"))]][0]
    return [sum([1 if (rolls[columns * y + x] if (x >= 0 and x < columns) and (y >= 0 and y < len(rolls) // columns) else 0) > 0 and sum([(rolls[columns * (y+j) + (x+i)] if ((x+i) >= 0 and (x+i) < columns) and ((y+j) >= 0 and (y+j) < len(rolls) // columns) else 0) for i, j in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]]) < 4 else 0 for y, x in [ (y, x) for x in [x for x in range(columns )] for y in range(len(rolls) // columns)]]) for rolls, columns in [([0 if c == "." else 1 for c in open("input/day4.txt").read().strip() if c != "\n"], open("input/day4.txt").read().find("\n"))]][0]
    

print(
    "One line with parsing:",
    one_line_with_parsing() == 1480 # real solution
)

o = [sum([1 if (r[c * y + x] if (x >= 0 and x < c) and (y >= 0 and y < len(r) // c) else 0) > 0 and sum([(r[c * (y+j) + (x+i)] if ((x+i) >= 0 and (x+i) < c) and ((y+j) >= 0 and (y+j) < len(r) // c) else 0) for i, j in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]]) < 4 else 0 for y, x in [ (y, x) for x in [x for x in range(c)] for y in range(len(r) // c)]]) for r, c in [([0 if c == "." else 1 for c in open("input/day4.txt").read().strip() if c != "\n"], open("input/day4.txt").read().find("\n"))]][0]

print("Truly one line:", o,  o == 1480)