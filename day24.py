import numpy as np

# 1. Define MDP Components
states = ["A", "B", "C", "D"]  # 4 states
actions = ["left", "right"]

# Transition probabilities and rewards
# P[s][a] = [(prob, next_state, reward, done)]
P = {
    "A": {
        "right": [(1.0, "B", 0, False)],
        "left": [(1.0, "A", 0, False)]
    },
    "B": {
        "right": [(1.0, "C", 0, False)],
        "left": [(1.0, "A", 0, False)]
    },
    "C": {
        "right": [(1.0, "D", 1, True)],   # Reaching D gives reward +1
        "left": [(1.0, "B", 0, False)]
    },
    "D": {
        "right": [(1.0, "D", 0, True)],
        "left": [(1.0, "D", 0, True)]
    }
}

# 2. Initialize parameters
gamma = 0.9  # discount factor
theta = 1e-4  # convergence threshold
V = {s: 0 for s in states}  # initial value function

# 3. Value Iteration Algorithm
iteration = 0
while True:
    delta = 0
    iteration += 1
    print(f"\nIteration {iteration}")

    for s in states:
        v = V[s]
        action_values = []

        for a in actions:
            val = 0
            for prob, next_state, reward, done in P[s][a]:
                val += prob * (reward + gamma * V[next_state])
            action_values.append(val)

        V[s] = max(action_values)
        delta = max(delta, abs(v - V[s]))
        print(f"State {s}: Value = {V[s]:.4f}")

    if delta < theta:
        break

# 4. Derive the Optimal Policy
policy = {}
for s in states:
    best_action = None
    best_value = float('-inf')
    for a in actions:
        val = sum([prob * (reward + gamma * V[next_state]) for prob, next_state, reward, done in P[s][a]])
        if val > best_value:
            best_value = val
            best_action = a
    policy[s] = best_action

# 5. Display Results
print("\nFinal Value Function:")
for s in V:
    print(f"{s}: {V[s]:.4f}")

print("\nOptimal Policy:")
for s in policy:
    print(f"{s}: {policy[s]}")

     