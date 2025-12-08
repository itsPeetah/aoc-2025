from helpers import get_text_input


def parse(text: str) -> list[tuple]:
    data = []
    *lines, operators = [line for line in text.split("\n")]
    i = 0
    l = len(operators)
    while i < l:
        c = operators[i]
        if c != " ":
            op = c
            nums = []
            j = i + 1
            while j < l and operators[j] == " ":
                j += 1
            splitpoint = j - 1 if j < l else j
            for line in lines:
                nums.append(line[i:splitpoint])
        data.append((op, nums))
        i = j
    return data


def part1(data: list[tuple]) -> int:

    cum_sum = 0
    for op, nums in data:
        res = int(nums[0])
        for i in range(1, len(nums)):
            res = ((lambda a, b: a + b) if op == "+" else (lambda a, b: a * b))(
                res, int(nums[i])
            )
        cum_sum += res
    return cum_sum


def part2(data: list[tuple]) -> int:
    def rotate_num_matrix(nums: list[str]) -> list[str]:
        rotated = []
        for x in range(len(nums[0]) - 1, -1, -1):
            num = ""
            for y in range(len(nums)):
                num += nums[y][x]
            rotated.append(num)
        return rotated

    new_data = []
    for op, nums in data:
        new_data.append((op, rotate_num_matrix(nums)))
    return part1(new_data)


text_input = get_text_input(6, False)
data = parse(text_input)
p1 = part1(data)
p2 = part2(data)

print("Grand total for part 1:", p1)
print("Grand total for part 2:", p2)
