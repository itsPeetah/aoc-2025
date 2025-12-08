from helpers import get_text_input


def parse(text: str) -> tuple[list[tuple[int]], list[int]]:
    ranges = []
    ids = []
    ranges_txt, ids_txt = text.split("\n\n")
    for range_line in ranges_txt.strip().split("\n"):
        a, b = tuple(map(int, range_line.split("-")))
        ranges.append((a, b))
    for id in ids_txt.strip().split("\n"):
        ids.append(int(id))
    return ranges, ids


def merge_ranges(range_a: tuple[int], range_b: tuple[int]) -> tuple[tuple[int], bool]:
    am, aM = range_a
    bm, bM = range_b
    if (
        (aM >= bm and aM <= bM)
        or (bm >= am and bm <= aM)
        or (bM >= am and bM <= aM)
        or (am >= bm and am <= bM)
    ):
        return (min(am, bm), max(aM, bM)), True
    return (-1, -1), False


def collapse_range_list(ranges: list[tuple[int]]) -> list[tuple[int]]:
    rs = sorted([r for r in ranges], key=lambda interval: interval[1])
    for i in range(len(rs) - 1, 0, -1):
        new_r, merged = merge_ranges(rs[i], rs[i - 1])
        if merged:
            rs[i - 1] = new_r
            rs.pop(i)
    return rs


def part1(ranges: list[int], ids: list[int]):
    cum_sum = 0
    for id in ids:
        for m, M in ranges:
            if m <= id <= M:
                cum_sum += 1
                break
    return cum_sum


def part2(ranges: list[tuple[int]]):
    cum_sum = 0
    for m, M in ranges:
        delta = M - m
        cum_sum += delta + 1
    return cum_sum


text_input = get_text_input(5, False)
ranges, ids = parse(text_input)
p1 = part1(ranges, ids)

print("Fresh ids (part 1):", p1)
ranges = collapse_range_list(ranges)
p1 = part1(ranges, ids)
p2 = part2(ranges)

print("Fresh ids (part 1):", p1)
print("Total fresh ids (part 2):", p2)
