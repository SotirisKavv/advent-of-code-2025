with open("instructions.txt", 'r') as file:
    lines = file.readlines()

index = 50
zero_passed = 0

for line in lines:
    last_index = index
    if line.strip()[0] == 'R':
        index += int(line.strip()[1:])
    elif line.strip()[0] == 'L':
        index -= int(line.strip()[1:])
    index %= 100
    zero_passed += index == 0
    
    
print(f"Total times passed zero: {zero_passed}")