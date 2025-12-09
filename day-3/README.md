# 🎄 Day 3: Lobby

## Part 1

### Story
You descend a short staircase and enter the surprisingly vast lobby. After passing through security, you discover that all elevators have red lights above them—they're all offline.

"Sorry about that," an Elf apologizes. "Some kind of electrical surge seems to have fried them."

You explain your need to get further underground. The escalator to the printing department could help, but it's also offline. However, it's not fried—it just needs power!

### The Challenge
There are **batteries** nearby that can supply emergency power. Each battery is labeled with a **joltage rating** (1-9).

**Input example:**
```
987654321111111
811111111111119
234234234234278
818181911112111
```

### Battery Banks
- Each line = one bank of batteries
- Within each bank, turn on **exactly 2 batteries**
- Joltage = number formed by the two digits (cannot rearrange!)

**Example:** Bank `12345` with batteries 2 and 4 turned on → `24` jolts

### Goal
Find the **largest possible joltage** each bank can produce.

### Example Analysis
| Bank | Best Joltage | Strategy |
|------|--------------|----------|
| `987654321111111` | **98** | Turn on first two batteries |
| `811111111111119` | **89** | Turn on batteries 8 and 9 |
| `234234234234278` | **78** | Turn on last two (7 and 8) |
| `818181911112111` | **92** | Turn on 9 and 2 |

**Total:** 98 + 89 + 78 + 92 = **357**

### ⭐ Answer: **17613**

---

## Part 2

### New Requirement
The escalator doesn't move! The Elf hits the big red **"joltage limit safety override"** button after confirming "yes, I'm sure" many times.

Now you need to turn on **exactly 12 batteries** per bank instead of 2.

### Updated Rules
- Turn on **12 batteries** per bank (not 2)
- Joltage = 12-digit number formed by selected batteries
- Still cannot rearrange batteries—maintain order!

### Strategy
To maximize the 12-digit number, **remove the smallest digits** that hurt the final value (greedy removal algorithm).

### Example Analysis
| Bank | Best 12-Digit Joltage | What to Remove |
|------|----------------------|----------------|
| `987654321111111` | `987654321111` | Remove trailing 1s |
| `811111111111119` | `811111111119` | Remove middle 1s |
| `234234234234278` | `434234234278` | Remove `2`, `3`, `2` at start |
| `818181911112111` | `888911112111` | Remove 1s near front |

**Calculation:**
```
  987654321111
+ 811111111119
+ 434234234278
+ 888911112111
─────────────────
= 3121910778619
```

### ⭐ Answer: **175304218462560**