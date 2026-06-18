# How To Think While Solving Problems

---

# Introduction

Most people try to memorize solutions.

Strong problem solvers do something different:

```
Problem
↓
Understand
↓
Brute Force
↓
Analyze
↓
Find Bottleneck
↓
Optimize
↓
Recognize Pattern
↓
Code
```

Never think:

```
Problem
↓
Remember Solution
↓
Code
```

That approach eventually fails.

---

# Golden Rule

Don't memorize code.

Memorize:

- Patterns
- Intuition
- Complexity
- Tradeoffs

Code can always be rebuilt.

---

# Step 1: Understand the Problem

Before writing code, ask:

### What is the input?

```python
nums = [2,7,11,15]
target = 9
```

### What is the output?

```python
[0,1]
```

### Constraints

```text
1 <= n <= 10^5
```

### Can numbers be negative?

### Can duplicates exist?

### Is the array sorted?

### What should I return?

---

# Step 2: Become the Computer

Solve manually.

Example:

```python
nums = [2,7,11,15]
target = 9
```

Human thinking:

```
2 + 7 = 9
```

Answer:

```python
[0,1]
```

Always solve with paper first.

---

# Step 3: Write Brute Force

Never jump to the optimal solution.

Bad:

```
Problem
↓
HashMap
↓
Code
```

Good:

```
Problem
↓
Brute Force
↓
Optimization
```

---

Example:

Two Sum

```python
for i in range(n):
    for j in range(i+1,n):
        if nums[i]+nums[j]==target:
            return [i,j]
```

Complexity:

```
O(n²)
```

---

# Step 4: Find the Bottleneck

Ask:

Where is time being wasted?

Example:

```python
for i in range(n):
    for j in range(n):
```

Problem:

```
Repeated searching
```

Cost:

```
O(n²)
```

Question:

Can we search faster?

Answer:

HashMap.

---

# Optimization Questions

These questions are extremely important.

---

## Question 1

Can I trade memory for speed?

Usually:

```
HashMap
HashSet
```

Example:

Two Sum

```
O(n²)
```

↓

```
O(n)
```

---

## Question 2

Is the array sorted?

Think:

- Binary Search
- Two Pointers

---

## Question 3

Do I need a pair?

Think:

```
Two Pointers
HashMap
```

---

## Question 4

Do I need frequency count?

Think:

```
Dictionary
Counter
HashMap
```

---

## Question 5

Am I recalculating something repeatedly?

Think:

```
Prefix Sum
Dynamic Programming
```

---

## Question 6

Do I need maximum or minimum?

Think:

```
Heap
Sliding Window
DP
Greedy
```

---

## Question 7

Is this contiguous?

Words:

```
Subarray
Substring
Continuous
```

Think:

```
Sliding Window
Prefix Sum
```

---

## Question 8

Need Top K?

Think:

```
Heap
Priority Queue
```

---

## Question 9

Need all combinations?

Think:

```
Backtracking
```

---

## Question 10

Problem size reduced by half?

Think:

```
Binary Search
```

---

# General Optimization Path

Almost every problem follows:

```
Built-in Functions
↓
Manual Solution
↓
Brute Force
↓
Extra Array
↓
HashMap
↓
Two Pointers
↓
Sliding Window
↓
Binary Search
↓
Heap
↓
Greedy
↓
Dynamic Programming
```

---

# Approach 1: Built-in Functions

Example:

Largest element

```python
max(nums)
```

Easy.

But interviewers usually expect manual implementation.

---

# Approach 2: Manual Loop

```python
largest = nums[0]

for num in nums:
    if num > largest:
        largest = num
```

---

# Approach 3: Nested Loops

Most brute force solutions use:

```python
for i in range(n):
    for j in range(n):
```

Complexity:

```
O(n²)
```

---

# Approach 4: Extra Array

Trade memory for speed.

Example:

Move Zeroes

```python
non_zero = []

for num in nums:
    if num != 0:
        non_zero.append(num)
```

Complexity:

```
Time = O(n)

Space = O(n)
```

---

# Approach 5: HashMap

Store information.

Example:

Two Sum

Instead of searching repeatedly.

Store:

```python
value → index
```

Complexity:

```
Time = O(n)

Space = O(n)
```

---

# Approach 6: Two Pointers

Example:

Move Zeroes

```text
i
↓

4 2 0 1 8 0
    ↑
    j
```

Complexity:

```
Time = O(n)

Space = O(1)
```

---

# Approach 7: Sliding Window

Instead of recalculating every subarray.

Move boundaries.

```text
left----right
```

Complexity:

```
O(n)
```

---

# Approach 8: Binary Search

Reduce search space by half.

Example:

```
1 2 3 4 5 6 7 8
```

Middle:

```
4
```

Discard half.

Complexity:

```
O(log n)
```

---

# Approach 9: Stack

Useful when we need:

- Previous Greater
- Next Greater
- Parentheses

Examples:

- Valid Parentheses
- Daily Temperatures

Complexity:

```
O(n)
```

---

# Approach 10: Queue

Useful for:

- BFS
- Level order traversal

Complexity:

```
O(n)
```

---

# Approach 11: Heap

Useful for:

- Top K elements
- Priority based problems

Complexity:

```
Insertion = O(log n)
```

---

# Approach 12: Greedy

Take best choice now.

Examples:

- Jump Game
- Gas Station

Complexity:

Usually:

```
O(n)
```

---

# Approach 13: Recursion

Break problem into smaller problems.

Example:

```python
factorial(5)

5 × factorial(4)
```

---

# Approach 14: Backtracking

Try every possibility.

Examples:

- Subsets
- Permutations

Complexity:

```
O(2^n)
```

or

```
O(n!)
```

---

# Approach 15: Dynamic Programming

Reuse previous answers.

Examples:

- House Robber
- Coin Change
- LIS

---

# Dry Run Every Solution

Never trust code.

Example:

```python
nums=[4,2,0,1,8,0]
```

Trace:

```text
i=0
j=1

4 2 0 1 8 0

i=2
j=3

4 2 0 1 8 0

swap

4 2 1 0 8 0

swap

4 2 1 8 0 0
```

Dry runs find most bugs.

---

# Learn Complexity Automatically

Whenever you see code, ask:

### How many times does each loop run?

Single loop:

```
O(n)
```

Nested loop:

```
O(n²)
```

Divide by 2:

```
O(log n)
```

Two pointers:

```
O(n)
```

Sort:

```
O(n log n)
```

---

# Common Mistakes

## Memorizing Code

Wrong.

Memorize:

- Pattern
- Intuition
- Complexity

---

## Ignoring Constraints

```text
n = 100
```

O(n²) acceptable.

```text
n = 100000
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

## Coding Too Early

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
Think
↓
Brute Force
↓
Optimize
↓
Code
```

---

## Not Doing Dry Runs

Most bugs are logical.

Dry runs catch them.

---

# Interview Thinking

Interviewers are not checking:

```
Can you remember code?
```

They are checking:

1. Can you understand the problem?
2. Can you build a brute force solution?
3. Can you analyze complexity?
4. Can you optimize?
5. Can you explain your thinking?

---

# Final Formula

```text
Understand
↓
Manual Solution
↓
Brute Force
↓
Complexity Analysis
↓
Find Bottleneck
↓
Optimization
↓
Dry Run
↓
Code
↓
Edge Cases
↓
Success
```

---

# Remember

Don't try to become someone who has solved 1000 problems.

Become someone who can solve a problem they have never seen before.

Because:

```
Problem Solving > Problem Memorization
```
