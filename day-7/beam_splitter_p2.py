with open("manifold.txt") as f:
    manifold = f.readlines()


def count_traversals(manifold):    
    outcomes = [[0 for _ in range(len(manifold[0].strip()))] for _ in range(len(manifold))]
    
    for y in range(len(manifold)):
        for x in range(len(manifold[y].strip())):
            char = manifold[y][x]
            if char == 'S':
                outcomes[y][x] = 1
            elif char == '^':
                if x > 0:
                    outcomes[y][x - 1] += outcomes[y - 1][x]
                if x < len(manifold[0].strip()) - 1:
                    outcomes[y][x + 1] += outcomes[y - 1][x]
            else:
                outcomes[y][x] += outcomes[y - 1][x]
        
    return sum(outcomes[-1])
total_paths = count_traversals(manifold)
print(f"Total beam paths through the manifold: {total_paths}")
    
