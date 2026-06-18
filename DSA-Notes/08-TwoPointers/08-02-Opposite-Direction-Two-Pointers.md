# Opposite Direction Two Pointers

---

# Introduction

In Opposite Direction Two Pointers, one pointer starts from the left and the other starts from the right.

```text
left ---->

<---- right
```

Both pointers move toward each other.

This pattern is extremely common in interviews and is used when:

- Array is sorted.
- Need to find a pair.
- Need to reverse.
- Need to check palindrome.
- Need to maximize or minimize something.
- Need to avoid O(n²) brute force.

---

# General Template

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

# Complexity

Since each pointer moves at most n times:

```text
Time = O(n)

Space = O(1)
```

---

# Pattern Recognition

Think Opposite Direction Two Pointers when you hear:

### Pair

Examples:

- Two Sum II
- Three Sum

---

### Reverse

Examples:

- Reverse Array
- Reverse String

---

### Palindrome

Examples:

- Valid Palindrome

---

### Max Area

Examples:

- Container With Most Water

---

### Sorted Array

Whenever the problem mentions:

```text
Sorted Array
```

Think:

```text
Binary Search
Two Pointers
```

---

# Pattern 1 : Reverse Array

Input:

```python
nums = [1,2,3,4,5]
```

Output:

```python
[5,4,3,2,1]
```

---

## Approach 1

Built-in

```python
nums.reverse()
```

Complexity:

```text
O(n)
```

---

## Approach 2

Slicing

```python
nums[::-1]
```

Complexity:

```text
Time = O(n)

Space = O(n)
```

---

## Approach 3

Opposite Direction Two Pointers

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
Time = O(n)

Space = O(1)
```

---

# Dry Run

Initial:

```text
1 2 3 4 5

L       R
```

Swap:

```text
5 2 3 4 1

  L   R
```

Swap:

```text
5 4 3 2 1

    LR
```

Stop.

---

# Pattern 2 : Valid Palindrome

Input:

```python
s = "madam"
```

Output:

```python
True
```

---

## Brute Force

Reverse string.

```python
s == s[::-1]
```

Complexity:

```text
Time = O(n)

Space = O(n)
```

---

## Optimal

```python
left = 0
right = len(s)-1

while left < right:

    if s[left] != s[right]:
        return False

    left += 1
    right -= 1

return True
```

Complexity:

```text
Time = O(n)

Space = O(1)
```

---

# Dry Run

```text
m a d a m

L       R
```

Equal.

Move.

```text
m a d a m

  L   R
```

Equal.

Move.

Pointers meet.

Answer:

```python
True
```

---

# Pattern 3 : Two Sum II

Input:

```python
nums = [2,7,11,15]

target = 9
```

Output:

```python
[0,1]
```

Array is sorted.

---

## Brute Force

Nested loops.

```python
for i in range(n):
    for j in range(i+1,n):
```

Complexity:

```text
O(n²)
```

---

## HashMap

```text
Time = O(n)

Space = O(n)
```

---

## Opposite Direction Two Pointers

```python
left = 0
right = len(nums)-1

while left < right:

    total = nums[left] + nums[right]

    if total == target:
        return [left,right]

    elif total < target:
        left += 1

    else:
        right -= 1
```

Complexity:

```text
Time = O(n)

Space = O(1)
```

---

# Why Does It Work?

Suppose:

```text
2 7 11 15

L       R

sum = 17
```

Target:

```text
9
```

Since array is sorted:

Moving right leftward decreases the sum.

---

# Pattern 4 : Container With Most Water

Input:

```python
height = [1,8,6,2,5,4,8,3,7]
```

---

## Brute Force

Try every pair.

```python
for i:
    for j:
```

Complexity:

```text
O(n²)
```

---

## Optimal

```python
left = 0
right = len(height)-1

while left < right:

    area = min(height[left],height[right])*(right-left)

    answer = max(answer, area)

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1
```

Complexity:

```text
Time = O(n)

Space = O(1)
```

---

# Why Move Smaller Height?

Example:

```text
1 8 6 2 5 4 8 3 7

L               R
```

Area is limited by:

```text
min(1,7)
```

Increasing the bigger side won't help.

Move the smaller side.

---

# Pattern 5 : Three Sum

Input:

```python
[-1,0,1,2,-1,-4]
```

Need:

```text
a+b+c=0
```

---

## Brute Force

Three loops.

```python
O(n³)
```

---

## Better

Sort.

Fix one element.

Use two pointers.

```python
for i in range(n):

    left = i+1
    right = n-1
```

Complexity:

```text
O(n²)
```

---

# Pattern 6 : Trapping Rain Water

Brute Force:

```text
O(n²)
```

Prefix Arrays:

```text
O(n)

Space O(n)
```

Two Pointers:

```text
O(n)

Space O(1)
```

---

# Master Template

## Pair Problems

```python
left = 0
right = len(nums)-1

while left < right:

    total = nums[left]+nums[right]

    if total == target:
        return

    elif total < target:
        left += 1

    else:
        right -= 1
```

---

## Reverse Problems

```python
left = 0
right = len(nums)-1

while left < right:

    nums[left], nums[right] = nums[right], nums[left]

    left += 1
    right -= 1
```

---

## Palindrome Problems

```python
left = 0
right = len(s)-1

while left < right:

    if s[left] != s[right]:
        return False

    left += 1
    right -= 1
```

---

# Complexity Summary

| Problem | Time | Space |
|----------|------|------|
| Reverse Array | O(n) | O(1) |
| Reverse String | O(n) | O(1) |
| Valid Palindrome | O(n) | O(1) |
| Two Sum II | O(n) | O(1) |
| Container With Most Water | O(n) | O(1) |
| Three Sum | O(n²) | O(1) |
| Trapping Rain Water | O(n) | O(1) |

---

# Common Mistakes

## Forgetting array must be sorted

Two Sum II works because:

```text
Array is sorted
```

Without sorting, the logic breaks.

---

## Moving the wrong pointer

Wrong:

```python
sum > target

left += 1
```

Correct:

```python
sum > target

right -= 1
```

---

## Using nested loops

Many O(n²) problems become:

```text
O(n)
```

with opposite-direction pointers.

---

# Important Problems

Easy

1. Reverse String
2. Valid Palindrome
3. Two Sum II

Medium

4. Container With Most Water
5. Three Sum
6. Sort Colors

Hard

7. Trapping Rain Water

---

# Golden Rule

Whenever you hear:

```text
Sorted Array
Pair
Palindrome
Reverse
Max Area
```

Think:

```text
Opposite Direction Two Pointers
```
