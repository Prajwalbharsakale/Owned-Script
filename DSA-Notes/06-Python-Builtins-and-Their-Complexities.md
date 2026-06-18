# Python Built-ins and Their Complexities

---

# Introduction

Knowing Python built-ins and their complexities is extremely important for:

- LeetCode
- Competitive Programming
- Product Company Interviews

Always ask:

1. What is the complexity?
2. Can I do better?
3. Is there a hidden O(n)?

---

# List Operations

```python
nums = [1,2,3]
```

---

## append()

```python
nums.append(4)
```

Adds element at the end.

### Time Complexity

Average:

```text
O(1)
```

Worst:

```text
O(n)
```

(when resizing happens)

### Space Complexity

```text
O(1)
```

---

## pop()

### pop from end

```python
nums.pop()
```

Time:

```text
O(1)
```

---

### pop from beginning

```python
nums.pop(0)
```

Time:

```text
O(n)
```

Because all elements shift left.

---

## insert()

```python
nums.insert(0,100)
```

Time:

```text
O(n)
```

Elements must shift.

---

## remove()

```python
nums.remove(5)
```

Time:

```text
O(n)
```

First searches, then removes.

---

## index()

```python
nums.index(7)
```

Time:

```text
O(n)
```

---

## count()

```python
nums.count(3)
```

Time:

```text
O(n)
```

---

## reverse()

```python
nums.reverse()
```

Time:

```text
O(n)
```

---

## sort()

```python
nums.sort()
```

Uses Timsort.

Average:

```text
O(n log n)
```

Worst:

```text
O(n log n)
```

Space:

```text
O(n)
```

---

## sorted()

```python
sorted(nums)
```

Returns a new list.

Time:

```text
O(n log n)
```

Space:

```text
O(n)
```

---

## len()

```python
len(nums)
```

Time:

```text
O(1)
```

---

## max()

```python
max(nums)
```

Time:

```text
O(n)
```

---

## min()

```python
min(nums)
```

Time:

```text
O(n)
```

---

## sum()

```python
sum(nums)
```

Time:

```text
O(n)
```

---

# Membership Operator

## in

```python
5 in nums
```

List:

```text
O(n)
```

---

Set:

```python
5 in s
```

Time:

```text
O(1)
```

Average.

---

Dictionary:

```python
key in d
```

Time:

```text
O(1)
```

Average.

---

# Slicing

```python
nums[start:end]
```

Example:

```python
nums[2:7]
```

Copies elements.

Time:

```text
O(k)
```

where

```text
k = slice length
```

---

String slicing

```python
s[2:8]
```

Time:

```text
O(k)
```

---

# String Operations

```python
s = "hello"
```

---

## len()

```python
len(s)
```

Time:

```text
O(1)
```

---

## lower()

```python
s.lower()
```

Time:

```text
O(n)
```

---

## upper()

```python
s.upper()
```

Time:

```text
O(n)
```

---

## replace()

```python
s.replace("a","b")
```

Time:

```text
O(n)
```

---

## split()

```python
s.split()
```

Time:

```text
O(n)
```

---

## join()

```python
"".join(words)
```

Time:

```text
O(n)
```

Very efficient.

---

## String concatenation

```python
result += ch
```

Time:

```text
O(n)
```

inside loop may become

```text
O(n²)
```

Avoid.

Prefer:

```python
arr.append(ch)

"".join(arr)
```

---

# Set Operations

```python
s = {1,2,3}
```

---

## add()

```python
s.add(5)
```

Time:

```text
O(1)
```

Average.

---

## remove()

```python
s.remove(2)
```

Time:

```text
O(1)
```

Average.

---

## discard()

```python
s.discard(2)
```

Time:

```text
O(1)
```

---

## Membership

```python
5 in s
```

Time:

```text
O(1)
```

Average.

---

# Dictionary Operations

```python
d = {}
```

---

## Insert

```python
d[key]=value
```

Time:

```text
O(1)
```

Average.

---

## Lookup

```python
d[key]
```

Time:

```text
O(1)
```

Average.

---

## Delete

```python
del d[key]
```

Time:

```text
O(1)
```

Average.

---

## get()

```python
d.get(key)
```

Time:

```text
O(1)
```

---

## keys()

```python
d.keys()
```

Time:

```text
O(1)
```

Creating view.

---

Iterating keys

```python
for key in d:
```

Time:

```text
O(n)
```

---

# Collections.Counter

```python
from collections import Counter

freq = Counter(nums)
```

Time:

```text
O(n)
```

Space:

```text
O(n)
```

---

# collections.deque

```python
from collections import deque
```

---

## append()

```python
dq.append(x)
```

Time:

```text
O(1)
```

---

## appendleft()

```python
dq.appendleft(x)
```

Time:

```text
O(1)
```

---

## pop()

```python
dq.pop()
```

Time:

```text
O(1)
```

---

## popleft()

```python
dq.popleft()
```

Time:

```text
O(1)
```

---

### Preferred over

```python
list.pop(0)
```

which is

```text
O(n)
```

---

# Heap Operations

```python
import heapq
```

---

## heapify()

```python
heapq.heapify(nums)
```

Time:

```text
O(n)
```

---

## heappush()

```python
heapq.heappush(heap,x)
```

Time:

```text
O(log n)
```

---

## heappop()

```python
heapq.heappop(heap)
```

Time:

```text
O(log n)
```

---

## heap[0]

Peek smallest.

Time:

```text
O(1)
```

---

# enumerate()

```python
for i,val in enumerate(nums):
```

Time:

```text
O(n)
```

Space:

```text
O(1)
```

---

# zip()

```python
for a,b in zip(arr1,arr2):
```

Time:

```text
O(min(n,m))
```

---

# range()

```python
range(n)
```

Creation:

```text
O(1)
```

---

Iteration:

```python
for i in range(n)
```

Time:

```text
O(n)
```

---

# all()

```python
all(nums)
```

Time:

```text
O(n)
```

Short circuits.

---

# any()

```python
any(nums)
```

Time:

```text
O(n)
```

Short circuits.

---

# map()

```python
map(int,arr)
```

Time:

```text
O(n)
```

---

# filter()

```python
filter(func,arr)
```

Time:

```text
O(n)
```

---

# zip()

```python
zip(a,b)
```

Time:

```text
O(min(n,m))
```

---

# Complexity Table

| Operation | Complexity |
|------------|------------|
| append() | O(1) |
| pop() end | O(1) |
| pop(0) | O(n) |
| insert() | O(n) |
| remove() | O(n) |
| count() | O(n) |
| index() | O(n) |
| reverse() | O(n) |
| sort() | O(n log n) |
| len() | O(1) |
| min() | O(n) |
| max() | O(n) |
| sum() | O(n) |
| set add | O(1) |
| set lookup | O(1) |
| dict lookup | O(1) |
| Counter() | O(n) |
| heapify() | O(n) |
| heappush() | O(log n) |
| heappop() | O(log n) |
| deque appendleft() | O(1) |
| deque popleft() | O(1) |

---

# Interview Tip

Memorize these five:

```text
append()        → O(1)
pop()           → O(1)
pop(0)          → O(n)
sort()          → O(n log n)
dict/set lookup → O(1)
heap push/pop   → O(log n)
```

These alone appear in almost every coding interview.
