"""
5 4 8 6 3 8 7 7 9
16
"""
from collections import deque
clothes = input().split()
stack = deque()

for x in clothes:
    stack.append(int(x))

rack_size = int(input())


counter = 0
summed = 0
while stack:
    if summed + stack[-1] <= rack_size:
        summed += stack.pop()
    else:
        summed = 0
        counter += 1
counter += 1

print(counter)

