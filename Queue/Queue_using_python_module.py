

# How to use collection.deque as a fifo queue

from collections import deque


q = deque(maxlen=3)
# print(q)
#
# q.append(1)
# q.append(2)
# q.append(3)
# q.append(4) # removes the first element
# print(q)
#
# print(q.popleft())
# print(q)
#
# print(q.clear())
# print(q)


# Queue module to create fifo queue

import queue as q

que = q.Queue(maxsize=3)
print(que.qsize())
print(que.empty())

# enqueue
que.put(1)
que.put(2)
que.put(3)

print(que.qsize())
print(que.full())

# deque
print(que.get())

# Multiprocessing Module to implement FIFO queue

from multiprocessing import Queue

q = Queue(maxsize=3)
q.put(1)
q.put(2)
q.put(3)

print(q.get())
