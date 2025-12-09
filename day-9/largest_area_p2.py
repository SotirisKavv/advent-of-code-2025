def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

with open("tiles.txt") as f:
    tiles = [tuple(map(int, line.strip().split(','))) for line in f if line.strip()]


edges = []
n = len(tiles)
for i in range(n):
    x1, y1 = tiles[i]
    x2, y2 = tiles[(i + 1) % n]
    edges.append((x1, y1, x2, y2))


xs = sorted(set(x for x, _ in tiles))
ys = sorted(set(y for _, y in tiles))

x_index = {x: i for i, x in enumerate(xs)}
y_index = {y: i for i, y in enumerate(ys)}

W = len(xs) - 1
H = len(ys) - 1

inside = [[False] * W for _ in range(H)]

vertical_edges = []
for x1, y1, x2, y2 in edges:
    if x1 == x2 and y1 != y2:
        y_lo, y_hi = sorted((y1, y2))
        vertical_edges.append((x1, y_lo, y_hi))

for j in range(H):
    y_mid = (ys[j] + ys[j+1]) / 2.0

    xs_cross = []
    for x, y_lo, y_hi in vertical_edges:
        if y_lo <= y_mid < y_hi:
            xs_cross.append(x)

    xs_cross.sort()

    k = 0
    while k + 1 < len(xs_cross):
        x_start = xs_cross[k]
        x_end   = xs_cross[k + 1]

        for i in range(W):
            if xs[i] >= x_start and xs[i+1] <= x_end:
                inside[j][i] = True

        k += 2

ps = [[0] * (W + 1) for _ in range(H + 1)]
for j in range(H):
    row_sum = 0
    for i in range(W):
        if inside[j][i]:
            row_sum += 1
        ps[j+1][i+1] = ps[j][i+1] + row_sum


def rect_sum(i0, j0, i1, j1):
    return ps[j1][i1] - ps[j0][i1] - ps[j1][i0] + ps[j0][i0]

max_area = 0
best_pair = None

for a in range(n):
    x1, y1 = tiles[a]
    for b in range(a + 1, n):
        x2, y2 = tiles[b]
        
        if x1 == x2 or y1 == y2:
            continue

        xmin, xmax = sorted((x1, x2))
        ymin, ymax = sorted((y1, y2))

        ix_min = x_index[xmin]
        ix_max = x_index[xmax]
        iy_min = y_index[ymin]
        iy_max = y_index[ymax]

        if ix_max == ix_min or iy_max == iy_min:
            continue

        total_cells   = (ix_max - ix_min) * (iy_max - iy_min)
        inside_cells  = rect_sum(ix_min, iy_min, ix_max, iy_max)

        if inside_cells == total_cells:
            a_val = area((x1, y1), (x2, y2))
            if a_val > max_area:
                max_area = a_val
                best_pair = ((x1, y1), (x2, y2))

print(f"Largest valid area: {max_area}, between points {best_pair[0]} and {best_pair[1]}")
