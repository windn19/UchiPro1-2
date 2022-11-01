from collections import deque
from queue import Queue


# q = []
#
# q.append('eat')
# q.append('sleep')
# q.append('code')
#
# print(q)
#
# print(q.pop(0))

# q = deque()
# q.append('eat')
# q.append('sleep')
# q.append('code')
# print(q)
# for _ in range(len(q)):
#     print(q.popleft())
#
# print(q.popleft())

q = Queue()

q.put('eat')
q.put('sleep')
q.put('code')

print(q)

for _ in range(q.qsize()):
    print(q.get())
