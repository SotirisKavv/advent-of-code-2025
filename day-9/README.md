# 🎄 Day 9: Movie Theater

## Part 1

### Story
You slide down the firepole in the corner of the playground and land in the **North Pole base movie theater**! 🎬

The theater has a **big tile floor** with an interesting pattern. Elves are redecorating by switching out square tiles. Some tiles are **red**, and the Elves want to find the **largest rectangle** using **red tiles** for **two opposite corners**.

### Input Format
List of red tile coordinates (`X,Y`):

```
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
```

### Visual Representation
Red tiles as `#`, other tiles as `.`:

```
..............
.......#...#..
..............
..#....#......
..............
..#......#....
..............
.........#.#..
..............
```

### The Challenge
Choose any **two red tiles** as opposite corners and find the **largest possible rectangle**.

### Example Rectangles

**Rectangle 1:** Area = 24 (between `2,5` and `9,7`)
```
..............
.......#...#..
..............
..#....#......
..............
..OOOOOOOO....
..OOOOOOOO....
..OOOOOOOO.#..
..............
```

**Rectangle 2:** Area = 35 (between `7,1` and `11,7`)
```
..............
.......OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
..#....OOOOO..
.......OOOOO..
.......OOOOO..
..............
```

**Rectangle 3:** Area = 6 (between `7,3` and `2,3`)
```
..............
.......#...#..
..............
..OOOOOO......
..............
..#......#....
..............
.........#.#..
..............
```

### Largest Rectangle
**Area = 50** (between `2,5` and `11,1`)

```
..............
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..OOOOOOOOOO..
..............
.........#.#..
..............
```

**Calculation:**
- Width: `11 - 2 + 1 = 10`
- Height: `5 - 1 + 1 = 5`
- Area: `10 × 5 = 50`

### ⭐ Answer: **4744899849**

---

## Part 2

### New Constraint! 🟢
The Elves just remembered: they can **only switch out tiles that are red or green**. Your rectangle can **only include red or green tiles**.

### Green Tile Rules
1. Each **consecutive pair** of red tiles in the list is connected by a **straight line of green tiles**
2. The list **wraps** (first red tile connects to last red tile)
3. Adjacent red tiles in the list are always on the **same row or column**
4. All tiles **inside the loop** of red/green tiles are also **green**

### Green Tiles Visualization

**Boundary green tiles** (marked `X`):
```
..............
.......#XXX#..
.......X...X..
..#XXXX#...X..
..X........X..
..#XXXXXX#.X..
.........X.X..
.........#X#..
..............
```

**All green tiles** (boundary + interior):
```
..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
```

### Updated Challenge
Rectangle **must have red corners** but can **only include red or green tiles** (significantly limiting options).

### Example Rectangles

**Option 1:** Area = 15 (between `7,3` and `11,1`)
```
..............
.......OOOOO..
.......OOOOO..
..#XXXXOOOOO..
..XXXXXXXXXX..
..#XXXXXX#XX..
.........XXX..
.........#X#..
..............
```

**Option 2:** Area = 3 (between `9,7` and `9,5`)
```
..............
.......#XXX#..
.......XXXXX..
..#XXXX#XXXX..
..XXXXXXXXXX..
..#XXXXXXOXX..
.........OXX..
.........OX#..
..............
```

### Largest Valid Rectangle
**Area = 24** (between `9,5` and `2,3`)

```
..............
.......#XXX#..
.......XXXXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
..OOOOOOOOXX..
.........XXX..
.........#X#..
..............
```

### Strategy
1. Build the **polygon** from red tiles (edges between consecutive tiles)
2. Find all **green tiles** using **point-in-polygon** detection
3. Check each red tile pair: rectangle valid only if **all interior points are red or green**

### ⭐ Answer: **1540192500**