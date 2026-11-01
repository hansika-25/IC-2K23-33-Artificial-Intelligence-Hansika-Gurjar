
# Lab 1 – Water Jug Problem

## 1. Aim / Problem Statement

### Aim

To implement the Water Jug Problem in Python using a state-transition approach and determine a sequence of operations to measure an exact target quantity of water.

### Problem Statement

Two water jugs have capacities of 4 litres and 9 litres. Initially, both jugs are empty. The objective is to measure exactly 6 litres using the following operations:

1. Fill a jug completely.
2. Empty a jug completely.
3. Pour water from one jug into another until the source jug is empty or the destination jug is full.

**Input:**
- First Jug Capacity = 4 L
- Second Jug Capacity = 9 L
- Target = 6 L

## 2. Algorithm

### State Representation

A state is represented as `(a, b)` where:

- `a` is the quantity of water in the first jug.
- `b` is the quantity of water in the second jug.

Initial state: `(0, 0)`

Goal state: Any state where `a = 6` or `b = 6`.

### Algorithm Steps

1. Initialize both jugs to zero.
2. Check whether the target is achievable using the jug capacities.
3. If the first jug is empty, fill it.
4. If the second jug is full, empty it.
5. Otherwise, pour water from the first jug into the second jug.
6. Display the operation and the resulting state.
7. Repeat until the target amount is reached.

### Pseudocode

```text
START

Set first_capacity = 4
Set second_capacity = 9
Set target = 6

Set first_jug = 0
Set second_jug = 0

WHILE first_jug != target AND second_jug != target:

    IF first_jug is empty:
        Fill first jug

    ELSE IF second_jug is full:
        Empty second jug

    ELSE:
        Pour water from first jug into second jug
        until source is empty or destination is full

    Display operation
    Display current state

Display "Target reached"

END
```

## 3. Implementation

The program is implemented in Python using functions for input validation and solving the Water Jug Problem.

Source file: `Task1_Water-Jug-Problem.py`

## 4. Results / Output

### Console Output

```text
Initial State: (0, 0)

Fill 4L jug
State: (4, 0)

Pour 4L from first jug into second jug
State: (0, 4)

Fill 4L jug
State: (4, 4)

Pour 4L from first jug into second jug
State: (0, 8)

Fill 4L jug
State: (4, 8)

Pour 1L from first jug into second jug
State: (3, 9)

Empty 9L jug
State: (3, 0)

Pour 3L from first jug into second jug
State: (0, 3)

Fill 4L jug
State: (4, 3)

Pour 4L from first jug into second jug
State: (0, 7)

Fill 4L jug
State: (4, 7)

Pour 2L from first jug into second jug
State: (2, 9)

Empty 9L jug
State: (2, 0)

Pour 2L from first jug into second jug
State: (0, 2)

Fill 4L jug
State: (4, 2)

Pour 4L from first jug into second jug
State: (0, 6)

Target reached! Final State: (0, 6)
```

### Result

The Water Jug Problem was successfully solved. The algorithm measured exactly 6 litres of water in the second jug.

Final state: `(0, 6)`

## 5. Performance Analysis

| Metric | Result |
|---|---|
| Target Achieved | Yes |
| Number of Operations | 15 |
| Time Complexity | O(X × Y) upper bound for the number of distinct states |
| Auxiliary Space Complexity | O(X × Y) due to the visited-state set |
| Accuracy / Precision / Recall / F1-score | Not applicable |

Here, `X` and `Y` represent the capacities of the two jugs.

The problem is deterministic and does not involve classification or prediction. Therefore, classification metrics are not applicable.

The visited-state set stores previously encountered states to prevent repeated processing.

## 6. State Visualization

```text
(0,0)
  ↓
(4,0)
  ↓
(0,4)
  ↓
(4,4)
  ↓
(0,8)
  ↓
(4,8)
  ↓
(3,9)
  ↓
(3,0)
  ↓
(0,3)
  ↓
(4,3)
  ↓
(0,7)
  ↓
(4,7)
  ↓
(2,9)
  ↓
(2,0)
  ↓
(0,2)
  ↓
(4,2)
  ↓
(0,6)
```

## 7. Learning Outcomes

- Understood problem formulation in Artificial Intelligence.
- Learned to represent a problem using states.
- Implemented state transitions using Python.
- Applied fill, empty, and pour operations.
- Understood the role of validation and visited-state tracking.
- Analyzed the time and space complexity of a state-based problem.
