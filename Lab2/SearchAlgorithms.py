from collections import deque
import heapq

def bfs(graph, start, goal):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(path + [neighbor])

    return None


def main():
    graph = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": [],
        "E": ["H"],
        "F": [],
        "G": ["H"],
        "H": []
    }

    start = "A"
    goal = "H"

    path = bfs(graph, start, goal)

    if path:
        print("Breadth-First Search")
        print("Start Node:", start)
        print("Goal Node:", goal)
        print("Path:", " -> ".join(path))
        print("Path Length:", len(path) - 1)
    else:
        print("Goal not reachable from the start node.")

def dfs(graph, start, goal):
    visited = set()
    stack = [[start]]

    while stack:
        path = stack.pop()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(path + [neighbor])

    return None
if __name__ == "__main__":
    main()
def hill_climbing():
    def heuristic(x):
        return -(x - 5) ** 2 + 25

    current = 0

    while True:
        neighbors = [current - 1, current + 1]

        best_neighbor = max(neighbors, key=heuristic)

        if heuristic(best_neighbor) <= heuristic(current):
            break

        current = best_neighbor

    return current, heuristic(current)


result, value = hill_climbing()

print("Hill Climbing Search")
print("Best State:", result)
print("Maximum Value:", value)




def best_first_search(graph, heuristic, start, goal):
    priority_queue = [(heuristic[start], start, [start])]
    visited = set()

    while priority_queue:
        _, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    heapq.heappush(
                        priority_queue,
                        (heuristic[neighbor], neighbor, path + [neighbor])
                    )

    return None


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": ["H"],
    "F": [],
    "G": ["H"],
    "H": []
}

heuristic = {
    "A": 7,
    "B": 6,
    "C": 4,
    "D": 5,
    "E": 2,
    "F": 3,
    "G": 1,
    "H": 0
}

path = best_first_search(graph, heuristic, "A", "H")

if path:
    print("Best-First Search")
    print("Path:", " -> ".join(path))
    print("Path Length:", len(path) - 1)
else:
    print("Goal not reachable.")

def a_star_search(graph, heuristic, start, goal):
    priority_queue = [(heuristic[start], 0, start, [start])]
    visited = set()

    while priority_queue:
        f_cost, g_cost, node, path = heapq.heappop(priority_queue)

        if node == goal:
            return path, g_cost

        if node in visited:
            continue

        visited.add(node)

        for neighbor, cost in graph.get(node, []):
            if neighbor not in visited:
                new_g_cost = g_cost + cost
                new_f_cost = new_g_cost + heuristic[neighbor]

                heapq.heappush(
                    priority_queue,
                    (
                        new_f_cost,
                        new_g_cost,
                        neighbor,
                        path + [neighbor]
                    )
                )

    return None, float("inf")


# Weighted graph: each edge stores (neighbor, cost)
weighted_graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2), ("E", 5)],
    "C": [("F", 3), ("G", 6)],
    "D": [],
    "E": [("H", 2)],
    "F": [],
    "G": [("H", 1)],
    "H": []
}

heuristic = {
    "A": 6,
    "B": 5,
    "C": 4,
    "D": 3,
    "E": 2,
    "F": 3,
    "G": 1,
    "H": 0
}

path, cost = a_star_search(
    weighted_graph,
    heuristic,
    "A",
    "H"
)

print("\nA* Search")

if path:
    print("Path:", " -> ".join(path))
    print("Total Cost:", cost)
else:
    print("Goal not reachable.")