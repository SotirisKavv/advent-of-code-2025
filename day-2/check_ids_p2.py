import re

with open("id_ranges.txt") as f:
    line = f.readline().strip()

invalid_ids_sum = 0

id_ranges = line.split(",")
for id_range in id_ranges:
    start_str, end_str = id_range.split("-")
    start_id = int(start_str)
    end_id = int(end_str)
    
    for item_id in range(start_id, end_id + 1):
        string_id = str(item_id)
        for i in range(1, len(string_id)//2 + 1):
            if len(string_id) % i == 0 and re.fullmatch(r"({})+".format(string_id[:i]), string_id):
                print(f"Invalid ID found: {item_id} (repeats '{string_id[:i]}')")
                invalid_ids_sum += item_id
                break

print(invalid_ids_sum)
        