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


def part2(vertices: list[tuple[int, int]]):
    def calculate_area(i, j) -> int:
        xi, yi = vertices[i]
        xj, yj = vertices[j]
        area = (abs(xi - xj) + 1) * (abs(yi - yj) + 1)
        return area

    def get_edges(xi, yi, xj, yj):
        return [
            (True, xi, (min(yi, yj), max(yi, yj))),
            (True, xj, (min(yi, yj), max(yi, yj))),
            (False, yi, (min(xi, xj), max(xi, xj))),
            (False, yj, (min(xi, xj), max(xi, xj))),
        ]

    def check_valid(i, j) -> bool:
        xi, yi = vertices[i]
        xj, yj = vertices[j]
        valid = True
        for vertical, fixed_axis, edge_range in get_edges(xi, yi, xj, yj):
            # check only points on perimeter
            for r in range(edge_range[0], edge_range[1] + 1):
                # point on perimeter
                p = (fixed_axis, r) if vertical else (r, fixed_axis)
                valid = False
                break
            break

        return valid

    max_area = 0
    max_indices = (0, 0)
    for i in range(len(vertices)):
        for j in range(i, len(vertices)):
            print(i, j, len(vertices))
            if not check_valid(i, j):
                continue
            area = calculate_area(i, j)
            if area > max_area:
                max_area = area
                max_indices = i, j
    return max_area, max_indices


text_input = get_text_input(9, False)
vertices = parse(text_input)

p1, indices = timed_run("part 1", part1, vertices)
print(
    "The largest rectangle for part 1 has area:",
    p1,
    f" - vertices #{indices[0]} ({vertices[indices[0]]}) and #{indices[1]} ({vertices[indices[1]]})",
)
print("\n===\n")

p2, indices = timed_run("part 2", part2, vertices)


print(
    "The largest rectangle for part 2 has area:",
    p2,
    f" - vertices #{indices[0]} ({vertices[indices[0]]}) and #{indices[1]} ({vertices[indices[1]]})",
)
