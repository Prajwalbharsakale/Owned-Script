# Fast and Slow Pointers

---

# Introduction

Fast and Slow Pointer is one of the most powerful two-pointer patterns.

It is also known as:

- Floyd's Algorithm
- Tortoise and Hare Algorithm

Idea:

```text
slow --->

fast -------->
```

or

```text
slow moves by 1

fast moves by 2
```

---

# When To Use Fast and Slow Pointers

Think about this pattern when you hear:

- Middle of Linked List
- Cycle Detection
- Circular Array
- Happy Number
- Duplicate Number
- Remove Duplicates
- Move Zeroes
- In-place Array Compression

---

# Why Is Complexity O(n)?

Beginners often think:

```python
slow += 1
fast += 1
```

means:

```text
O(n²)
```

Wrong.

Suppose:

```text
slow moves n times

fast moves n times
```

Total:

```text
2n
```

Big O ignores constants.

Therefore:

```text
Time = O(n)

Space = O(1)
```

---

# Types of Fast and Slow Pointers

There are three variations:

### Type 1

Slow moves by 1

Fast moves by 1

```text
s --->

f -------->
```

Examples:

- Move Zeroes
- Remove Duplicates

---

### Type 2

Slow moves by 1

Fast moves by 2

```text
slow --->

fast ---------->
```

Examples:

- Middle Linked List
- Cycle Detection

---

### Type 3

Slow stops

Fast searches

```text
slow
↓

4 2 0 1 8 0
    ↑
    fast
```

Examples:

- Move Zeroes
- Partition Array

---

# Pattern 1 : Move Zeroes

Input:

```python
nums = [4,2,0,1,8,0]
```

Output:

```python
[4,2,1,8,0,0]
```

---

## Brute Force

Nested loops.

```python
for i in range(n):
    if nums[i] == 0:

        for j in range(i+1,n):
```

Complexity:

```text
Time = O(n²)

Space = O(1)
```

---

## Extra Array

```python
non_zero = []

for num in nums:
    if num != 0:
        non_zero.append(num)
```

Complexity:

```text
Time = O(n)

Space = O(n)
```

---

## Fast and Slow Pointer

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

Iteration 1

```text
4 2 0 1 8 0

  s
  f
```

---

Iteration 2

```text
4 2 0 1 8 0

    s
    f
```

---

Iteration 3

Zero found.

Only fast moves.

```text
4 2 0 1 8 0

    s
      f
```

---

Iteration 4

Swap.

```text
4 2 1 0 8 0

      s
        f
```

---

Iteration 5

Swap.

```text
4 2 1 8 0 0

        s
          f
```

---

# Pattern 2 : Remove Duplicates

Input:

```python
[1,1,2,2,3]
```

Output:

```python
[1,2,3]
```

---

Template

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

# Pattern 3 : Middle of Linked List

Linked List:

```text
1 → 2 → 3 → 4 → 5
```

Need:

```text
3
```

---

Brute Force

Count nodes.

Traverse again.

Complexity:

```text
Time = O(n)

Space = O(1)
```

Two traversals.

---

Fast and Slow

```python
while fast and fast.next:

    slow = slow.next

    fast = fast.next.next
```

---

Dry Run

Initial:

```text
1 → 2 → 3 → 4 → 5

s
f
```

---

Iteration 1

```text
1 → 2 → 3 → 4 → 5

    s
        f
```

---

Iteration 2

```text
1 → 2 → 3 → 4 → 5

        s
```

Fast reaches end.

Answer:

```text
3
```

Complexity:

```text
Time = O(n)

Space = O(1)
```

---

# Pattern 4 : Detect Cycle

Linked List:

```text
1 → 2 → 3 → 4
      ↑     ↓
      ← ← ←
```

---

Using HashSet

Store visited nodes.

Complexity:

```text
Time = O(n)

Space = O(n)
```

---

Using Floyd's Algorithm

```python
while fast and fast.next:

    slow = slow.next

    fast = fast.next.next

    if slow == fast:
        return True
```

Complexity:

```text
Time = O(n)

Space = O(1)
```

---

# Why Does It Work?

Inside a cycle:

```text
slow --->

fast -------->
```

Eventually fast catches slow.

Like two runners on a circular track.

---

# Pattern 5 : Happy Number

Example:

```text
19

1² + 9² = 82

8² + 2² = 68

6² + 8² = 100

1² + 0² + 0² = 1
```

Answer:

Happy Number.

---

Observation:

Numbers either:

- Reach 1
- Enter a cycle

Cycle Detection can be used.

---

Complexity:

```text
Time = O(log n)

Space = O(1)
```

---

# Pattern 6 : Find Duplicate Number

Input:

```python
[1,3,4,2,2]
```

Output:

```python
2
```

---

HashSet

```text
Time = O(n)

Space = O(n)
```

---

Floyd Cycle Detection

```text
Time = O(n)

Space = O(1)
```

---

# Master Templates

---

## Array Template

```python
slow = 0

for fast in range(len(nums)):

    if condition:

        nums[slow] = nums[fast]

        slow += 1
```

---

## Linked List Template

```python
slow = head

fast = head

while fast and fast.next:

    slow = slow.next

    fast = fast.next.next
```

---

## Cycle Detection Template

```python
slow = head

fast = head

while fast and fast.next:

    slow = slow.next

    fast = fast.next.next

    if slow == fast:
        return True
```

---

# Complexity Table

| Problem | Time | Space |
|----------|------|------|
| Move Zeroes | O(n) | O(1) |
| Remove Duplicates | O(n) | O(1) |
| Middle Linked List | O(n) | O(1) |
| Linked List Cycle | O(n) | O(1) |
| Happy Number | O(log n) | O(1) |
| Find Duplicate Number | O(n) | O(1) |

---

# Common Mistakes

### Thinking Two Pointers Means O(n²)

Wrong.

Both pointers move forward.

Maximum movement:

```text
n + n = 2n
```

Therefore:

```text
O(n)
```

---

### Forgetting

```python
while fast and fast.next
```

Writing:

```python
while fast
```

can cause:

```text
AttributeError
```

---

### Moving Fast By One

Wrong:

```python
fast = fast.next
```

Correct:

```python
fast = fast.next.next
```

for cycle problems.

---

# Important Problems

Easy

1. Move Zeroes
2. Remove Duplicates
3. Middle Linked List

Medium

4. Linked List Cycle
5. Happy Number
6. Find Duplicate Number

Hard

7. Circular Array Loop

---

# Golden Rule

Whenever you hear:

```text
Cycle
Middle
Duplicate
Move
Compress
```

Think:

```text
Fast and Slow Pointers
```
