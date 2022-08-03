from collections import deque
"""
499
57 45 62 70 33 90 88 76 100 50
"""
food_amount = int(input())
line = deque()
orders = input()

orders = orders.split()
for i in range(len(orders)):
    line.append(int(orders[i]))

print(max(line))
while line:
    if food_amount - line[0] <= 0:
        break
    else:
        food_amount -= line.popleft()

if food_amount - line[0] <= 0:
    print("Orders left:",*line, sep=' ')

else:
    print("Orders complete")

