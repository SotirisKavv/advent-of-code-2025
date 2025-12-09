# 🎄 Day 4: Printing Department

## Part 1

### Story
You ride the escalator down to the printing department. They're clearly getting ready for Christmas with lots of large rolls of paper everywhere and even a massive printer in the corner.

Decorating here will be easy—they can make their own decorations! But you need a way to get further into the North Pole base while the elevators are offline.

"We're pretty sure there's a cafeteria on the other side of the back wall," an Elf explains. "If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."

### The Challenge
If you can **optimize the forklift work**, they'd have time to break through the wall!

### The Grid
Rolls of paper (`@`) are arranged on a large grid:

```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

### Accessibility Rule
A forklift can access a roll of paper **only if** there are **fewer than 4 rolls** in the **8 adjacent positions**.

```
Adjacent positions:
  ███
  █@█
  ███
```

### Example Solution
Accessible rolls (marked with `x`):

```
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
```

**Total accessible rolls:** `13`

### ⭐ Answer: **1578**

---

## Part 2

### New Challenge
Now the Elves need help accessing **as much paper as possible**!

### The Process
1. **Access** rolls with < 4 neighbors
2. **Remove** those rolls
3. **Repeat** - more rolls may become accessible after removal
4. **Stop** when no more rolls can be accessed

### Example Walkthrough

**Initial state:** 100 total rolls
```
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
```

**Wave 1:** Remove 13 rolls
```
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
```

**Wave 2:** Remove 12 rolls
```
.......x..
.@@.x.x.@x
x@@@@...@@
x.@@@@..x.
.@.@@@@.x.
.x@@@@@@.x
.x.@.@.@@@
..@@@.@@@@
.x@@@@@@@.
....@@@...
```

**Wave 3:** Remove 7 rolls
```
..........
.x@.....x.
.@@@@...xx
..@@@@....
.x.@@@@...
..@@@@@@..
...@.@.@@x
..@@@.@@@@
..x@@@@@@.
....@@@...
```

**Wave 4:** Remove 5 rolls
**Wave 5:** Remove 2 rolls
**Wave 6:** Remove 1 roll
**Wave 7:** Remove 1 roll
**Wave 8:** Remove 1 roll
**Wave 9:** Remove 1 roll

**Final state:** All accessible rolls removed
```
..........
..........
..........
...x@@....
...@@@@...
...@@@@@..
...@.@.@@.
...@@.@@@.
...@@@@@..
....@@@...
```

**Total removed:** `13 + 12 + 7 + 5 + 2 + 1 + 1 + 1 + 1 = 43`

### ⭐ Answer: **10132**