def parse(path: str) -> list[tuple[int]]:
    with open(path) as file:
        return [tuple(map(int, line.strip().split(","))) for line in file]


def distance(p0: tuple[int, int, int], p1: tuple[int, int, int]) -> float:
    x0, y0, z0 = p0
    x1, y1, z1 = p1
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2 + (z0 - z1) ** 2) ** 0.5


def make_graph(node_positions: list[tuple[int]]):
    labeled_nodes = [(index, position) for index, position in enumerate(node_positions)]
    edge_weights = {}
    for i in range(0, len(labeled_nodes)):
        for j in range(i, len(labeled_nodes)):
            if i == j:
                continue
            edge_weights[(i, j)] = distance(labeled_nodes[i][1], labeled_nodes[j][1])
    return (
        labeled_nodes,
        edge_weights,
        sorted(edge_weights.keys(), key=lambda k: edge_weights[k]),
    )


def part1(graph: tuple[list, dict, list], max_connections=1000):
    l_nodes, _, closest_pairs = graph
    circuit_labels = [(label, False) for label, _ in l_nodes]

    def decide_cirtcuit(i: int, j: int) -> tuple[int, bool, bool]:
        circi, conni = circuit_labels[i]
        circj, connj = circuit_labels[j]
        if conni and connj:
            if circi == circj:
                return -1, False, False
            return circi, True, True
        elif conni:
            return circi, True, False
        elif connj:
            return circj, True, False
        else:
            return circi, True, False

    def connect_closest(iteration: int):
        close_i, close_j = closest_pairs[iteration]

        label, should_connect, should_propagate = decide_cirtcuit(close_i, close_j)
        prev_j = circuit_labels[close_j][0]
        if should_connect:
            circuit_labels[close_i] = (label, True)
            circuit_labels[close_j] = (label, True)
        if should_propagate:
            for k in range(len(circuit_labels)):
                if circuit_labels[k][0] == prev_j:
                    circuit_labels[k] = (label, True)

    connections_made = 0
    iteration = 0
    while connections_made < max_connections:
        connect_closest(iteration)
        iteration += 1
        connections_made += 1

    circuit_sizes = {}
    for label, _ in circuit_labels:
        if label not in circuit_sizes:
            circuit_sizes[label] = 0
        circuit_sizes[label] += 1

    sizes = sorted([circuit_sizes[k] for k in circuit_sizes], reverse=True)
    res = 1
    for i in range(3):
        res *= sizes[i]

    return res


def part2(graph: tuple[list, dict]):
    l_nodes, w_edges, closest_pairs = graph
    circuit_labels = [(label, False) for label, _ in l_nodes]
    circuit_sizes = {label: 1 for label, _ in circuit_labels}

    def decide_cirtcuit(i: int, j: int) -> tuple[int, bool, bool]:
        circi, conni = circuit_labels[i]
        circj, connj = circuit_labels[j]
        if conni and connj:
            if circi == circj:
                return -1, False, False
            return circi, True, True
        elif conni:
            return circi, True, False
        elif connj:
            return circj, True, False
        else:
            return circi, True, False

    def connect_closest(iteration: int) -> tuple[bool, int, int]:
        close_i, close_j = closest_pairs[iteration]

        prev_i = circuit_labels[close_i][0]
        prev_j = circuit_labels[close_j][0]
        label, should_connect, should_propagate = decide_cirtcuit(close_i, close_j)
        if should_connect:
            circuit_labels[close_i] = (label, True)
            circuit_labels[close_j] = (label, True)
            circuit_sizes[label] += 2
            circuit_sizes[prev_i] -= 1
            circuit_sizes[prev_j] -= 1
        if should_propagate:
            circuit_sizes[label] += circuit_sizes[prev_j]
            circuit_sizes[prev_j] = 0
            for k in range(len(circuit_labels)):
                if circuit_labels[k][0] == prev_j:
                    circuit_labels[k] = (label, True)
        return (
            label >= 0 and circuit_sizes[label] >= len(l_nodes),
            close_i,
            close_j,
        )

    iteration = 0
    max_size_reached = False
    last_node_i = -1
    last_node_j = -1
    while iteration < len(w_edges):
        max_size_reached, last_node_i, last_node_j = connect_closest(iteration)
        iteration += 1
        if max_size_reached:
            break

    pos_i = l_nodes[last_node_i][1]
    pos_j = l_nodes[last_node_j][1]
    return pos_i[0] * pos_j[0]


parsed = parse("input/day8.txt")
graph = make_graph(parsed)
p1 = part1(graph, 1000)
p2 = part2(graph)

print("Part 1:", p1)
print("Part 2:", p2)
