with open("joltages.txt") as f:
    lines = f.readlines()

def find_largest_by_removal(line):
    digits = line.strip()
    k = len(digits) - 12
    
    stack = []
    for _, digit in enumerate(digits):
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    while k > 0:
        stack.pop()
        k -= 1
    
    return int(''.join(stack))

total_joltage = 0
for line in lines:
    joltage = find_largest_by_removal(line)
    print(f"Line: {line.strip()} -> Largest 12-digit: {joltage}")
    total_joltage += joltage
 
print(f"\nTotal joltage: {total_joltage}")