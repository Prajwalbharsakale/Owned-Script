# Pattern Recognition

---

# Introduction

Beginners think:

```
Problem → Solution
```

Experienced programmers think:

```
Problem → Pattern → Solution
```

The goal is NOT to memorize 500 problems.

The goal is to recognize:

- HashMap pattern
- Two Pointer pattern
- Sliding Window pattern
- Binary Search pattern
- Stack pattern
- Heap pattern
- DFS/BFS pattern
- Dynamic Programming pattern

Once you identify the pattern, writing the code becomes easy.

---

# Step 1: Read the Problem Carefully

Ask:

1. What is the input?
2. What is the output?
3. Are duplicates allowed?
4. Is the array sorted?
5. Do we need all combinations?
6. Are we looking for the maximum or minimum?
7. Are we searching for a pair?
8. Are we dealing with contiguous subarrays?
9. Are we repeatedly calculating something?
10. Are there overlapping subproblems?

---

# Pattern 1: Brute Force

Always start with brute force.

Example:

Two Sum

```python
for i in range(n):
    for j in range(i+1,n):
        if nums[i] + nums[j] == target:
            return [i,j]
```

Complexity:

```
Time = O(n²)
Space = O(1)
```

---

# Pattern 2: HashMap

### Keywords

- Frequency
- Count
- Duplicate
- Pair lookup
- Fast search

### Questions

Can I store something?

Can I trade memory for speed?

### Examples

- Two Sum
- Contains Duplicate
- Valid Anagram
- Group Anagrams
- Top K Frequent Elements

### Complexity

```
Time = O(n)
Space = O(n)
```

---

## Example

Brute Force:

```python
for i in range(n):
    for j in range(i+1,n):
```

O(n²)

HashMap:

```python
store numbers already seen
```

O(n)

---

# Pattern 3: Two Pointers

### Keywords

- Pair
- Sorted array
- Remove duplicates
- Move elements
- Reverse array

### Types

### Same Direction

```
slow ---->
fast ---->
```

Examples:

- Move Zeroes
- Remove Duplicates

---

### Opposite Direction

```
left ---->

<---- right
```

Examples:

- Two Sum II
- Container With Most Water

---

### Fast and Slow Pointer

```
slow --->

fast -------->
```

Examples:

- Linked List Cycle
- Middle Node

---

### Complexity

```
Time = O(n)

Space = O(1)
```

---

# Pattern 4: Sliding Window

### Keywords

- Contiguous
- Subarray
- Substring
- Longest
- Shortest
- Maximum sum

### Fixed Size Window

Example:

Maximum sum of size k.

```python
window_size = k
```

---

### Variable Size Window

Example:

Longest substring without repeating characters.

Window expands and shrinks.

---

### Examples

- Maximum Average Subarray
- Longest Repeating Character Replacement
- Minimum Window Substring

---

### Complexity

```
Time = O(n)
Space = O(1) or O(n)
```

---

# Pattern 5: Prefix Sum

### Keywords

- Range sum
- Repeated sums
- Subarray sum

### Idea

Store previous sums.

Instead of:

```
sum every time
```

Use:

```
prefix[right]-prefix[left]
```

---

### Examples

- Range Sum Query
- Subarray Sum Equals K

---

### Complexity

```
Time = O(n)
Space = O(n)
```

---

# Pattern 6: Binary Search

### Keywords

- Sorted array
- Search
- Minimize
- Maximize
- Find first
- Find last

### Examples

- Binary Search
- Search Insert Position
- Search Rotated Array

---

### Complexity

```
Time = O(log n)
Space = O(1)
```

---

# Pattern 7: Stack

### Keywords

- Parentheses
- Undo
- Previous greater
- Next greater
- Monotonic

### Examples

- Valid Parentheses
- Daily Temperatures
- Next Greater Element

---

### Complexity

```
Time = O(n)
Space = O(n)
```

---

# Pattern 8: Queue

### Keywords

- Level by level
- BFS
- Shortest path

### Examples

- Binary Tree Level Order Traversal
- Rotting Oranges

---

### Complexity

```
Time = O(n)
Space = O(n)
```

---

# Pattern 9: Heap

### Keywords

- Top K
- Largest
- Smallest
- Priority

### Examples

- Kth Largest Element
- Top K Frequent Elements

---

### Complexity

```
Insertion = O(log n)

Deletion = O(log n)
```

---

# Pattern 10: Recursion

### Keywords

- Tree
- Divide and conquer

### Examples

- Factorial
- Fibonacci
- Tree Traversals

---

# Pattern 11: Backtracking

### Keywords

- All combinations
- All subsets
- Permutations

### Examples

- Subsets
- Permutations
- Combination Sum
- N Queens

---

### Complexity

Usually:

```
O(2ⁿ)
```

or

```
O(n!)
```

---

# Pattern 12: Greedy

### Keywords

- Local optimum
- Minimum jumps
- Intervals

### Examples

- Jump Game
- Gas Station
- Merge Intervals

---

### Complexity

Usually:

```
O(n)
```

---

# Pattern 13: Trees

### Keywords

- Hierarchy
- Parent-child

### DFS

```python
Preorder
Inorder
Postorder
```

### BFS

Level Order Traversal

---

### Examples

- Maximum Depth
- Same Tree
- Invert Binary Tree

---

### Complexity

```
Time = O(n)

Space = O(h)
```

---

# Pattern 14: Graphs

### Keywords

- Network
- Connected
- Shortest path

### DFS

Depth First Search

### BFS

Breadth First Search

---

### Examples

- Number of Islands
- Clone Graph

---

### Complexity

```
O(V+E)
```

---

# Pattern 15: Dynamic Programming

### Keywords

- Maximum
- Minimum
- Count ways
- Overlapping subproblems

### Examples

- House Robber
- Coin Change
- Climbing Stairs
- LIS

---

### Complexity

Usually

```
O(n)
```

or

```
O(n²)
```

---

# Pattern Recognition Table

| Problem Clue | Pattern |
|--------------|---------|
| Frequency Count | HashMap |
| Pair in Sorted Array | Two Pointers |
| Contiguous Subarray | Sliding Window |
| Range Sum | Prefix Sum |
| Search Sorted Array | Binary Search |
| Parentheses | Stack |
| Level by Level | Queue/BFS |
| Top K | Heap |
| All Combinations | Backtracking |
| Hierarchy | Trees |
| Network | Graph |
| Overlapping Subproblems | Dynamic Programming |

---

# Pattern Learning Order

### Phase 1

Arrays

HashMap

Strings

---

### Phase 2

Two Pointers

Sliding Window

Prefix Sum

---

### Phase 3

Stack

Queue

Linked List

---

### Phase 4

Binary Search

Heap

Recursion

---

### Phase 5

Trees

BST

Trie

---

### Phase 6

Graphs

Union Find

Topological Sort

---

### Phase 7

Greedy

Backtracking

Dynamic Programming

---

# Golden Rule

Don't ask:

```
Have I seen this problem before?
```

Ask:

```
Which pattern does this problem belong to?
```

Because

```
Patterns > Problems
```

Master 20 patterns and you can solve thousands of problems.
