def get_text_input(day: int, example: bool, relative_dir: str = ".") -> str:
    dir = "example_input" if example else "input"
    with open(f"{relative_dir}/{dir}/day_{day}.txt") as file:
        return file.read()
