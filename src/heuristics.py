from itertools import combinations
from random import Random


def minimum_fill(adjacency, seed=42):

    graph = [set(neighbors) for neighbors in adjacency]
    remaining = set(range(len(graph)))
    order = []
    rng = Random(seed)

    while remaining:
        best_score = None
        candidates = []

        for node in remaining:
            neighbors = sorted(graph[node] & remaining)

            missing_edges = sum(
                1
                for left, right in combinations(neighbors, 2)
                if right not in graph[left]
            )

            score = (missing_edges, len(neighbors))

            if best_score is None or score < best_score:
                best_score = score
                candidates = [node]
            elif score == best_score:
                candidates.append(node)

        node = rng.choice(sorted(candidates))
        neighbors = list(graph[node] & remaining)

        for left, right in combinations(neighbors, 2):
            graph[left].add(right)
            graph[right].add(left)

        for neighbor in neighbors:
            graph[neighbor].discard(node)

        graph[node].clear()
        remaining.remove(node)
        order.append(node)

    return order