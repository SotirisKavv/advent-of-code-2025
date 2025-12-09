with open("math.txt") as f:
    lines = f.readlines()
    grid = [list(line.rstrip("\n")) for line in lines]

for row in grid:
    row.insert(0, " ")

total = 0
column_vals = []
operation = ""
for col_index in range(len(grid[0])-1, -1, -1):
    digits = []
    
    if grid[-1][col_index] in "+*":
        operation = grid[-1][col_index]
    
    for row in grid[:-1]:
        digits.append(row[col_index])
    
    if all(d == " " for d in digits):
        if operation == "+":
            partial = sum(column_vals)
        elif operation == "*":
            partial = 1
            for val in column_vals:
                partial *= val
        print(f"Column {col_index}: operation {operation} on values {column_vals} gives {partial}")
        total += partial
        column_vals = []
        operation = ""
    else:
        value = int(''.join(digits).strip())
        print(f"Column {col_index}: extracted value {value}")
        column_vals.append(value)

print(f"Total after operations: {total}")