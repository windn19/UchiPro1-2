# my_stack = []
#
# my_stack.append('a')
# my_stack.append('b')
# my_stack.append('c')
#
# print(my_stack)
#
# for _ in range(len(my_stack)):
#     print(my_stack.pop())

# from collections import deque
#
# my_stack = deque()
#
# my_stack.append('a')
# my_stack.append('b')
# my_stack.append('c')
#
# print(my_stack)
#
# for _ in range(len(my_stack)):
#     print(my_stack.pop())

from queue import LifoQueue

my_stack = LifoQueue()

my_stack.put('a')
my_stack.put('b')
my_stack.put('c')

print(my_stack)

for _ in range(my_stack.qsize()):
    print(my_stack.get())
