map = []
    
with open("map.txt") as f:
    for line in f:
        row = list(line.strip())
        map.append(row)
        
# for row in map:
#     print(row)

def pad_map(map):
    width = len(map[0])
    empty_row = ["."] * (width + 2)
    new_map = [empty_row]
    
    for row in map:
        new_row = ["."] + row + ["."]
        new_map.append(new_row)
    
    new_map.append(empty_row)
    return new_map

def is_accessible(x, y, map):
    neighbors = (map[y+1][x-1] == "@") + (map[y+1][x] == "@") + (map[y+1][x+1] == "@") +\
                (map[y][x-1] == "@") + (map[y][x+1] == "@") +\
                (map[y-1][x-1] == "@") + (map[y-1][x] == "@") + (map[y-1][x+1] == "@")
    
    return neighbors < 4

padded_map = pad_map(map)
total_accessible = 0
for y in range(1, len(padded_map)-1):
    for x in range(1, len(padded_map[0])-1):
        total_accessible += (padded_map[y][x] == "@" and is_accessible(x, y, padded_map))
  
print(f"Total accessible rolls: {total_accessible}")