from collections import deque

connections = {}

with open("devices.txt") as f:
    for line in f.readlines():
        parts = line.strip().split(": ")
        connections[parts[0]] = parts[1].split(" ")

def bfs_paths_counter(start, goal):
    queue = deque([start])
    total_paths = 0

    while queue:
        current_device = queue.popleft()
        if current_device == goal:
            total_paths += 1
        for neighbor in connections.get(current_device, []):
            queue.append(neighbor)
    return total_paths

total_paths_count = bfs_paths_counter("you", "out")
print(f"Total distinct paths from you to out: {total_paths_count}")