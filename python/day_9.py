from helpers import get_text_input, timed_run


def parse(text: str) -> list[tuple[int, int]]:
    return [tuple(map(int, line.split(","))) for line in text.split("\n")]


def part1(vertices: list[tuple[int, int]]):
    max_area = 0
    max_indices = (0, 0)
    for i in range(len(vertices)):
        xi, yi = vertices[i]
        for j in range(i, len(vertices)):
            xj, yj = vertices[j]
            area = (abs(xi - xj) + 1) * (abs(yi - yj) + 1)
            if area > max_area:
                max_area = area
                max_indices = i, j
    return max_area, max_indices


def part2(vertices: list[tuple[int, int]]): ...


text_input = get_text_input(9, True)
vertices = parse(text_input)

p1, indices = timed_run("part 1", part1, vertices)
print(
    "The largest rectangle has area:",
    p1,
    f" - vertices #{indices[0]} ({vertices[indices[0]]}) and #{indices[1]} ({vertices[indices[1]]})",
)
print("\n===\n")

p2 = timed_run("part 2", part2, vertices)


print("Largest rectangle for part 2:", p2)
