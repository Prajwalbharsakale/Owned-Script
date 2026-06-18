````md
# Move Zeroes - Deep Dive

---

# Problem Statement

Given an integer array `nums`, move all zeros to the end while maintaining the relative order of non-zero elements.

Example:

```python
nums = [4,2,0,1,8,0]
```

Output:

```python
[4,2,1,8,0,0]
```

---

# Constraints

- Do the operation in-place.
- Maintain relative order.
- Minimize extra space.

---

# Understanding the Problem

Input:

```text
4 2 0 1 8 0
```

Output:

```text
4 2 1 8 0 0
```

Observe:

- Non-zero numbers remain in same order.
- Zeroes are pushed to the end.
- Array size remains same.

---

# Approach 1 : Built-in Functions

### Idea

Remove zeros and append them back.

---

### Code

```python
count_zero = nums.count(0)

while 0 in nums:
    nums.remove(0)

nums.extend([0]*count_zero)
```

---

### Dry Run

Initial:

```text
4 2 0 1 8 0
```

Remove first zero:

```text
4 2 1 8 0
```

Remove second zero:

```text
4 2 1 8
```

Append:

```text
4 2 1 8 0 0
```

---

### Complexity

count():

```text
O(n)
```

0 in nums:

```text
O(n)
```

remove():

```text
O(n)
```

Overall:

```text
Time = O(n²)

Space = O(1)
```

---

# Approach 2 : Extra Array

### Idea

Store all non-zero elements.

Then append zeros.

---

### Code

```python
answer = []

for num in nums:

    if num != 0:
        answer.append(num)

while len(answer) < len(nums):
    answer.append(0)
```

---

### Dry Run

Initial:

```text
4 2 0 1 8 0
```

Non-zero array:

```text
4 2 1 8
```

Append zeros:

```text
4 2 1 8 0 0
```

---

### Complexity

```text
Time = O(n)

Space = O(n)
```

---

# Approach 3 : Brute Force Nested Loops

### Idea

Whenever a zero is found, search for next non-zero.

Swap.

---

### Code

```python
for i in range(len(nums)):

    if nums[i] == 0:

        for j in range(i+1,len(nums)):

            if nums[j] != 0:

                nums[i], nums[j] = nums[j], nums[i]

                break
```

---

### Dry Run

Initial:

```text
4 2 0 1 8 0
```

Zero found at index 2.

Search next non-zero:

```text
1
```

Swap:

```text
4 2 1 0 8 0
```

Next zero at index 3.

Search:

```text
8
```

Swap:

```text
4 2 1 8 0 0
```

---

### Complexity

Worst case:

```text
Time = O(n²)

Space = O(1)
```

---

# Approach 4 : True Two Pointers

### Idea

i stops at zero.

j searches ahead for a non-zero.

---

### Pointer Visualization

```text
4 2 0 1 8 0
    i j
```

---

### Code

```python
i = 0
j = 1

while j < len(nums):

    if nums[i] != 0:

        i += 1

        if i >= j:
            j = i + 1

    elif nums[j] == 0:

        j += 1

    else:

        nums[i], nums[j] = nums[j], nums[i]

        i += 1
        j += 1
```

---

### Detailed Iteration

Initial:

```text
4 2 0 1 8 0

i=0
j=1
```

---

Iteration 1

```text
nums[i]=4
nums[j]=2
```

4 is not zero.

Move i.

```text
i=1
j=2
```

---

Iteration 2

```text
nums[i]=2
nums[j]=0
```

2 is not zero.

Move i.

```text
i=2
j=3
```

---

Iteration 3

```text
nums[i]=0
nums[j]=1
```

Swap.

```text
4 2 1 0 8 0
```

Move both.

```text
i=3
j=4
```

---

Iteration 4

```text
nums[i]=0
nums[j]=8
```

Swap.

```text
4 2 1 8 0 0
```

Move both.

---

### Complexity

```text
Time = O(n)

Space = O(1)
```

---

# Approach 5 : Fast and Slow Pointer

### Idea

Fast scans.

Slow tracks where next non-zero should go.

---

### Code

```python
slow = 0

for fast in range(len(nums)):

    if nums[fast] != 0:

        nums[slow], nums[fast] = nums[fast], nums[slow]

        slow += 1
```

---

### Dry Run

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

Swap:

```text
4 2 1 0 8 0
```

---

Iteration 5

Swap:

```text
4 2 1 8 0 0
```

---

### Complexity

```text
Time = O(n)

Space = O(1)
```

---

# Complexity Comparison

| Approach | Time | Space |
|----------|------|------|
| Built-in | O(n²) | O(1) |
| Extra Array | O(n) | O(n) |
| Nested Loops | O(n²) | O(1) |
| True Two Pointers | O(n) | O(1) |
| Fast & Slow | O(n) | O(1) |

---

# Common Mistakes

## Forgetting Relative Order

Wrong:

```text
0 4 2 1 8 0
```

Correct:

```text
4 2 1 8 0 0
```

---

## Thinking Two Pointers Is O(n²)

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

## Using Extra Space

Works.

But not optimal.

---

# Interview Discussion

If asked in an interview:

1. Explain brute force.
2. Analyze complexity.
3. Optimize using extra array.
4. Optimize further using two pointers.
5. Reach O(n) time and O(1) space.

This demonstrates problem-solving ability instead of memorization.

---

# Pattern Learned

Move Zeroes teaches:

- Same Direction Two Pointers
- Fast & Slow Pointers
- In-place modification
- Space optimization
- Brute Force → Optimal thinking

This pattern appears in dozens of problems.
````
