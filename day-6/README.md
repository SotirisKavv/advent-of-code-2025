# 🎄 Day 6: Trash Compactor

## Part 1

### Story
After helping the Elves in the kitchen, you were re-enacting a movie scene when you **over-enthusiastically jumped into the garbage chute!**

A brief fall later, you find yourself in a garbage smasher with a magnetically sealed door.

A family of cephalopods approaches! They can get the door open, but it will take time. While you wait, they ask if you can help the youngest cephalopod with her **math homework**.

### Cephalopod Math Basics
The math worksheet consists of problems where numbers need to be either **added** (`+`) or **multiplied** (`*`) together.

However, the problems are arranged **horizontally** in a strange way:

```
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
```

### Reading Rules (Part 1)
- Each problem's numbers are arranged **vertically**
- The symbol at the **bottom** indicates the operation
- Problems are separated by a **full column of spaces**
- Left/right alignment within each problem can be ignored

### Example Breakdown

| Problem | Calculation | Result |
|---------|-------------|--------|
| Problem 1 | `123 * 45 * 6` | `33210` |
| Problem 2 | `328 + 64 + 98` | `490` |
| Problem 3 | `51 * 387 * 215` | `4243455` |
| Problem 4 | `64 + 23 + 314` | `401` |

### Grand Total
Add all individual answers together:

```
33210 + 490 + 4243455 + 401 = 4277556
```

### ⭐ Answer: **5524274308182**

---

## Part 2

### The Real Rules! 🦑
The big cephalopods come back and realize they **forgot to explain** how to actually read cephalopod math!

### Correct Reading Method
**Cephalopod math is written RIGHT-TO-LEFT in columns!**

- Each **column** represents one number
- Read digits **vertically** (top = most significant, bottom = least significant)
- Problems still separated by **space columns**
- Operator still at the **bottom**

### Same Example, Different Reading

```
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
```

**Reading RIGHT-TO-LEFT:**

| Problem | Columns (right-to-left) | Calculation | Result |
|---------|-------------------------|-------------|--------|
| Rightmost | `4`, `431`, `623` | `4 + 431 + 623` | `1058` |
| 2nd from right | `175`, `581`, `32` | `175 * 581 * 32` | `3253600` |
| 3rd from right | `8`, `248`, `369` | `8 + 248 + 369` | `625` |
| Leftmost | `356`, `24`, `1` | `356 * 24 * 1` | `8544` |

### Column Reading Example
For the rightmost problem (`+`):
```
Column 1: 4   (vertical: 4)
Column 2: 431 (vertical: 4, 3, 1 top-to-bottom)
Column 3: 623 (vertical: 6, 2, 3 top-to-bottom)
```

### New Grand Total
```
1058 + 3253600 + 625 + 8544 = 3263827
```

### ⭐ Answer: **8843673199391**