# 🎄 Day 5: Inventory Management System

## Part 1

### Story
As the forklifts break through the wall, the Elves discover a cafeteria on the other side!

You hear commotion from the kitchen: "At this rate, we won't have any time left to put the wreaths up in the dining hall!"

"If only we hadn't switched to the new inventory management system right before Christmas!" another Elf exclaims.

### The Problem
The Elves can't figure out which ingredients are **fresh** and which are **spoiled** due to their complicated new system.

### Database Format
The database consists of:
1. **Fresh ingredient ID ranges** (inclusive)
2. A blank line
3. **Available ingredient IDs**

### Example Input

**Fresh ID Ranges:**
```
3-5
10-14
16-20
12-18
```

**Available IDs:**
```
1
5
8
11
17
32
```

### Rules
- Ranges are **inclusive**: `3-5` means IDs `3`, `4`, and `5` are fresh
- Ranges can **overlap**: an ID is fresh if it's in **any** range

### Example Walkthrough

| Ingredient ID | Status | Reason |
|---------------|--------|--------|
| `1` | ❌ Spoiled | Not in any range |
| `5` | ✅ Fresh | In range `3-5` |
| `8` | ❌ Spoiled | Not in any range |
| `11` | ✅ Fresh | In range `10-14` |
| `17` | ✅ Fresh | In ranges `16-20` **and** `12-18` |
| `32` | ❌ Spoiled | Not in any range |

**Result:** `3` fresh ingredients out of `6` available

### ⭐ Answer: **896**

---

## Part 2

### New Challenge
The Elves start bringing spoiled inventory to the trash chute. Now they want to know **all possible IDs** that the fresh ranges consider to be fresh—so they can stop bugging you with every new shipment!

### Simplified Problem
- **Ignore** the available ingredient IDs section
- **Count** all IDs covered by the fresh ranges

### Example Ranges
```
3-5
10-14
16-20
12-18
```

### Calculating Total Fresh IDs

**Individual ranges:**
- `3-5` → IDs: `3, 4, 5` (3 IDs)
- `10-14` → IDs: `10, 11, 12, 13, 14` (5 IDs)
- `16-20` → IDs: `16, 17, 18, 19, 20` (5 IDs)
- `12-18` → IDs: `12, 13, 14, 15, 16, 17, 18` (7 IDs)

**Combined (merged overlaps):**
- `3-5` → `3, 4, 5`
- `10-20` → `10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20` (merged `10-14`, `16-20`, and `12-18`)

**Fresh IDs:** `3, 4, 5, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20`

**Total:** `14` fresh ingredient IDs

### Strategy
1. Sort ranges by start position
2. Merge overlapping ranges
3. Sum the lengths of merged ranges

### ⭐ Answer: **346240317247002**