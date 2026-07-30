# ArrayQueue in Python

## Overview

This project implements a First-In, First-Out (FIFO) Queue using a dynamically resizable array in Python. Rather than relying on Python's built-in collections.deque, the queue is implemented entirely from scratch to demonstrate the internal mechanics of one of the most fundamental data structures in computer science.

The implementation uses a circular array to eliminate unnecessary element shifting and supports automatic dynamic resizing to maintain both performance and memory efficiency. This project is designed for students learning Data Structures and Algorithms, software engineering, and technical interview preparation.

The repository is organized as follows:

- README.md - Explains the implementation, complexity analysis, and usage.
- array_queue.py - Contains the complete queue implementation.
- test_array_queue.py - Provides sample tests to validate the queue's behavior.

---
## Objectives

This project demonstrates the following computer science concepts:

- Queue Abstract Data Type (ADT)
- First-In, First-Out (FIFO) processing
- Constant-time front access
- Efficient enqueue and dequeue operations
- Circular array implementation for efficient indexing
- Dynamic array resizing
- Object-oriented programming in Python
- Exception handling
- Memory-efficient data structures
- Time complexity analysis
- Amortized analysis

The primary goal is to understand how a queue works internally instead of relying on Python's built-in implementations.

---
## Implementation Overview

The queue stores its elements inside a Python list that acts as a dynamic array.

Instead of shifting every element after a dequeue operation, the implementation maintains a front index (_f) that always points to the first element in the queue.

When an element is removed, the front index simply advances using modular arithmetic:

```python
self._f = (self._f + 1) % len(self._data)
```

This creates a circular array, allowing empty positions at the beginning of the array to be reused efficiently.

Whenever the array becomes full, its capacity is doubled.

Whenever the number of stored elements falls below one-quarter of the current capacity, the array shrinks to half its size.

This strategy minimizes both memory usage and the number of expensive resizing operations.

---
## Time Complexity

|Operation| Complexity|
---------------------
|enqueue()|	O(1) amortized\
|dequeue()|	O(1) amortized|
|first()|	O(1)| is_empty()	O(1)|
|len(queue)|	O(1)|

Hello
