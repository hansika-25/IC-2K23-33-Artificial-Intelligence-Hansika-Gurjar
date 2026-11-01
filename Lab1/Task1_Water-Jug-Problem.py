
from math import gcd


def validate_input(first_capacity, second_capacity, target):
    """Validate the capacities and target amount."""
    if not all(isinstance(value, int) for value in
               (first_capacity, second_capacity, target)):
        raise TypeError("Capacities and target must be integers.")

    if first_capacity <= 0 or second_capacity <= 0:
        raise ValueError("Jug capacities must be positive.")

    if target < 0:
        raise ValueError("Target cannot be negative.")

    if target > max(first_capacity, second_capacity):
        raise ValueError("Target cannot exceed the largest jug capacity.")

    if target != 0 and target % gcd(first_capacity, second_capacity) != 0:
        raise ValueError("The target cannot be measured with these jugs.")


def water_jug(first_capacity, second_capacity, target):
    """
    Solve the Water Jug Problem using a state-transition approach.

    State: (amount in first jug, amount in second jug)
    """
    first_jug = 0
    second_jug = 0
    visited_states = set()

    print(f"Initial State: ({first_jug}, {second_jug})\n")

    while first_jug != target and second_jug != target:
        current_state = (first_jug, second_jug)

        if current_state in visited_states:
            print("No new state found. Stopping.")
            return

        visited_states.add(current_state)

        if first_jug == 0:
            first_jug = first_capacity
            operation = f"Fill {first_capacity}L jug"

        elif second_jug == second_capacity:
            second_jug = 0
            operation = f"Empty {second_capacity}L jug"

        else:
            transferred = min(
                first_jug,
                second_capacity - second_jug
            )

            first_jug -= transferred
            second_jug += transferred

            operation = (
                f"Pour {transferred}L from first jug "
                f"into second jug"
            )

        print(operation)
        print(f"State: ({first_jug}, {second_jug})\n")

    print(f"Target reached! Final State: ({first_jug}, {second_jug})")


def main():
    """Run the Water Jug Problem."""
    first_capacity = 4
    second_capacity = 9
    target = 6

    try:
        validate_input(first_capacity, second_capacity, target)
        water_jug(first_capacity, second_capacity, target)

    except (TypeError, ValueError) as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
