ids = []
id_ranges = []
total_fresh = 0

def merge_ranges(ranges):
    if not ranges:
        return []
    
    ranges.sort(key=lambda r: (r[0], r[1]))
    merged = [ranges[0]]
    
    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]
        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    
    return [tuple(r) for r in merged]
    
def is_fresh(ranges, id):
    if not ranges:
        return False
    left, right = 0, len(ranges) - 1
    while left <= right:
        mid = (left + right) // 2
        start, end = ranges[mid]
        if start <= id <= end:
            return True
        elif id < start:
            right = mid -1
        else:
            left = mid + 1
    return False

with open("inventory_ids.txt") as f:
    for line in f.readlines():
        if '-' in line:
            start, end = line.strip().split('-')
            id_ranges.append((int(start), int(end)))
        elif '' != line.strip():
            ids.append(int(line.strip()))

ids = sorted(ids)

id_ranges= merge_ranges(id_ranges)
for id in ids:
    if is_fresh(id_ranges, id):
        total_fresh += 1
  
print(f"Total fresh inventory IDs: {total_fresh}") 
            
            
