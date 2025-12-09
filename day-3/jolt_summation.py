with open("joltages.txt") as f:
    lines = f.readlines()

total_joltage = 0
for line in lines:
    joltages = list(line.strip())
    highest_index = joltages.index(max(joltages))
    if highest_index == len(joltages) - 1:
        second_highest_index = joltages.index(max(joltages[:-1]))
        bank_joltage = int(joltages[second_highest_index]+ joltages[highest_index])
    else:
        second_highest_index = joltages.index(max(joltages[highest_index+1:]))
        bank_joltage = int(joltages[highest_index] + joltages[second_highest_index])
    total_joltage += bank_joltage
 
print(f"Total joltage: {total_joltage}")   
    