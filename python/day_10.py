from helpers import get_text_input, timed_run


def parse(text: str) -> list[tuple[int, int]]:
    def parse_indicator_lights(string: str, start_from_index: int):
        i = start_from_index
        j = i + 1
        print(string, i, j)
        while string[j] != "]":
            j += 1
        return [True if c == "#" else False for c in string[i + 1 : j]]

    def parse_button_wirings(string: str, start_from_index: int): ...
    def parse_joltage_requirements(string: str, start_from_index: int): ...

    res = []
    for line in text.split("\n"):
        lights = None
        wirings = None
        joltage = None
        for idx in range(0, len(line)):
            if text[idx] == "[":
                lights = parse_indicator_lights(line, idx)
        res.append((lights, wirings, joltage))
    return res


text_input = get_text_input(10, True)
parsed = parse(text_input)

print(parsed)
