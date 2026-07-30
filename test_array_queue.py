from ArrayQueue import ArrayQueue

queue = ArrayQueue()
queue.enqueue("Alice")
queue.enqueue("Bob")
queue.enqueue("Charlie")
print(queue.first()) # Alice 
print(queue.dequeue()) # Alice 
print(queue.dequeue()) # Bob 
queue.enqueue("David") 
print(len(queue)) # 2
