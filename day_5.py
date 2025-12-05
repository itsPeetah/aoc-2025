def parse(path: str) -> tuple[list[tuple[int]], list[int]]:
    ranges = []
    ids = []
    with open(path) as file:
        ranges_txt, ids_txt = file.read().split("\n\n")
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
    rs = [r for r in ranges]
    curr_size = len(rs)
    while True:
        for a in range(curr_size - 1, -1, -1):
            ra = rs[a]
            for b in range(a - 1, -1, -1):
                rb = rs[b]
                new_r, merged = merge_ranges(ra, rb)
                if merged:
                    rs.pop(a)
                    rs[b] = new_r
                    break
        last_size = curr_size
        curr_size = len(rs)
        if last_size == curr_size:
            break
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


ranges, ids = parse("input/day5.txt")
ranges = collapse_range_list(ranges)
print("Fresh ids (part 1):", part1(ranges, ids))
print("Total fresh ids (part 2):", part2(ranges))
