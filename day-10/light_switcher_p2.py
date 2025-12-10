import pulp
import re

def umarshal_schematics(line: str):
    lights = re.findall(r'\[(.*?)\]', line)
    light_bin = tuple(light == '#' for light in lights[0])

    b_wirings_list = re.findall(r'\((.*?)\)', line)
    b_wirings = [tuple(map(int, wiring.split(','))) for wiring in b_wirings_list]

    joltage_reqs_list = re.findall(r'{(.*?)}', line)
    joltage_reqs = tuple(int(req) for req in joltage_reqs_list[0].split(','))

    return light_bin, b_wirings, joltage_reqs

# ILP to find the shortest sequence
def shortest_sequence(init_state, goal, actions):
    n = len(goal)
    covered = set(idx for wiring in actions for idx in wiring)
    for i, g in enumerate(goal):
        if g > 0 and i not in covered:
            return -1

    action_vectors = []
    for wiring in actions:
        vec = [0] * n
        for idx in wiring:
            vec[idx] += 1
        action_vectors.append(vec)

    costs = [1.0] * len(action_vectors)
    prob = pulp.LpProblem("Minimize_Button_Presses", pulp.LpMinimize)

    x = [pulp.LpVariable(f'x{i}', lowBound=0, cat='Integer') for i in range(len(action_vectors))]

    prob += pulp.lpSum(costs[i] * x[i] for i in range(len(action_vectors)))

    for i in range(n):
        lhs = init_state[i] + pulp.lpSum(action_vectors[j][i] * x[j] for j in range(len(action_vectors)))
        prob += (lhs == goal[i]), f"Constraint_Light_{i}"

    prob.solve(pulp.PULP_CBC_CMD(msg=False))

    if prob.status != pulp.LpStatusOptimal:
        return -1

    action_counts = [int(pulp.value(x[k])) for k in range(len(action_vectors))]

    return sum(action_counts)

total_min_steps = 0
with open("schematics.txt") as f:
    for line in f.readlines():
        _, b_wirings, joltage_reqs = umarshal_schematics(line.strip())
        init_lights = tuple([0] * len(joltage_reqs))
        steps = shortest_sequence(init_lights, joltage_reqs, b_wirings)
        total_min_steps += steps
        print(f"Minimum steps for configuration {joltage_reqs}: {steps}")
print(f"Total minimum steps to achieve all light configurations: {total_min_steps}")