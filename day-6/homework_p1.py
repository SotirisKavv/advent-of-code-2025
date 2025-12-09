operations = {}

with open("math.txt") as f:
    for line in f.readlines():
        parts = line.strip().split()
        for i in range(len(parts)):
            if i not in operations:
                operations[i] = []
            operations[i].append(parts[i])

total = 0
for i in range(len(operations)):
    op = operations[i][-1]
    if op == "+":
        partial = sum(int(x) for x in operations[i][:-1])
    elif op == "*":
        partial = 1
        for x in operations[i][:-1]:
            partial *= int(x)
    total += partial
    
print(f"Total after operations: {total}")
