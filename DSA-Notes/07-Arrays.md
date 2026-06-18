# Arrays

---

# Introduction

Array is the most fundamental data structure.

Almost every problem eventually reduces to:

- Arrays
- Strings
- Matrices

Mastering arrays means mastering:

- HashMap
- Two Pointers
- Sliding Window
- Prefix Sum
- Binary Search
- Dynamic Programming

---

# What is an Array?

An array is a contiguous block of memory storing elements of the same type.

Example:

```python
nums = [4,2,7,1,9]
```

Indexing:

```text
Index

0 1 2 3 4

Array

4 2 7 1 9
```

---

# Accessing Elements

```python
nums[2]
```

Output:

```python
7
```

Time Complexity:

```text
O(1)
```

---

# Traversing an Array

### Using Index

```python
for i in range(len(nums)):
    print(nums[i])
```

Complexity:

```text
Time : O(n)

Space : O(1)
```

---

### Using Element

```python
for num in nums:
    print(num)
```

Complexity:

```text
Time : O(n)

Space : O(1)
```

---

### Using enumerate()

```python
for i, num in enumerate(nums):
    print(i, num)
```

Complexity:

```text
O(n)
```

---

# Array Operations

---

## Append

```python
nums.append(10)
```

Before:

```text
4 2 7 1
```

After:

```text
4 2 7 1 10
```

Complexity:

```text
Average O(1)
```

---

## Insert

```python
nums.insert(2,100)
```

Before:

```text
4 2 7 1
```

After:

```text
4 2 100 7 1
```

Complexity:

```text
O(n)
```

---

## Remove

```python
nums.remove(7)
```

Complexity:

```text
O(n)
```

---

## Pop

```python
nums.pop()
```

Complexity:

```text
O(1)
```

---

## Pop Front

```python
nums.pop(0)
```

Complexity:

```text
O(n)
```

Because all elements shift left.

---

# Common Traversal Patterns

---

# Pattern 1: Find Largest Element

### Built-in

```python
max(nums)
```

Complexity:

```text
O(n)
```

---

### Manual

```python
largest = nums[0]

for num in nums:
    if num > largest:
        largest = num
```

Complexity:

```text
Time : O(n)

Space : O(1)
```

---

# Pattern 2: Find Minimum Element

```python
smallest = nums[0]

for num in nums:
    if num < smallest:
        smallest = num
```

Complexity:

```text
O(n)
```

---

# Pattern 3: Frequency Count

Example:

```python
nums = [1,1,2,3,2]
```

Answer:

```text
1 → 2 times

2 → 2 times

3 → 1 time
```

Using HashMap:

```python
freq = {}

for num in nums:
    freq[num] = freq.get(num,0)+1
```

Complexity:

```text
Time : O(n)

Space : O(n)
```

---

# Pattern 4: Running Sum

Example:

```python
nums = [1,2,3,4]
```

Result:

```text
1
3
6
10
```

Code:

```python
sum_so_far = 0

for num in nums:
    sum_so_far += num
```

Complexity:

```text
O(n)
```

---

# Pattern 5: Reverse Array

### Built-in

```python
nums.reverse()
```

---

### Slicing

```python
nums[::-1]
```

Space:

```text
O(n)
```

---

### Two Pointers

```python
left = 0
right = len(nums)-1

while left < right:
    nums[left], nums[right] = nums[right], nums[left]

    left += 1
    right -= 1
```

Complexity:

```text
Time : O(n)

Space : O(1)
```

---

# Pattern 6: Search Element

### Linear Search

```python
for num in nums:
    if num == target:
        return True
```

Complexity:

```text
O(n)
```

---

### Membership Operator

```python
target in nums
```

Complexity:

```text
O(n)
```

---

# Pattern 7: Count Elements

Built-in:

```python
nums.count(5)
```

Complexity:

```text
O(n)
```

---

Manual:

```python
count = 0

for num in nums:
    if num == target:
        count += 1
```

Complexity:

```text
O(n)
```

---

# Pattern 8: Remove Duplicates

### Using Set

```python
list(set(nums))
```

Complexity:

```text
Time : O(n)

Space : O(n)
```

---

# Pattern 9: Sorting

Built-in:

```python
nums.sort()
```

Complexity:

```text
O(n log n)
```

---

# Pattern 10: Pair Problems

Examples:

- Two Sum
- Three Sum

Possible approaches:

### Brute Force

```python
for i in range(n):
    for j in range(i+1,n):
```

Complexity:

```text
O(n²)
```

---

### HashMap

Complexity:

```text
O(n)
```

---

### Two Pointers

Sorted arrays:

```text
left ---->

<---- right
```

Complexity:

```text
O(n)
```

---

# Pattern 11: Move Elements

Examples:

- Move Zeroes
- Remove Duplicates

Approaches:

### Extra Array

```text
O(n)
Space O(n)
```

---

### Two Pointers

```text
O(n)
Space O(1)
```

---

# Pattern 12: Rotation

Example:

```text
1 2 3 4 5

Rotate right by 2

4 5 1 2 3
```

Approaches:

### Extra Array

```text
O(n)
```

---

### Reversal Algorithm

```text
Reverse entire array

Reverse first k

Reverse remaining
```

Complexity:

```text
Time : O(n)

Space : O(1)
```

---

# Pattern 13: Prefix Sum

Example:

```python
nums=[1,2,3,4]
```

Prefix array:

```text
1 3 6 10
```

Useful for:

- Range Sum
- Subarray Sum

Complexity:

```text
Time : O(n)

Space : O(n)
```

---

# Pattern Recognition

---

### Need frequency?

Think:

```text
HashMap
Counter
```

---

### Need pair?

Think:

```text
Two Pointers
HashMap
```

---

### Need reverse?

Think:

```text
Two Pointers
```

---

### Need repeated sums?

Think:

```text
Prefix Sum
```

---

### Need maximum subarray?

Think:

```text
Sliding Window
Kadane's Algorithm
```

---

# Common Mistakes

---

## Using pop(0)

```python
nums.pop(0)
```

Complexity:

```text
O(n)
```

Avoid.

---

## Using list membership repeatedly

Wrong:

```python
for num in nums:
    if num in nums:
```

Complexity:

```text
O(n²)
```

Use set.

---

## String concatenation inside loop

Wrong:

```python
result += ch
```

Can become:

```text
O(n²)
```

Use:

```python
arr.append(ch)

"".join(arr)
```

---

# Important Problems

### Easy

1. Largest Element
2. Second Largest Element
3. Check Sorted Array
4. Remove Duplicates
5. Move Zeroes
6. Rotate Array
7. Missing Number
8. Running Sum
9. Contains Duplicate
10. Best Time to Buy and Sell Stock

---

### Medium

11. Two Sum
12. Product Except Self
13. Majority Element
14. Maximum Subarray
15. Three Sum
16. Container With Most Water
17. Subarray Sum Equals K
18. Merge Intervals
19. Spiral Matrix
20. Set Matrix Zeroes

---

# Complexity Table

| Operation | Time |
|------------|------|
| Access | O(1) |
| Search | O(n) |
| Append | O(1) |
| Insert | O(n) |
| Delete End | O(1) |
| Delete Front | O(n) |
| Reverse | O(n) |
| Sort | O(n log n) |
| Traversal | O(n) |

---

# Next Topics

Arrays lead naturally to:

```text
Arrays
↓
HashMap
↓
Two Pointers
↓
Sliding Window
↓
Prefix Sum
↓
Binary Search
↓
Dynamic Programming
```

Master arrays first.

Most interview questions are simply combinations of array patterns.
