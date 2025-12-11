from functools import lru_cache

connections = {}

with open("devices.txt") as f:
    for line in f.readlines():
        parts = line.strip().split(": ")
        connections[parts[0]] = parts[1].split(" ")

@lru_cache(maxsize=None)
def count_paths(start, goal):
    if start == goal:
        return 1
    return sum(count_paths(device, goal) for device in connections.get(start, []))

total_paths_fft_dac = (
    count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out")
)
total_paths_dac_fft = (
    count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out")
)
print(f"Total distinct paths from svr to out (via fft then dac): {total_paths_fft_dac}")
print(f"Total distinct paths from svr to out (via dac then fft): {total_paths_dac_fft}")
total_paths_count = total_paths_fft_dac + total_paths_dac_fft
print(f"Total distinct paths from svr to out: {total_paths_count}")