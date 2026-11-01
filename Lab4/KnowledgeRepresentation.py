# Lab 4: Knowledge Representation and Rule-Based System

# Facts
facts = {
    "has_feathers": True,
    "can_fly": True,
    "lays_eggs": True
}

# Knowledge base: rules
rules = {
    "bird": ["has_feathers", "lays_eggs"],
    "flying_bird": ["bird", "can_fly"]
}

# Inference function
def infer(facts, rules):
    inferred = set()

    # Apply rules to infer new knowledge
    for conclusion, conditions in rules.items():
        if all(
            facts.get(condition, False) or condition in inferred
            for condition in conditions
        ):
            inferred.add(conclusion)

    return inferred


# Display facts
print("Initial Facts:")
for fact, value in facts.items():
    print(f"{fact}: {value}")

# Perform inference
results = infer(facts, rules)

# Display inferred knowledge
print("\nInferred Knowledge:")
for result in results:
    print(result)