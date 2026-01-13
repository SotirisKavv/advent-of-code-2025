with open("input.txt") as f:
    lines = [line.rstrip('\n') for line in f.readlines()]
    
shapes = {}
containers = []

i = 0
while i < len(lines):
    line = lines[i]
    if line and ':' in line and line.split(':')[0].strip().isdigit():
        shape_num = int(line.split(':')[0])
        present_area = 0
        for j in range(1, 4):
            present_area += lines[i + j].count('#')
        shapes[shape_num] = present_area
        i += 3
    elif 'x' in line and ':' in line:
        parts = line.split(':')
        dims = parts[0].split('x')
        width = int(dims[0])
        height = int(dims[1])
        numbers = [int(x) for x in parts[1].strip().split()]
        containers.append((width, height, numbers))
        i += 1
    else:
        i += 1
        
print(f"Parsed shapes: {shapes}")
   
def fits(container):
    width, height, numbers = container
    blocks_in_container = (width // 3) * (height // 3)
    
    print(f"Checking container {container}: blocks_in_container={blocks_in_container}")
    # check if we have enough blocks to fill the container
    if blocks_in_container >= sum(numbers):
        return True
    
    # check if we have enough area to fit all presents
    total_present = sum(numbers[i-1] * shapes[i] for i in range(1, 6))
    print(f"Total present area needed: {total_present}, container area: {width * height}")
    if total_present > width * height:
        return False
    return None

total_fits = 0
for container in containers:
    if fits(container):
        total_fits += 1
        
print(f"Total containers that can fit presents: {total_fits}")