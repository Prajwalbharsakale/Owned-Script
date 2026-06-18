# Complexity Cheat Sheet

---

# Big O Hierarchy

From fastest to slowest:

```text
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
O(n!)
```

---

# O(1) — Constant Time

### Meaning

Execution time does not depend on input size.

### Examples

#### Access array element

```python
nums[5]
```

#### Stack push

```python
stack.append(x)
```

#### Stack pop

```python
stack.pop()
```

#### HashMap lookup (average)

```python
d[key]
```

### Space

```text
O(1)
```

---

# O(log n) — Logarithmic Time

### Meaning

Problem size gets reduced by half each step.

### Example

```python
while n > 1:
    n = n // 2
```

Example:

```text
16
8
4
2
1
```

Only 5 operations.

---

## Examples

### Binary Search

```python
while low <= high:
    mid = (low+high)//2
```

### Heap Push

```python
heapq.heappush(heap,x)
```

### Heap Pop

```python
heapq.heappop(heap)
```

---

# O(n) — Linear Time

### Meaning

Work grows proportionally with input size.

### Example

```python
for i in range(n):
    print(i)
```

---

## Examples

### Traverse array

```python
for num in nums:
```

### Frequency count

```python
for num in nums:
    freq[num]+=1
```

### Sliding window

```python
left=0

for right in range(n):
```

### Two pointers

```python
while i<n and j<n:
```

---

# O(n log n)

### Meaning

Perform O(log n) work for each element.

---

## Examples

### Merge Sort

```python
O(n log n)
```

### Heap Sort

```python
O(n log n)
```

### Quick Sort Average

```python
O(n log n)
```

### Python sort()

```python
nums.sort()
```

---

# O(n²)

### Meaning

Nested loops.

### Example

```python
for i in range(n):
    for j in range(n):
```

---

## Examples

### Bubble Sort

```python
O(n²)
```

### Selection Sort

```python
O(n²)
```

### Insertion Sort

Worst Case:

```python
O(n²)
```

### Brute Force Two Sum

```python
O(n²)
```

---

# O(n³)

Three nested loops.

Example:

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
```

---

# O(2ⁿ)

Exponential growth.

Example:

Recursive Fibonacci

```python
fib(n)

fib(n-1)
fib(n-2)
```

---

# O(n!)

Example:

Permutations.

```python
ABC

ABC
ACB
BAC
BCA
CAB
CBA
```

---

# Loop Complexity

---

## Single Loop

```python
for i in range(n):
```

Complexity:

```text
O(n)
```

---

## Two Loops

```python
for i in range(n):
    ...

for j in range(n):
    ...
```

Operations:

```text
n+n
```

Result:

```text
O(n)
```

---

## Nested Loops

```python
for i in range(n):
    for j in range(n):
```

Operations:

```text
n×n
```

Result:

```text
O(n²)
```

---

## Three Nested Loops

```python
for i in range(n):
    for j in range(n):
        for k in range(n):
```

Result:

```text
O(n³)
```

---

## Different Variables

```python
for i in range(n):
    ...

for j in range(m):
    ...
```

Result:

```text
O(n+m)
```

---

## Nested Different Variables

```python
for i in range(n):
    for j in range(m):
```

Result:

```text
O(nm)
```

---

# While Loop

```python
i=0

while i<n:
    i+=1
```

Complexity:

```text
O(n)
```

---

# Divide By Two

```python
while n>1:
    n//=2
```

Complexity:

```text
O(log n)
```

---

# Multiply By Two

```python
i=1

while i<n:
    i*=2
```

Complexity:

```text
O(log n)
```

---

# Recursion Complexity

---

## Factorial

```python
factorial(n)

factorial(n-1)
```

Complexity:

```text
O(n)
```

---

## Fibonacci

```python
fib(n)

fib(n-1)
fib(n-2)
```

Complexity:

```text
O(2ⁿ)
```

---

# Sorting Complexities

| Algorithm | Best | Average | Worst | Space |
|------------|------|---------|-------|------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |

---

# Searching Complexities

| Operation | Complexity |
|-----------|-----------|
| Linear Search | O(n) |
| Binary Search | O(log n) |
| HashMap Lookup | O(1) average |
| HashMap Lookup Worst | O(n) |

---

# Data Structure Complexities

## Array

| Operation | Complexity |
|-----------|-----------|
| Access | O(1) |
| Search | O(n) |
| Insert End | O(1) |
| Insert Beginning | O(n) |
| Delete End | O(1) |
| Delete Beginning | O(n) |

---

## Stack

| Operation | Complexity |
|-----------|-----------|
| Push | O(1) |
| Pop | O(1) |
| Peek | O(1) |

---

## Queue

| Operation | Complexity |
|-----------|-----------|
| Enqueue | O(1) |
| Dequeue | O(1) |

---

## Heap

| Operation | Complexity |
|-----------|-----------|
| Peek | O(1) |
| Insert | O(log n) |
| Delete | O(log n) |

---

# Pattern Complexities

| Pattern | Time | Space |
|---------|------|------|
| Brute Force | O(n²) | O(1) |
| HashMap | O(n) | O(n) |
| Two Pointers | O(n) | O(1) |
| Sliding Window | O(n) | O(1) |
| Prefix Sum | O(n) | O(n) |
| Binary Search | O(log n) | O(1) |
| Stack | O(n) | O(n) |
| Queue | O(n) | O(n) |
| Heap | O(n log k) | O(k) |
| DFS | O(V+E) | O(V) |
| BFS | O(V+E) | O(V) |
| Union Find | O(α(n)) |
| Dynamic Programming | O(n) to O(n²) |

---

# Space Complexity

---

## O(1)

Only variables.

```python
largest = nums[0]
```

---

## O(n)

Extra array.

```python
result=[]
```

Dictionary.

```python
freq={}
```

Set.

```python
visited=set()
```

---

## O(n²)

Matrix.

```python
matrix=[[0]*n for _ in range(n)]
```

---

# Constraint Cheat Sheet

| n | Expected Complexity |
|---|---|
| 10 | O(n!) |
| 20 | O(2ⁿ) |
| 100 | O(n³) |
| 1000 | O(n²) |
| 100000 | O(n log n) |
| 1000000 | O(n) |
| 1000000000 | O(log n) |

---

# Golden Questions

Whenever you see code ask:

1. How many times does each loop run?
2. Are loops nested?
3. Is input reduced by half?
4. Is extra memory used?
5. Are two pointers moving only forward?
6. Is sorting involved?

Answering these questions automatically gives the complexity.
