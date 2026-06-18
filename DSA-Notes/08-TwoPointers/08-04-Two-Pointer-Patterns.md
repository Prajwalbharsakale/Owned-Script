# Two Pointer Patterns

---

# Introduction

Two Pointers is one of the most important patterns in DSA.

Many problems that initially appear to be:

```text
O(n²)
```

can often be reduced to:

```text
O(n)
```

or

```text
O(n log n)
```

using Two Pointers.

---

# Types of Two Pointers

There are three major types:

```text
1. Same Direction

slow ---->

fast -------->

------------------------

2. Opposite Direction

left ---->

<---- right

------------------------

3. Fast and Slow

slow --->

fast ---------->
```

Understanding when to use each type is more important than memorizing solutions.

---

# Type 1 : Same Direction

Both pointers move from left to right.

```text
slow ---->

fast -------->
```

---

## General Template

```python
slow = 0

for fast in range(len(nums)):

    if condition:

        nums[slow] = nums[fast]

        slow += 1
```

---

## When To Use

Whenever you hear:

- Move
- Remove
- Compress
- Partition
- Maintain order

---

## Examples

### Move Zeroes

```text
[4,2,0,1,8,0]

↓

[4,2,1,8,0,0]
```

---

### Remove Duplicates

```text
[1,1,2,2,3]

↓

[1,2,3]
```

---

### Remove Element

```text
Remove all 3s
```

---

### Partition Array

```text
Move negatives left
```

---

## Complexity

```text
Time = O(n)

Space = O(1)
```

---

# Type 2 : Opposite Direction

Pointers start at opposite ends.

```text
left ---->

<---- right
```

---

## General Template

```python
left = 0
right = len(nums)-1

while left < right:

    if condition:
        return answer

    elif something:
        left += 1

    else:
        right -= 1
```

---

## When To Use

Whenever you hear:

- Sorted Array
- Pair
- Reverse
- Palindrome
- Maximum Area

---

## Examples

### Reverse Array

```text
1 2 3 4 5

↓

5 4 3 2 1
```

---

### Valid Palindrome

```text
madam
```

---

### Two Sum II

```text
sorted array
```

---

### Container With Most Water

---

### Three Sum

---

## Complexity

```text
Time = O(n)

Space = O(1)
```

---

# Type 3 : Fast and Slow

Fast moves faster than slow.

```text
slow --->

fast ---------->
```

Usually:

```python
slow += 1

fast += 2
```

---

## General Template

```python
slow = head

fast = head

while fast and fast.next:

    slow = slow.next

    fast = fast.next.next
```

---

## When To Use

Whenever you hear:

- Cycle
- Middle
- Duplicate
- Circular

---

## Examples

### Middle of Linked List

```text
1→2→3→4→5

Answer = 3
```

---

### Detect Cycle

Floyd Algorithm.

---

### Happy Number

---

### Find Duplicate Number

---

## Complexity

```text
Time = O(n)

Space = O(1)
```

---

# Recognition Table

| Problem Clue | Pattern |
|-------------|----------|
| Move | Same Direction |
| Remove | Same Direction |
| Compress | Same Direction |
| Partition | Same Direction |
| Sorted Pair | Opposite Direction |
| Reverse | Opposite Direction |
| Palindrome | Opposite Direction |
| Max Area | Opposite Direction |
| Middle | Fast & Slow |
| Cycle | Fast & Slow |
| Duplicate | Fast & Slow |

---

# How To Decide?

---

## Question 1

Need to move elements?

Think:

```text
Same Direction
```

Examples:

- Move Zeroes
- Remove Duplicates

---

## Question 2

Need pair in sorted array?

Think:

```text
Opposite Direction
```

Examples:

- Two Sum II
- Three Sum

---

## Question 3

Need reverse?

Think:

```text
Opposite Direction
```

---

## Question 4

Need palindrome?

Think:

```text
Opposite Direction
```

---

## Question 5

Need middle node?

Think:

```text
Fast and Slow
```

---

## Question 6

Need cycle detection?

Think:

```text
Fast and Slow
```

---

# Complexity Proof

Many beginners think:

```python
while i<n and j<n:
```

means:

```text
O(n²)
```

Wrong.

Suppose:

```text
i moves n times

j moves n times
```

Total:

```text
2n
```

Ignoring constants:

```text
O(n)
```

---

# Brute Force vs Two Pointers

---

## Two Sum II

Brute Force

```python
for i in range(n):
    for j in range(i+1,n):
```

Complexity:

```text
O(n²)
```

---

Two Pointers

```python
left = 0
right = n-1
```

Complexity:

```text
O(n)
```

---

## Move Zeroes

Nested loops

```text
O(n²)
```

↓

Two Pointers

```text
O(n)
```

---

## Trapping Rain Water

Brute Force

```text
O(n²)
```

↓

Two Pointers

```text
O(n)
```

---

# Master Templates

---

## Same Direction

```python
slow = 0

for fast in range(len(nums)):

    if condition:

        nums[slow] = nums[fast]

        slow += 1
```

---

## Opposite Direction

```python
left = 0
right = len(nums)-1

while left < right:

    if condition:
        return answer

    elif something:
        left += 1

    else:
        right -= 1
```

---

## Fast and Slow

```python
slow = head
fast = head

while fast and fast.next:

    slow = slow.next
    fast = fast.next.next
```

---

# Most Important Problems

## Same Direction

Easy

1. Move Zeroes
2. Remove Element
3. Remove Duplicates

Medium

4. Sort Colors
5. Dutch National Flag

---

## Opposite Direction

Easy

1. Reverse String
2. Valid Palindrome
3. Two Sum II

Medium

4. Container With Most Water
5. Three Sum

Hard

6. Trapping Rain Water

---

## Fast and Slow

Easy

1. Middle Linked List

Medium

2. Linked List Cycle
3. Happy Number
4. Find Duplicate Number

Hard

5. Circular Array Loop

---

# Golden Rule

Whenever you see a problem ask:

```text
Do I need to move elements?

↓

Same Direction

----------------

Need pair/reverse?

↓

Opposite Direction

----------------

Need cycle or middle?

↓

Fast and Slow
```

Two Pointers is not a single pattern.

It is a family of patterns.
