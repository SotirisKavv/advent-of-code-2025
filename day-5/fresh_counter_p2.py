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


with open("inventory_ids.txt") as f:
    for line in f.readlines():
        if '-' in line:
            start, end = line.strip().split('-')
            id_ranges.append((int(start), int(end)))
        else:
            pass

id_ranges= merge_ranges(id_ranges)
for range in id_ranges:
    total_fresh += range[1] - range[0] + 1
    
  
print(f"Total fresh inventory IDs: {total_fresh}") 
            
            
