from collections import deque
import re

def umarshal_schematics(line: str):
    lights = re.findall(r'\[(.*?)\]', line)
    light_bin = tuple(light == '#' for light in lights[0])

    b_wirings_list = re.findall(r'\((.*?)\)', line)
    b_wirings = [tuple(map(int, wiring.split(','))) for wiring in b_wirings_list]

    joltage_reqs_list = re.findall(r'{(.*?)}', line)
    joltage_reqs = [int(req) for req in joltage_reqs_list[0].split(',')]

    return light_bin, b_wirings, joltage_reqs

def apply_button(lights, buttons):
    lists_lights = list(lights)
    for button in buttons:
        lists_lights[button] = not lists_lights[button]

    return tuple(lists_lights)

def shortest_sequence(init_state, goal, actions):
    visited = set()
    queue = deque([(init_state, 0)])

    while queue:
        current_state, depth = queue.popleft()
        if current_state == goal:
            return depth
        for wiring in actions:
            new_state = apply_button(current_state, wiring)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, depth + 1))
    return -1

total_min_steps = 0
with open("schematics.txt") as f:
    for line in f.readlines():
        lights, b_wirings, _ = umarshal_schematics(line.strip())
        init_lights = tuple([False] * len(lights))
        steps = shortest_sequence(init_lights, lights, b_wirings)
        total_min_steps += steps
        print(f"Minimum steps for configuration {lights}: {steps}")
print(f"Total minimum steps to achieve all light configurations: {total_min_steps}")