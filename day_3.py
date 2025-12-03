import threading


def parse():
    res = []
    with open("input/day3.txt") as file:
        for line in file:
            res.append([int(j) for j in line.strip()])
    return res


# again I'm doing the idiot solution because I'm in uni and
# I need to make my thesis presentation for the 10th lol
def part1():
    # honestly looking at part 2 this is not even the correct approach I think
    def get_bank_joltage(bank: list[int]) -> int:
        l = len(bank)
        curr_max = -1
        for t in range(l):
            for u in range(t + 1, l):
                j = 10 * bank[t] + bank[u]
                if curr_max < j:
                    curr_max = j
        return curr_max

    banks = parse()
    cum_sum = 0
    for bank in banks:
        cum_sum += get_bank_joltage(bank)

    return cum_sum


def part2():
    banks = parse()
    cum_sum = 0

    def get_bank_joltage(bank: list[int]) -> int:
        def remove_lowest_from_left(bank: list[int]) -> tuple[list[int], int]:
            # Remove the first value from the start that is lower than its immediate neighbour to the right
            index_to_remove = 0
            for i in range(1, len(bank)):
                if bank[i] > bank[i - 1]:
                    break
                index_to_remove = i
            new_bank = bank[:index_to_remove] + bank[index_to_remove + 1 :]
            return new_bank, index_to_remove

        while len(bank) > 12:
            bank, removed = remove_lowest_from_left(bank)
        js = [bank[i] for i in range(len(bank))]
        cum_sum = 0
        for j in js:
            cum_sum *= 10
            cum_sum += j
        return cum_sum

    for bank in banks:
        cum_sum += get_bank_joltage(bank)
    return cum_sum


print("Total output joltage for part 1:", part1())
print("Total output joltage for part 2:", part2())
