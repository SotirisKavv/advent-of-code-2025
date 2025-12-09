# 🎄 Day 8: Playground

## Part 1

### Story
Equipped with teleporter knowledge, you confidently step onto the **repaired teleporter pad**.

You rematerialize in a **vast underground space** containing a **giant playground**! 🎪

Across the playground, Elves are setting up an ambitious Christmas decoration: they've suspended many small **electrical junction boxes** and plan to connect them with **long strings of lights**.

### The Setup
- Most junction boxes **don't provide electricity**
- When two boxes are **connected** by lights, electricity can **pass between them**
- This creates **circuits** of connected boxes

### Input Format
Junction box positions in **3D space** (`X,Y,Z` coordinates):

```
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
```

### Strategy
Connect pairs of junction boxes **closest together** (by straight-line distance) to save on string lights.

### Example Walkthrough

**Connection 1:** Closest pair
- `162,817,812` ↔ `425,690,689`
- Creates: **1 circuit** with 2 boxes, **18 individual** circuits

**Connection 2:** Next closest (not already connected)
- `162,817,812` ↔ `431,825,988`
- Creates: **1 circuit** with 3 boxes, **17 individual** circuits

**Connection 3:** Next closest
- `906,360,560` ↔ `805,96,715`
- Creates: **1 circuit** with 3 boxes, **1 circuit** with 2 boxes, **15 individual** circuits

**Connection 4:** Already in same circuit!
- `431,825,988` ↔ `425,690,689`
- **No change** (already connected via `162,817,812`)

### After 10 Shortest Connections

| Circuit Size | Count |
|--------------|-------|
| 5 boxes | 2 |
| 2 boxes | 3 |
| 1 box | 7 |
| **Total circuits** | **11** |

**Calculation:** Multiply three largest circuit sizes
```
5 × 5 × 2 = 50
```

### Task
Connect the **1000 closest pairs** of junction boxes.

**Multiply the sizes of the three largest circuits.**

### ⭐ Answer: **135169**

---

## Part 2

### New Goal
The Elves don't have enough extension cables! Keep connecting junction boxes until **they're all in one large circuit**.

### The Question
Find the **last connection** that unifies all boxes into a single circuit.

Then multiply the **X coordinates** of those two junction boxes to determine how far they are from the wall (for picking the right extension cable).

### Example Solution

Continuing from Part 1, keep connecting closest pairs...

**Final connection** that creates a single circuit:
- `216,146,977` ↔ `117,168,530`

**Calculation:**
```
X coordinate of first box:  216
X coordinate of second box: 117
Product: 216 × 117 = 25272
```

### Strategy
1. Continue connecting **closest unconnected pairs**
2. Use **Union-Find** (Disjoint Set Union) to track circuits efficiently
3. Stop when all boxes are in the **same circuit**
4. Multiply the **X coordinates** of the final pair

### ⭐ Answer: **302133440**