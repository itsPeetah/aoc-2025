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


def merge_ranges(ra: tuple[int], rb: tuple[int]) -> tuple[tuple[int], bool]:
    return (
        ((min(ra[0], rb[0]), max(ra[1], rb[1])), (0, -1))
        if (
            (ra[1] >= rb[0] and ra[1] <= rb[1])
            or (rb[0] >= ra[0] and rb[0] <= ra[1])
            or (rb[1] >= ra[0] and rb[1] <= ra[1])
            or (ra[0] >= rb[0] and ra[0] <= rb[1])
        )
        else (rb, ra)
    )


def collapse_range_list(ranges: list[tuple[int]]) -> list[tuple[int]]:
    # rs = sorted([r for r in ranges], key=lambda r: r[1])
    # for i in range(len(rs) - 1, 0, -1):
    #     rs[i - 1 : i + 1] = merge_ranges(rs[i], rs[i - 1])
    # return rs

    rs_ = [
        [
            (
                rs,  # the list of merged ranges
                rs.__setitem__(
                    i - 1,
                    # the following is the range merge
                    (
                        (
                            (
                                min(rs[i][0], rs[i - 1][0]),
                                max(rs[i][1], rs[i - 1][1]),
                            ),
                            (0, -1),
                        )
                        if (
                            (rs[i][1] >= rs[i - 1][0] and rs[i][1] <= rs[i - 1][1])
                            or (rs[i - 1][0] >= rs[i][0] and rs[i - 1][0] <= rs[i][1])
                            or (rs[i - 1][1] >= rs[i][0] and rs[i - 1][1] <= rs[i][1])
                            or (rs[i][0] >= rs[i - 1][0] and rs[i][0] <= rs[i - 1][1])
                        )
                        else (rs[i - 1], rs[i])
                    )[
                        0
                    ],  # take the first returned value
                ),
                rs.__setitem__(
                    i,
                    # the following is the range merge
                    (
                        (
                            (
                                min(rs[i][0], rs[i - 1][0]),
                                max(rs[i][1], rs[i - 1][1]),
                            ),
                            (0, -1),
                        )
                        if (
                            (rs[i][1] >= rs[i - 1][0] and rs[i][1] <= rs[i - 1][1])
                            or (rs[i - 1][0] >= rs[i][0] and rs[i - 1][0] <= rs[i][1])
                            or (rs[i - 1][1] >= rs[i][0] and rs[i - 1][1] <= rs[i][1])
                            or (rs[i][0] >= rs[i - 1][0] and rs[i][0] <= rs[i - 1][1])
                        )
                        else (rs[i - 1], rs[i])
                    )[
                        1
                    ],  # take the second returned value
                ),
            )[
                0
            ]  # take just the list
            for i in [i for i in range(len(rs) - 1, 0, -1)]
        ][  # get the decreasing indices
            0
        ]  # take just one copy of 'sortd'
        for rs in [sorted([r for r in ranges], key=lambda r: r[1])]  # define sortd
    ][0]

    return rs_

    # rs = sorted([r for r in ranges], key=lambda r: r[1])
    # for i in range(len(rs) - 1, 0, -1):
    #     rs[i - 1 : i + 1] = (
    #         ((min(rs[i][0], rs[i - 1][0]), max(rs[i][1], rs[i - 1][1])), (0, -1))
    #         if (
    #             (rs[i][1] >= rs[i - 1][0] and rs[i][1] <= rs[i - 1][1])
    #             or (rs[i - 1][0] >= rs[i][0] and rs[i - 1][0] <= rs[i][1])
    #             or (rs[i - 1][1] >= rs[i][0] and rs[i - 1][1] <= rs[i][1])
    #             or (rs[i][0] >= rs[i - 1][0] and rs[i][0] <= rs[i - 1][1])
    #         )
    #         else (rs[i - 1], rs[i])
    #     )
    # return rs

    # rs = sorted([r for r in ranges], key=lambda r: r[1])
    # for i in range(len(rs) - 1, 0, -1):
    #     rs[i - 1 : i + 1] = (
    #         ((min(rs[i][0], rs[i - 1][0]), max(rs[i][1], rs[i - 1][1])), (0, -1))
    #         if (
    #             (rs[i][1] >= rs[i - 1][0] and rs[i][1] <= rs[i - 1][1])
    #             or (rs[i - 1][0] >= rs[i][0] and rs[i - 1][0] <= rs[i][1])
    #             or (rs[i - 1][1] >= rs[i][0] and rs[i - 1][1] <= rs[i][1])
    #             or (rs[i][0] >= rs[i - 1][0] and rs[i][0] <= rs[i - 1][1])
    #         )
    #         else (rs[i - 1], rs[i])
    #     )
    # return rs


# Includes parsing
def part1():
    return [
        sum([1 if any([m <= id <= M for m, M in ranges]) else 0 for id in ids])
        for ranges, ids in
        # parsing
        [
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


def part2():
    return sum(
        [
            M - m + 1
            for m, M in [
                [
                    (
                        rs,  # the list of merged ranges
                        rs.__setitem__(
                            i - 1,
                            # the following is the range merge
                            (
                                (
                                    (
                                        min(rs[i][0], rs[i - 1][0]),
                                        max(rs[i][1], rs[i - 1][1]),
                                    ),
                                    (0, -1),
                                )
                                if (
                                    (
                                        rs[i][1] >= rs[i - 1][0]
                                        and rs[i][1] <= rs[i - 1][1]
                                    )
                                    or (
                                        rs[i - 1][0] >= rs[i][0]
                                        and rs[i - 1][0] <= rs[i][1]
                                    )
                                    or (
                                        rs[i - 1][1] >= rs[i][0]
                                        and rs[i - 1][1] <= rs[i][1]
                                    )
                                    or (
                                        rs[i][0] >= rs[i - 1][0]
                                        and rs[i][0] <= rs[i - 1][1]
                                    )
                                )
                                else (rs[i - 1], rs[i])
                            )[
                                0
                            ],  # take the first returned value
                        ),
                        rs.__setitem__(
                            i,
                            # the following is the range merge
                            (
                                (
                                    (
                                        min(rs[i][0], rs[i - 1][0]),
                                        max(rs[i][1], rs[i - 1][1]),
                                    ),
                                    (0, -1),
                                )
                                if (
                                    (
                                        rs[i][1] >= rs[i - 1][0]
                                        and rs[i][1] <= rs[i - 1][1]
                                    )
                                    or (
                                        rs[i - 1][0] >= rs[i][0]
                                        and rs[i - 1][0] <= rs[i][1]
                                    )
                                    or (
                                        rs[i - 1][1] >= rs[i][0]
                                        and rs[i - 1][1] <= rs[i][1]
                                    )
                                    or (
                                        rs[i][0] >= rs[i - 1][0]
                                        and rs[i][0] <= rs[i - 1][1]
                                    )
                                )
                                else (rs[i - 1], rs[i])
                            )[
                                1
                            ],  # take the second returned value
                        ),
                    )[
                        0
                    ]  # take just the list
                    for i in [i for i in range(len(rs) - 1, 0, -1)]
                ][  # get the decreasing indices
                    0
                ]  # take just one copy of 'sortd'
                for rs in [
                    sorted(
                        [
                            r
                            for r in
                            # parsing
                            tuple(
                                map(
                                    lambda block: [
                                        (
                                            tuple(map(int, line.split("-")))
                                            if "-" in line
                                            else int(line)
                                        )
                                        for line in block.strip().split("\n")
                                    ],
                                    open("input/day5.txt").read().split("\n\n"),
                                )
                            )[
                                0
                            ]  # just the ranges (no ids)
                        ],
                        key=lambda r: r[1],
                    )
                ]  # define sortd
            ][0]
        ]
    )


ranges, ids = parse("input/day5.txt")
ranges = collapse_range_list(ranges)
print("Fresh ids (part 1):", part1())
print("Total fresh ids (part 2):", part2())
