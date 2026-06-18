# Same Direction Two Pointers

---

# Introduction

Two Pointers is one of the most important techniques in DSA.

There are three types:

1. Same Direction
2. Opposite Direction
3. Fast and Slow

In this file, we focus on:

```text
Same Direction Two Pointers
```

Both pointers move from left to right.

```text
slow ---->

fast -------->
```

or

```text
i ---->

j -------->
```

---

# When To Use Same Direction Two Pointers

Usually when:

- Need to remove duplicates.
- Need to move elements.
- Need partitioning.
- Need to maintain relative order.
- Need to compress data.
- Need in-place modification.

---

# General Template

```python
slow = 0

for fast in range(len(nums)):

    if condition:
        nums[slow] = nums[fast]
        slow += 1
```

---

# Why Is Complexity O(n)?

Many beginners think:

```python
slow = 0

for fast in range(n):
```

means:

```text
O(n²)
```

Wrong.

Both pointers only move forward.

Suppose:

```text
slow moves n times

fast moves n times
```

Total:

```text
2n
```

Ignoring constants:

```text
O(n)
```

Space:

```text
O(1)
```

---

# Pattern 1: Move Zeroes

Input:

```python
nums = [4,2,0,1,8,0]
```

Output:

```python
[4,2,1,8,0,0]
```

---

## Approach 1

Extra Array

```python
non_zero = []

for num in nums:
    if num != 0:
        non_zero.append(num)

while len(non_zero) < len(nums):
    non_zero.append(0)
```

Complexity:

```text
Time = O(n)

Space = O(n)
```

---

## Approach 2

Same Direction Two Pointers

```python
slow = 0

for fast in range(len(nums)):

    if nums[fast] != 0:

        nums[slow], nums[fast] = nums[fast], nums[slow]

        slow += 1
```

Complexity:

```text
Time = O(n)

Space = O(1)
```

---

# Dry Run

Initial:

```text
4 2 0 1 8 0
s
f
```

---

After first iteration

```text
4 2 0 1 8 0
  s
  f
```

---

Second iteration

```text
4 2 0 1 8 0
    s
    f
```

---

Third iteration

```text
4 2 0 1 8 0
    s
      f
```

Zero found.

Skip.

---

Fourth iteration

```text
4 2 0 1 8 0
    s
        f
```

Swap:

```text
4 2 1 0 8 0
```

---

Fifth iteration

```text
4 2 1 0 8 0
      s
          f
```

Swap:

```text
4 2 1 8 0 0
```

---

# Pattern 2: Remove Duplicates from Sorted Array

Input:

```python
[1,1,2,2,3]
```

Output:

```python
[1,2,3]
```

---

Brute Force

Using set.

```python
list(set(nums))
```

Complexity:

```text
Time = O(n)

Space = O(n)
```

---

Optimal

```python
slow = 1

for fast in range(1,len(nums)):

    if nums[fast] != nums[fast-1]:

        nums[slow] = nums[fast]

        slow += 1
```

Complexity:

```text
Time = O(n)

Space = O(1)
```

---

# Dry Run

Initial

```text
1 1 2 2 3

s
  f
```

Duplicate.

Skip.

---

```text
1 1 2 2 3

s
    f
```

Different.

Copy.

```text
1 2 2 2 3

  s
    f
```

Continue.

Result:

```text
1 2 3
```

---

# Pattern 3: Partition Array

Goal:

Move negative numbers to the left.

Input:

```python
[-1,4,-2,5,-3]
```

Output:

```python
[-1,-2,-3,4,5]
```

Template:

```python
slow = 0

for fast in range(len(nums)):

    if nums[fast] < 0:

        nums[slow], nums[fast] = nums[fast], nums[slow]

        slow += 1
```

Complexity:

```text
Time = O(n)

Space = O(1)
```

---

# Pattern 4: Remove Target Value

Input:

```python
nums=[3,2,2,3]

val=3
```

Output:

```python
[2,2]
```

Template:

```python
slow = 0

for fast in range(len(nums)):

    if nums[fast] != val:

        nums[slow] = nums[fast]

        slow += 1
```

Complexity:

```text
O(n)
```

---

# Pattern 5: String Compression

Input:

```python
aaabbbccc
```

Output:

```python
a3b3c3
```

Useful for:

- Compression problems
- Encoding

Complexity:

```text
O(n)
```

---

# Pattern Recognition

If you hear:

### Move

Examples:

- Move Zeroes
- Move Negatives

Think:

```text
Same Direction Two Pointers
```

---

### Remove

Examples:

- Remove Duplicates
- Remove Element

Think:

```text
Same Direction Two Pointers
```

---

### Partition

Examples:

- Separate positives and negatives

Think:

```text
Same Direction Two Pointers
```

---

### Compress

Think:

```text
Same Direction Two Pointers
```

---

# Master Template

```python
slow = 0

for fast in range(len(nums)):

    if condition:

        nums[slow] = nums[fast]

        slow += 1
```

or

```python
slow = 0

for fast in range(len(nums)):

    if condition:

        nums[slow], nums[fast] = nums[fast], nums[slow]

        slow += 1
```

---

# Complexity

| Pattern | Time | Space |
|----------|------|------|
| Move Zeroes | O(n) | O(1) |
| Remove Duplicates | O(n) | O(1) |
| Remove Element | O(n) | O(1) |
| Partition Array | O(n) | O(1) |

---

# Common Mistakes

### Forgetting to move slow

Wrong:

```python
if condition:
    nums[slow] = nums[fast]
```

Correct:

```python
if condition:
    nums[slow] = nums[fast]
    slow += 1
```

---

### Thinking Two Pointers means O(n²)

Wrong.

Both pointers only move forward.

Total movement:

```text
n + n = 2n
```

Therefore:

```text
O(n)
```

---

### Using Extra Array

Works.

But space becomes:

```text
O(n)
```

Two pointers reduce space to:

```text
O(1)
```

---

# Important Problems

Easy:

1. Move Zeroes
2. Remove Element
3. Remove Duplicates from Sorted Array
4. Squares of Sorted Array

Medium:

5. Sort Colors
6. Partition Labels
7. Dutch National Flag
8. Compress String

Hard:

9. First Missing Positive

---

# Golden Rule

Whenever you hear:

```text
Move
Remove
Compress
Partition
```

Think:

```text
Same Direction Two Pointers
```
