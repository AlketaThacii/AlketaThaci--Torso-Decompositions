from itertools import combinations
from random import Random


def minimum_fill(adjacency, seed=42, candidate_limit=8):
    
    graph = [set(neighbors) for neighbors in adjacency]
    remaining = set(range(len(graph)))
    order = []
    rng = Random(seed)

    while remaining:
        degrees = {
            node: len(graph[node] & remaining)
            for node in remaining
        }
        if min(degrees.values()) > 500:
               order.extend(sorted(remaining))
               break


        candidates = sorted(
            remaining,
            key=lambda node: (degrees[node], node)
        )[:candidate_limit]

        best_fill = None
        best_candidates = []

        for node in candidates:
            neighbors = sorted(graph[node] & remaining)

            missing_edges = sum(
                1
                for left, right in combinations(neighbors, 2)
                if right not in graph[left]
            )

            if best_fill is None or missing_edges < best_fill:
                best_fill = missing_edges
                best_candidates = [node]
            elif missing_edges == best_fill:
                best_candidates.append(node)

        node = rng.choice(best_candidates)
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

def minimum_degree(adjacency):
    graph = [set(neighbors) for neighbors in adjacency]
    remaining = set(range(len(graph)))
    order = []

    while remaining:
        degrees = {
            current: len(graph[current] & remaining)
            for current in remaining
        }

        if min(degrees.values()) > 500:
            order.extend(sorted(remaining))
            break

        node = min(
            remaining,
            key=lambda current: (degrees[current], current)
        )

        neighbors = list(graph[node] & remaining)

        for i in range(len(neighbors)):
            for j in range(i + 1, len(neighbors)):
                left = neighbors[i]
                right = neighbors[j]
                graph[left].add(right)
                graph[right].add(left)

        for neighbor in neighbors:
            graph[neighbor].discard(node)

        graph[node].clear()
        remaining.remove(node)
        order.append(node)

    return order