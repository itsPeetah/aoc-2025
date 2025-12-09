from time import time_ns


def get_text_input(day: int, example: bool, relative_dir: str = ".") -> str:
    dir = "example_input" if example else "input"
    with open(f"{relative_dir}/{dir}/day_{day}.txt") as file:
        return file.read()


def timed_run(name: str, function, *args):
    t0 = time_ns()
    res = function(*args)
    t1 = time_ns()

    print("Completed", name, f"in {(t1-t0) / 1_000_000}ms")
    return res
