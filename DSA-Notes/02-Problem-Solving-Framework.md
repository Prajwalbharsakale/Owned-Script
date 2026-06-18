# Problem Solving Framework

---

# Introduction

Most beginners make the same mistake:

They see a problem and immediately try to remember the optimal solution.

This is wrong.

Interviewers are not testing whether you have memorized LeetCode.

They are testing whether you can think.

The goal is:

```
Understand Problem
↓
Brute Force
↓
Analyze Complexity
↓
Find Bottleneck
↓
Optimize
↓
Recognize Pattern
↓
Reach Optimal Solution
```

---

# Step 1: Understand the Problem

Never start coding immediately.

Ask:

1. What is the input?
2. What is the output?
3. Are duplicates allowed?
4. Is the array sorted?
5. Can elements be negative?
6. What are the constraints?
7. What should be returned?

---

Example:

Two Sum

Input:

```python
nums = [2,7,11,15]
target = 9
```

Output:

```python
[0,1]
```

Meaning:

```
nums[0] + nums[1] = 9
```

---

# Step 2: Solve Manually

Before coding, solve with paper.

Example:

```
nums = [2,7,11,15]
target = 9
```

Think:

```
2 + 7 = 9
```

Answer:

```
[0,1]
```

Always become the computer first.

---

# Step 3: Find the Brute Force Solution

The first solution doesn't have to be optimal.

It only has to work.

Example:

```python
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            return [i,j]
```

Complexity:

```
Time : O(n²)
Space : O(1)
```

---

# Step 4: Analyze Complexity

Ask:

```
Can I do better?
```

Look for bottlenecks.

Example:

Nested loops:

```python
for i in range(n):
    for j in range(n):
```

Cost:

```
n × n
```

Time:

```
O(n²)
```

Question:

Can we avoid checking every pair?

---

# Step 5: Optimize

Common optimizations:

### HashMap

Convert:

```
Search → O(n)
```

to

```
Lookup → O(1)
```

---

### Two Pointers

Convert:

```
O(n²)
```

into

```
O(n)
```

---

### Sliding Window

Avoid recalculating repeatedly.

---

### Prefix Sum

Reuse previous calculations.

---

### Binary Search

Reduce search space by half.

---

### Heap

Efficient Top K problems.

---

### Dynamic Programming

Reuse already solved subproblems.

---

# Step 6: Verify the Solution

Dry run every solution.

Example:

Move Zeroes

Input:

```python
[4,2,0,1,8,0]
```

Pointer trace:

```
i
↓

4 2 0 1 8 0
    ↑
    j
```

Swap:

```
4 2 1 0 8 0
```

Continue.

---

Never skip dry runs.

---

# General Approach

Every problem should follow:

```
Understand Problem
↓
Manual Solution
↓
Brute Force
↓
Complexity Analysis
↓
Optimization
↓
Dry Run
↓
Code
↓
Test Edge Cases
```

---

# Problem Solving Hierarchy

## Level 1

Built-in functions

Example:

```python
max(nums)
```

---

## Level 2

Manual implementation

Example:

```python
largest = nums[0]

for num in nums:
    if num > largest:
        largest = num
```

---

## Level 3

Brute Force

Usually nested loops.

Complexity:

```
O(n²)
```

---

## Level 4

Extra Array

Trade memory for speed.

Complexity:

```
Time : O(n)
Space : O(n)
```

---

## Level 5

HashMap

Complexity:

```
Time : O(n)
Space : O(n)
```

Examples:

- Two Sum
- Frequency Count
- Group Anagrams

---

## Level 6

Two Pointers

Complexity:

```
Time : O(n)
Space : O(1)
```

Examples:

- Move Zeroes
- Remove Duplicates
- Container With Most Water

---

## Level 7

Sliding Window

Examples:

- Maximum Sum Subarray
- Longest Substring Without Repeating Characters

Complexity:

```
O(n)
```

---

## Level 8

Binary Search

Examples:

- Search Insert Position
- Search Rotated Array

Complexity:

```
O(log n)
```

---

## Level 9

Stack

Examples:

- Valid Parentheses
- Daily Temperatures

Complexity:

```
O(n)
```

---

## Level 10

Queue

Examples:

- BFS
- Level Order Traversal

---

## Level 11

Heap

Examples:

- K Largest Elements
- Merge K Sorted Lists

Complexity:

```
O(n log k)
```

---

## Level 12

Recursion

Examples:

- Fibonacci
- Tree Traversals

---

## Level 13

Backtracking

Examples:

- Subsets
- Permutations
- N Queens

---

## Level 14

Greedy

Examples:

- Jump Game
- Gas Station

---

## Level 15

Dynamic Programming

Examples:

- House Robber
- Coin Change
- Longest Increasing Subsequence

---

# Pattern Recognition

## Need Fast Search?

Think:

```
HashMap
HashSet
Binary Search
```

---

## Need Pair?

Think:

```
Two Pointers
HashMap
```

---

## Sorted Array?

Think:

```
Binary Search
Two Pointers
```

---

## Top K?

Think:

```
Heap
Priority Queue
```

---

## Contiguous Subarray?

Think:

```
Sliding Window
Prefix Sum
```

---

## Need Frequency Count?

Think:

```
HashMap
Counter
```

---

## Need Next Greater Element?

Think:

```
Stack
Monotonic Stack
```

---

## Need Tree Traversal?

Think:

```
DFS
BFS
Recursion
```

---

## Need Shortest Path?

Think:

```
BFS
Dijkstra
```

---

## Need All Possible Combinations?

Think:

```
Backtracking
```

---

## Overlapping Subproblems?

Think:

```
Dynamic Programming
```

---

# Common Mistakes

## Jumping Directly to Optimal Solution

Wrong:

```
Problem
↓
Code
```

Correct:

```
Problem
↓
Brute Force
↓
Optimization
↓
Code
```

---

## Ignoring Constraints

Example:

```
n ≤ 100
```

O(n²) is acceptable.

Example:

```
n ≤ 100000
```

Need:

```
O(n log n)
```

or

```
O(n)
```

---

## Not Dry Running

Most bugs are found during dry runs.

---

## Memorizing Solutions

Never memorize code.

Memorize:

- Pattern
- Intuition
- Complexity

Code can always be rebuilt.

---

# Golden Questions

Whenever you see a problem, ask:

1. Can I solve manually?
2. What is the brute force solution?
3. What is its complexity?
4. What is the bottleneck?
5. Can I use extra memory?
6. Is the array sorted?
7. Can two pointers help?
8. Can HashMap help?
9. Can Binary Search help?
10. Can I reuse previous work?

These questions are the foundation of problem solving.

---

# Ultimate Goal

Don't aim to memorize 500 solutions.

Aim to recognize patterns.

Because:

```
Patterns > Problems
```

Once patterns become natural, unseen problems become solvable.
