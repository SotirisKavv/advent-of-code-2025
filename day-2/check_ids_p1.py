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
        if len(string_id) % 2 == 0:
            mid_index = len(string_id) // 2
            first_half = string_id[:mid_index]
            second_half = string_id[mid_index:]
            if first_half == second_half:
                invalid_ids_sum += item_id

print(invalid_ids_sum)
        