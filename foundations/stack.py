from collections import deque

# queue definition
queue = deque()

for i in range(4) :
    queue.append(i+1)

print(queue)

left = queue.popleft()

print(left)
print(queue)

# Stack definition

stack = []

for i in range(4):
    stack.append(i+1)

print("Here is the stack: ", stack)

last = stack.pop()

print(last)
print(stack)

