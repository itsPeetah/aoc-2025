def parse(path: str) -> list[int]:
    res = []
    with open(path) as file:
        for line in file:
            res.append([int(j) for j in line.strip()])
    return res


def calculate_bank_joltage(bank: list[int], battery_count: int) -> int:
    while len(bank) > battery_count:
        index_to_remove = 0
        # I'm still pretty sure I can remove the double loop
        for i in range(1, len(bank)):
            if bank[i] > bank[i - 1]:
                break
            index_to_remove = i
        bank = bank[:index_to_remove] + bank[index_to_remove + 1 :]

    js = [bank[i] for i in range(len(bank))]
    total = 0
    for j in js:
        total *= 10
        total += j
    return total


def calculate_joltage(num_batteries: int, banks: list[int]) -> int:
    return sum([calculate_bank_joltage(bank, num_batteries) for bank in banks])


banks = parse("input/day3.txt")
print("Total output joltage for part 1:", calculate_joltage(2, banks))
print("Total output joltage for part 2:", calculate_joltage(12, banks))
