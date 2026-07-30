# ArrayQueue in Python

## Overview

This project implements a First-In, First-Out (FIFO) Queue using a dynamically resizable array in Python. Rather than relying on Python's built-in collections.deque, the queue is implemented entirely from scratch to demonstrate the internal mechanics of one of the most fundamental data structures in computer science.

The implementation uses a circular array to eliminate unnecessary element shifting and supports automatic dynamic resizing to maintain both performance and memory efficiency. This project is designed for students learning Data Structures and Algorithms, software engineering, and technical interview preparation.

The repository is organized as follows:

- README.md - Explains the implementation, complexity analysis, and usage.
- ArrayQueue.py - Contains the complete queue implementation.
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

| Operation | Complexity |
|-----------|------------|
| enqueue() |	O(1) amortized |
| dequeue() |	O(1) amortized |
| first() |	O(1) | 
| is_empty() | O(1) |
| len(queue)|	O(1)|

## Why Enqueue is O(1) Amortized

Most enqueue operations simply place a new element into the next available position in the array.

Only when the array becomes completely full does the implementation allocate a larger array and copy the existing elements into it. This resizing operation requires O(n) time.

However, because the array capacity doubles after each resize, many future enqueue operations occur before another resize is necessary.

As a result, although an occasional insertion is expensive, the average cost over a sequence of enqueue operations remains O(1).

## Why Dequeue is O(1) Amortized

A typical dequeue operation performs only four constant-time steps:

1. Retrieve the front element.
2. Replace the removed position with None.
3. Advance the front index.
4. Decrease the queue size.

These operations are all O(1).

Occasionally, after many dequeue operations, the queue occupies only a small portion of the allocated array. When the number of elements becomes less than one-quarter of the current capacity, the implementation allocates a smaller array and copies the remaining elements.

Although this resizing operation requires O(n) time, it occurs only after many dequeue operations.

Therefore, the average running time of dequeue remains O(1) when analyzed over a long sequence of operations.

## What Does "Amortized" Mean?

Amortized analysis measures the average cost of an operation across a long sequence of operations instead of focusing on the occasional expensive operation.

Although one enqueue operation temporarily costs O(n) because every element must be copied into a larger array, that expensive operation is spread across many future enqueue operations.

The same principle applies to dequeue(). Shrinking the array occasionally requires copying elements, but because shrinking occurs only after many removals, the average cost of each dequeue operation remains O(1).

This is why both enqueue and dequeue are said to run in O(1) amortized time rather than strict O(1) worst-case time.

## Space Complexity

| Resource | Complexity |
|----------|------------|
| Queue Storage |	O(n) |

The queue stores only the elements currently contained in the data structure, along with a small amount of additional capacity reserved for future growth.

## Design Decisions

Several implementation choices improve both performance and maintainability:

- Circular indexing avoids shifting elements after every dequeue.
- Dynamic expansion doubles the capacity when the queue becomes full.
- Dynamic shrinking reduces unused memory when the queue becomes sparse.
- Removed elements are set to None to allow Python's garbage collector to reclaim memory.
- During resizing, elements are copied into contiguous positions and the front index is reset to zero while preserving FIFO order.

# Conclusion

The ArrayQueue implementation provides an efficient, memory-conscious, and educational example of a queue built from first principles. By combining a circular array with dynamic resizing, it achieves O(1) amortized time for both enqueue and dequeue operations while maintaining O(n) space complexity.

