def parse(path: str) -> tuple[list[tuple[int]], list[int]]:
    return tuple(
        map(
            lambda block: [
                tuple(map(int, line.split("-"))) if "-" in line else int(line)
                for line in block.strip().split("\n")
            ],
            open(path).read().split("\n\n"),
        )
    )


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


# Includes parsing
def part1():
    return [
        sum([1 if any([m <= id <= M for m, M in ranges]) else 0 for id in ids])
        for ranges, ids in [
            tuple(
                map(
                    lambda block: [
                        tuple(map(int, line.split("-"))) if "-" in line else int(line)
                        for line in block.strip().split("\n")
                    ],
                    open("input/day5.txt").read().split("\n\n"),
                )
            )
        ]
    ][0]


def part2(ranges: list[tuple[int]]):
    return sum([M - m + 1 for m, M in ranges])


ranges, ids = parse("input/day5.txt")
ranges = collapse_range_list(ranges)
print("Fresh ids (part 1):", part1())
print("Total fresh ids (part 2):", part2(ranges))
