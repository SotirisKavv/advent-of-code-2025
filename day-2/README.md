# 🎄 Day 2: Gift Shop

## Part 1

### Story
You get inside and take the elevator to its only other stop: the gift shop. "Thank you for visiting the North Pole!" gleefully exclaims a nearby sign. You aren't sure who is even allowed to visit the North Pole, but you know you can access the lobby through here, and from there you can access the rest of the North Pole base.

As you make your way through the surprisingly extensive selection, one of the clerks recognizes you and asks for your help.

### The Problem
A younger Elf was playing on a gift shop computer and managed to add a whole bunch of **invalid product IDs** to their database! You need to identify them.

### Input Format
Product ID ranges (comma-separated):
```
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
```

**Format:** `start-end` where each range gives first and last ID separated by a dash.

### Invalid ID Pattern
An ID is invalid if it's made of **some sequence of digits repeated exactly twice**.

**Examples:**
- `55` → `5` repeated twice ✗
- `6464` → `64` repeated twice ✗
- `123123` → `123` repeated twice ✗
- `101` → not a repeated pattern ✓

⚠️ **Note:** No leading zeroes! `0101` isn't an ID at all.

### Example Analysis
| Range | Invalid IDs | Details |
|-------|-------------|---------|
| `11-22` | 2 | `11`, `22` |
| `95-115` | 1 | `99` |
| `998-1012` | 1 | `1010` |
| `1188511880-1188511890` | 1 | `1188511885` |
| `222220-222224` | 1 | `222222` |
| `1698522-1698528` | 0 | none |
| `446443-446449` | 1 | `446446` |
| `38593856-38593862` | 1 | `38593859` |

**Sum of all invalid IDs:** `1227775554`

### ⭐ Answer: **12586854255**

---

## Part 2

### Updated Discovery
The clerk discovers there are still invalid IDs! The young Elf was doing other silly patterns too.

### New Rule
An ID is invalid if it's made of **some sequence of digits repeated at least twice** (2 or more times).

**Examples:**
- `12341234` → `1234` × 2 ✗
- `123123123` → `123` × 3 ✗
- `1212121212` → `12` × 5 ✗
- `1111111` → `1` × 7 ✗

### Updated Example Analysis
| Range | Invalid IDs | Details |
|-------|-------------|---------|
| `11-22` | 2 | `11`, `22` |
| `95-115` | 2 | `99`, `111` ⬅️ *new* |
| `998-1012` | 2 | `999` ⬅️ *new*, `1010` |
| `1188511880-1188511890` | 1 | `1188511885` |
| `222220-222224` | 1 | `222222` |
| `1698522-1698528` | 0 | none |
| `446443-446449` | 1 | `446446` |
| `38593856-38593862` | 1 | `38593859` |
| `565653-565659` | 1 | `565656` ⬅️ *new* |
| `824824821-824824827` | 1 | `824824824` ⬅️ *new* |
| `2121212118-2121212124` | 1 | `2121212121` ⬅️ *new* |

**Sum of all invalid IDs:** `4174379265`

### ⭐ Answer: **17298174201**