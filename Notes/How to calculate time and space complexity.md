Step 1: Count How Many Times Something Runs

Forget Big O at first.

Ask:

How many times will the important operation execute?

Example:

for i in range(n):
    print(i)

Loop runs n times.

Time Complexity:

O(n)

Space Complexity:

O(1)

(no extra memory)

Single Loop
for i in range(n):
    ...

Runs:

n times

Time:

O(n)
Two Nested Loops
for i in range(n):
    for j in range(n):
        ...

Outer loop:

n

Inner loop:

n

Total:

n × n

Time:

O(n²)
Three Nested Loops
for i in range(n):
    for j in range(n):
        for k in range(n):
            ...

Total:

n × n × n

Time:

O(n³)
Loops One After Another
for i in range(n):
    ...

for j in range(n):
    ...

First loop:

n

Second loop:

n

Total:

2n

Big O ignores constants:

O(n)
Different Variables
for i in range(n):
    ...

for j in range(m):
    ...

Time:

O(n + m)
Nested with Different Variables
for i in range(n):
    for j in range(m):
        ...

Time:

O(nm)
While Loop
i = 0

while i < n:
    i += 1

Runs:

n times

Time:

O(n)
Divide by 2 Every Time
while n > 1:
    n = n // 2

Example:

16
8
4
2
1

Only 5 iterations.

Time:

O(log n)

Examples:

Binary Search
Heap operations
Multiplying by 2
i = 1

while i < n:
    i *= 2

Example:

1
2
4
8
16
...

Time:

O(log n)
Recursion
Fibonacci
fib(n):
    fib(n-1)
    fib(n-2)

Tree grows exponentially.

Time:

O(2ⁿ)

Very slow.

Merge Sort

Split in half:

log n levels

At each level:

n work

Time:

O(n log n)
Space Complexity

Look for extra memory.

No Extra Variables
a = [1,2,3]

sum = 0

Only a few variables.

Space:

O(1)
New Array
ans = []

for num in a:
    ans.append(num)

Stores n elements.

Space:

O(n)
Dictionary
freq = {}

for x in nums:
    freq[x] += 1

Worst case:

n entries

Space:

O(n)
Matrix
matrix = [[0]*n for _ in range(n)]

Stores:

n² cells

Space:

O(n²)
Two Pointers
i = 0
j = 0

while j < n:
    ...

Many beginners think:

O(n²)

because there are two pointers.

Wrong.

Each pointer moves at most n times.

Total work:

2n

Therefore:

O(n)
Sliding Window
left = 0

for right in range(n):
    while condition:
        left += 1

Looks nested.

But:

right moves n times
left moves n times

Total:

2n

Time:

O(n)
Hash Map + Loop
for x in nums:
    if x in hashmap:
        ...

Dictionary lookup is O(1).

Total:

O(n)
Sorting
nums.sort()

Python's sort:

O(n log n)
Binary Search
low = 0
high = n-1

while low <= high:
    mid = (low+high)//2

Cuts search space in half each time.

Time:

O(log n)
Competitive Programming Cheat Sheet
Pattern	Complexity
Single loop	O(n)
Two nested loops	O(n²)
Three nested loops	O(n³)
Binary Search	O(log n)
Sort	O(n log n)
Two Pointers	O(n)
Sliding Window	O(n)
Hash Map	O(n)
BFS	O(V + E)
DFS	O(V + E)
Heap Push/Pop	O(log n)
Merge Sort	O(n log n)
Quick Sort Average	O(n log n)
Quick Sort Worst	O(n²)
A useful habit

Whenever you solve a problem, always ask:

How many times can each loop/pointer move?
Am I creating extra memory?
Can I improve from O(n²) to O(n)?
What is the largest constraint?

For example:

Constraint	Expected Complexity
n ≤ 10	O(n³)
n ≤ 100	O(n²)
n ≤ 10³	O(n²)
n ≤ 10⁵	O(n log n) or O(n)
n ≤ 10⁶	O(n)
n ≤ 10⁹	O(log n)

This way of thinking is what separates beginners from strong competitive programmers.

Since you're trying to build logic and crack product companies, I'd recommend learning complexity alongside common patterns in this order:

Arrays → Two Pointers → Sliding Window → Hash Maps → Stack → Binary Search → Recursion → Trees → Graphs → Dynamic Programming.