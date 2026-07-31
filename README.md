# Array Queue In Python

## Overview

An **Array Queue** is a queue data structure that stores elements in an array (or list) and follows the **First-In, First-Out (FIFO)** principle. This means the first element added to the queue is the first one removed.

Python already provides queue implementations, such as `collections.deque`, which are optimized for real-world applications. In this project, however, the queue is implemented **from scratch** to demonstrate how a queue works internally instead of relying on Python's built-in data structures.

This implementation uses a **circular array**, meaning that when the end of the array is reached, the queue wraps around and reuses the empty positions at the beginning. This eliminates unnecessary element shifting and improves performance. The array also grows automatically when it becomes full and shrinks when it becomes mostly empty to use memory efficiently.

Array queues are commonly used in many software systems, including:

* **Print servers** to process print jobs in order.
* **Web servers** to handle incoming client requests.
* **Customer support systems** to manage support tickets.
* **Task schedulers** to execute background jobs.
* **Message queue systems** such as RabbitMQ, Apache Kafka, and Amazon SQS for communication between services.

The repository is organized as follows:

* **README.md** – Project documentation, implementation details, and complexity analysis.
* **ArrayQueue.py** – Complete implementation of the Array Queue.
* **test_array_queue.py** – Sample test cases for validating the queue operations.

---

## Objectives

The goal of this project is to understand how an **Array Queue** works by implementing it from scratch in Python. Instead of using Python's built-in queue classes, this implementation focuses on the core concepts behind the data structure.

By completing this project, you will learn:

* How a FIFO (First-In, First-Out) queue works.
* How a circular array improves performance.
* How dynamic resizing manages memory efficiently.
* Why enqueue and dequeue operations run in **O(1) amortized** time.
* How object-oriented programming can be used to build data structures.

---

## Implementation Overview

The queue stores its elements inside a Python list that acts as a dynamic array.

A variable named `_f` keeps track of the front of the queue. Instead of moving every element after a `dequeue()`, the front index simply moves to the next position.

```python
self._f = (self._f + 1) % len(self._data)
```

The modulo operator (`%`) allows the index to wrap around to the beginning of the array when it reaches the end. This creates a **circular array**, which avoids unnecessary element shifting.

The queue also resizes itself automatically:

* The array **doubles** when it becomes full.
* The array **shrinks to half** when it is less than one-quarter full.

This approach provides good performance while using memory efficiently.

---

## Time Complexity

| Operation    | Complexity         |
| ------------ | ------------------ |
| `enqueue()`  | **O(1) amortized** |
| `dequeue()`  | **O(1) amortized** |
| `first()`    | **O(1)**           |
| `is_empty()` | **O(1)**           |
| `len(queue)` | **O(1)**           |

---

## Why Are `enqueue()` and `dequeue()` O(1) Amortized?

Most `enqueue()` operations simply insert a new element into the next available position. Likewise, most `dequeue()` operations remove the front element and move the front index to the next position. These operations take constant time.

Sometimes, however, the queue must resize its underlying array:

* When the array becomes full, a larger array is created and all elements are copied into it.
* When the queue becomes mostly empty, a smaller array is created and the remaining elements are copied.

These resize operations take **O(n)** time because every element must be copied.

Fortunately, resizing happens only occasionally. Between two resize operations, many enqueue and dequeue operations run in constant time. When the total cost is averaged over all operations, both **enqueue()** and **dequeue()** have an **O(1) amortized** running time.

---

## What Does "Amortized" Mean?

**Amortized analysis** measures the average cost of an operation over a long sequence of operations.

For example, one `enqueue()` may take **O(n)** when the array grows, but hundreds of other enqueue operations will take only **O(1)** before another resize is needed.

The same idea applies to `dequeue()`. Shrinking the array requires copying elements, but it happens only after many removals.

For this reason, the average running time of both operations is **O(1) amortized**, even though a few individual operations may temporarily take **O(n)**.

---

## Space Complexity

| Resource      | Complexity |
| ------------- | ---------- |
| Queue Storage | **O(n)**   |

The queue stores only the current elements and a small amount of extra space for future growth.

---

## Design Decisions

This implementation includes several design choices to improve performance and memory usage:

* A **circular array** avoids shifting elements after each dequeue.
* **Dynamic expansion** doubles the array size when it becomes full.
* **Dynamic shrinking** reduces memory usage when the queue becomes mostly empty.
* Removed elements are replaced with `None` so Python can reclaim unused memory.
* During resizing, the queue is copied into a new array while preserving the correct FIFO order.

---

## Conclusion

This project demonstrates how to build an **Array Queue** from scratch using a circular array and dynamic resizing. These techniques provide efficient memory usage and allow both `enqueue()` and `dequeue()` to run in **O(1) amortized** time while maintaining an overall space complexity of **O(n)**.

Although Python provides built-in queue implementations, understanding how they work internally is an important step toward mastering data structures and algorithm design.
