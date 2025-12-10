# 🎄 Day 10: Factory

## Part 1

### Story
Just across the hall, you find a large factory. Fortunately, the Elves here have plenty of time to decorate. Unfortunately, it's because the factory machines are all offline, and none of the Elves can figure out the initialization procedure. The section of the manual with the procedure is missing; all that remains are indicator light diagrams, button wiring schematics, and joltage requirements.

### Input Format
Each line describes one machine and contains:
- An indicator light diagram in square brackets `[...]`.
- One or more button wiring schematics in parentheses, e.g. `(0,3,4)`.
- Joltage requirements in curly braces `{...}` (ignore for Part 1).

Example lines:
```
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
```

### Rules
- Lights start all OFF; `.` means OFF and `#` means ON in the target diagram.
- Pressing a button toggles each listed light index (0-based).
- Find the fewest total button presses needed to match the diagram.

### Example
Across the three examples above, the fewest total presses are `2 + 3 + 2 = 7`.

### ⭐ Answer: **425**

---

## Part 2

### Story
All of the machines are starting to come online! Now, it's time to worry about the joltage requirements. Ignore the light diagrams and use the same button wirings, but in this mode each press increments the listed counters by 1.

### Input Format
Same as Part 1, but the goal is the joltage requirements in `{...}`. Counters start at 0.

### Rules
- Pressing a button increases each listed counter by 1.
- Find the fewest total button presses to exactly reach the target counters.

### Example
For the three example machines above, the minimal presses are `10 + 12 + 11 = 33`.

### ⭐ Answer: **15883**