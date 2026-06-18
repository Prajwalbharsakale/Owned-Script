# Time and Space Complexity

---

# Why Do We Need Complexity?

Suppose there are two solutions to the same problem.

Solution 1:

```python
for i in range(n):
    print(i)
```

Solution 2:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Both solutions are correct, but which one is better?

Instead of measuring execution time in seconds (which depends on hardware), we measure how the running time grows with input size.

This is called **Time Complexity**.

---

# Types of Complexity

1. Time Complexity
2. Space Complexity

---

# Time Complexity

Time Complexity tells us how many operations an algorithm performs as the input size increases.

It does NOT represent actual time in seconds.

Example:

```python
for i in range(n):
    print(i)
```

For:

n = 5

The loop runs:

```
0
1
2
3
4
```

Total operations = 5

Therefore:

```
Time Complexity = O(n)
```

---

# Space Complexity

Space Complexity tells us how much extra memory an algorithm uses.

Example:

```python
sum = 0

for num in nums:
    sum += num
```

Only one variable is used.

Therefore:

```
Space Complexity = O(1)
```

---

# Big O Notation

Big O represents the worst-case growth of an algorithm.

Common complexities:

```
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
O(n³)
O(2ⁿ)
O(n!)
```

As input size increases:

```
Best
O(1)
↓
O(log n)
↓
O(n)
↓
O(n log n)
↓
O(n²)
↓
O(n³)
↓
O(2ⁿ)
↓
Worst
```

---

# O(1) Constant Time

The number of operations remains constant.

Example:

```python
a = [4,2,7,1]

print(a[2])
```

Only one operation.

Regardless of array size:

```
Time Complexity = O(1)
```

Examples:

- Accessing an element by index
- Stack push
- Stack pop
- HashMap lookup (average)

---

# O(n) Linear Time

Number of operations grows proportionally with n.

Example:

```python
for i in range(n):
    print(i)
```

For:

n = 5

Operations:

```
5
```

For:

n = 100

Operations:

```
100
```

Therefore:

```
O(n)
```

---

# O(n²)

Example:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

For:

n = 3

Iterations:

```
(0,0)
(0,1)
(0,2)

(1,0)
(1,1)
(1,2)

(2,0)
(2,1)
(2,2)
```

Total:

```
3 × 3 = 9
```

Therefore:

```
Time Complexity = O(n²)
```

---

# O(n³)

Example:

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)
```

Total operations:

```
n × n × n
```

Therefore:

```
O(n³)
```

---

# O(log n)

When the problem size gets reduced by half each time.

Example:

```python
while n > 1:
    n = n // 2
```

Suppose:

```
n = 16
```

Iterations:

```
16
8
4
2
1
```

Only 5 steps.

Therefore:

```
O(log n)
```

Examples:

- Binary Search
- Heap operations

---

# O(n log n)

Combination of:

```
n work
```

performed

```
log n times
```

Examples:

- Merge Sort
- Heap Sort
- Quick Sort (average)

Therefore:

```
O(n log n)
```

---

# O(2ⁿ)

Example:

Fibonacci recursion:

```python
fib(n):
    fib(n-1)
    fib(n-2)
```

The recursion tree grows exponentially.

Therefore:

```
O(2ⁿ)
```

Very inefficient.

---

# O(n!)

Example:

Generating all permutations.

```python
ABC

ABC
ACB
BAC
BCA
CAB
CBA
```

For:

```
n = 3
```

Permutations:

```
3! = 6
```

Therefore:

```
Time Complexity = O(n!)
```

---

# Multiple Loops

Example:

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)
```

Operations:

```
n + n
```

Which becomes:

```
2n
```

Ignoring constants:

```
O(n)
```

---

# Nested Loops

Example:

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

Operations:

```
n × n
```

Therefore:

```
O(n²)
```

---

# Different Variables

Example:

```python
for i in range(n):
    print(i)

for j in range(m):
    print(j)
```

Operations:

```
n + m
```

Therefore:

```
O(n + m)
```

---

# Nested Different Variables

Example:

```python
for i in range(n):
    for j in range(m):
        print(i, j)
```

Operations:

```
n × m
```

Therefore:

```
O(nm)
```

---

# Ignoring Constants

Example:

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)

for k in range(n):
    print(k)
```

Operations:

```
3n
```

Big O ignores constants.

Therefore:

```
O(n)
```

---

# Space Complexity

## O(1)

Example:

```python
largest = nums[0]
```

Only one variable.

```
Space Complexity = O(1)
```

---

## O(n)

Example:

```python
result = []

for num in nums:
    result.append(num)
```

The new list stores n elements.

Therefore:

```
Space Complexity = O(n)
```

---

## O(n²)

Example:

```python
matrix = [[0]*n for _ in range(n)]
```

Memory used:

```
n²
```

Therefore:

```
Space Complexity = O(n²)
```

---

# Best, Average and Worst Case

## Best Case

Minimum operations required.

## Average Case

Expected operations.

## Worst Case

Maximum operations.

Big O usually represents the worst case.

---

# Competitive Programming Constraints

| Input Size | Expected Complexity |
|------------|--------------------|
| n ≤ 10 | O(n³) |
| n ≤ 100 | O(n²) |
| n ≤ 10³ | O(n²) |
| n ≤ 10⁵ | O(n log n) or O(n) |
| n ≤ 10⁶ | O(n) |
| n ≤ 10⁹ | O(log n) |

---

# Interview Tips

Whenever you see a problem, ask:

1. How many times does each loop run?
2. Are loops nested or separate?
3. Is the input reduced by half each time?
4. Am I using extra memory?
5. Can I improve from O(n²) to O(n)?

These five questions should become automatic.
