def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

with open("test_tiles.txt") as f:
    tiles = [tuple(map(int, line.strip().split(','))) for line in f.readlines()]

sorted_x = sorted(tiles, key=lambda t: t[0])
sorted_y = sorted(tiles, key=lambda t: t[1])

map = [['.' if (x, y) not in tiles else '#' for x in range(sorted_x[-1][0]+2)] for y in range(sorted_y[-1][1]+2) ]
for row in map:
    print(''.join(row))

max_area = 0
pair = None
for i in range(len(tiles)):
    for j in range(len(tiles)):
        if i != j:
            a = area(tiles[i], tiles[j])
            if a > max_area:
                pair = (tiles[i], tiles[j])
                max_area = a
print(f"Largest area: {max_area}, between points {pair[0]} and {pair[1]}")

for y in range(min(pair[0][1], pair[1][1]), max(pair[0][1], pair[1][1])+1):
    for x in range(min(pair[0][0], pair[1][0]), max(pair[0][0], pair[1][0])+1):
        map[y][x] = 'O'

for row in map:
    print(''.join(row))
