beam_indexes = set()
splits = 0
with open("manifold.txt") as f:
    for line in f.readlines():
        if 'S' in line:
            beam_indexes.add(line.index('S'))
        elif '^' in line:
            splitter_indices = [i for i, val in enumerate(line) if val == '^']
            for index in splitter_indices:
                if index in beam_indexes:
                    splits += 2
                    beam_indexes.remove(index)
                    beam_indexes.add(index - 1)
                    beam_indexes.add(index + 1)
        for index in beam_indexes:
            line = line[:index] + '|' + line[index + 1:]
        print(line, end='')
print(f"\nTotal splits: {splits}")