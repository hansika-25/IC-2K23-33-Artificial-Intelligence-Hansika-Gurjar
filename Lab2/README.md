
# Lab 2: Search Algorithms

**Student Name:** Hansika Gurjar  
**Roll Number:** IC-2K23-33  
**Course:** Artificial Intelligence  
**Year:** 4th Year  
**Semester:** 7  
**Section:** A  

## Aim

To implement and understand different search algorithms used in Artificial Intelligence and analyze their working, performance, and applications.

## Algorithms Implemented

1. Breadth-First Search (BFS)
2. Depth-First Search (DFS)
3. Hill Climbing
4. Best-First Search
5. A* Search

## 1. Breadth-First Search (BFS)

### Problem Statement
Find a path from a starting node to a goal node in an unweighted graph using Breadth-First Search.

### Algorithm
BFS explores nodes level by level using a queue. It finds the shortest path in terms of the number of edges in an unweighted graph.

### Sample Output

```text
Breadth-First Search
Start Node: A
Goal Node: H
Path: A -> B -> E -> H
Path Length: 3
```

### Complexity Analysis

- Time Complexity: O(V + E)
- Space Complexity: O(V)

Here, V is the number of vertices and E is the number of edges.

## 2. Depth-First Search (DFS)

### Problem Statement
Find a path from a starting node to a goal node by exploring one branch deeply before backtracking.

### Algorithm
DFS uses a stack to explore nodes. It continues along a branch until it cannot proceed further, then backtracks.

### Sample Output

```text
Depth-First Search
Start Node: A
Goal Node: H
Path: A -> C -> G -> H
Path Length: 3
```

### Complexity Analysis

- Time Complexity: O(V + E)
- Space Complexity: O(V)

## 3. Hill Climbing

### Problem Statement
Find the maximum value of a mathematical function using a heuristic-based search technique.

### Algorithm
Hill Climbing starts from an initial state and repeatedly moves to a neighboring state with a better heuristic value. It stops when no improvement is possible.

### Sample Output

```text
Hill Climbing Search
Best State: 5
Maximum Value: 25
```

### Complexity Analysis

- Time Complexity: O(k), where k is the number of steps taken
- Space Complexity: O(1)

Hill Climbing may get stuck at a local optimum and does not guarantee a global optimum in general.

## 4. Best-First Search

### Problem Statement
Find a path from a starting node to a goal node using heuristic information.

### Algorithm
Best-First Search uses a priority queue and selects the node with the lowest heuristic value first.

### Sample Output

```text
Best-First Search
Path: A -> C -> G -> H
Path Length: 3
```

### Complexity Analysis

- Time Complexity: O((V + E) log V) with a priority queue, under standard graph-search assumptions
- Space Complexity: O(V)

Best-First Search does not guarantee the shortest path.

## 5. A* Search

### Problem Statement
Find a minimum-cost path from a starting node to a goal node using actual path cost and heuristic estimates.

### Algorithm

A* evaluates each node using:

f(n) = g(n) + h(n)

Where:

- g(n): Actual cost from the start node to node n
- h(n): Estimated cost from node n to the goal
- f(n): Estimated total path cost

### Sample Output

```text
A* Search
Path: A -> B -> E -> H
Total Cost: 8
```

### Complexity Analysis

- Time Complexity: Exponential in the worst case, depending on the heuristic
- Space Complexity: Exponential in the worst case

A* can find an optimal path when the heuristic is admissible and the implementation handles node costs correctly.

## Learning Outcomes

- Understood uninformed and informed search strategies.
- Implemented BFS and DFS for graph traversal.
- Learned how heuristic functions guide search algorithms.
- Understood the role of priority queues in Best-First Search and A*.
- Compared algorithms based on path selection and complexity.
- Learned that heuristic quality affects search efficiency and optimality.

## Source Code

The Python implementation of all five algorithms is available in:

`SearchAlgorithms.py`
