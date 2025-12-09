# 🎄 Day 1: Secret Entrance

## Part 1

### Story
The Elves have good news and bad news.

The good news is that they've discovered project management! This has given them the tools they need to prevent their usual Christmas emergency. For example, they now know that the North Pole decorations need to be finished soon so that other critical tasks can start on time.

The bad news is that they've realized they have a different emergency: according to their resource planning, none of them have any time left to decorate the North Pole!

To save Christmas, the Elves need you to finish decorating the North Pole by December 12th.

### The Challenge
You arrive at the secret entrance to the North Pole base ready to start decorating. Unfortunately, the password seems to have been changed, so you can't get in. A document taped to the wall helpfully explains:

> "Due to new security protocols, the password is locked in the safe below. Please see the attached document for the new combination."

### The Safe Mechanism
The safe has a dial with only an arrow on it; around the dial are the numbers **0 through 99** in order. As you turn the dial, it makes a small click noise as it reaches each number.

**Rotation format:**
- `L` = rotate left (toward lower numbers)
- `R` = rotate right (toward higher numbers)
- Number = distance to rotate

**Examples:**
- Dial at `11` + `R8` → points at `19`
- Dial at `19` + `L19` → points at `0`
- Dial at `5` + `L10` → points at `95` (wraps around)
- Dial at `95` + `R5` → points at `0`

**Starting position:** `50`

### The Twist
The safe is a decoy! The actual password is **the number of times the dial points at 0 after any rotation** in the sequence.

### Example
```
L68  →  82
L30  →  52
R48  →   0  ✓
L5   →  95
R60  →  55
L55  →   0  ✓
L1   →  99
L99  →   0  ✓
R14  →  14
L82  →  32
```
**Password:** `3` (dial pointed at 0 three times)

### ⭐ Answer: **1154**

---

## Part 2

### New Discovery
While building a snowman (because the door won't open), you find another security document in the snow:

> "Due to newer security protocols, please use password method **0x434C49434B** until further notice."

### Updated Rule
Method `0x434C49434B` means: count **every time any click causes the dial to point at 0**, including clicks *during* rotations, not just at the end.

### Example Revisited
```
Start at 50
L68  →  82   (passes through 0 once during rotation)  ✓
L30  →  52
R48  →   0   (lands on 0)  ✓
L5   →  95
R60  →  55   (passes through 0 once during rotation)  ✓
L55  →   0   (lands on 0)  ✓
L1   →  99
L99  →   0   (lands on 0)  ✓
R14  →  14
L82  →  32   (passes through 0 once during rotation)  ✓
```
**Password:** `6` (3 endpoints + 3 during rotations)

⚠️ **Note:** A rotation like `R1000` from position `50` would pass through `0` **ten times** before returning to `50`!

### ⭐ Answer: **6819**