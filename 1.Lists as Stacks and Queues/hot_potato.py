"""
Hot potato is a game in which children from a circle and toss a hot potato.
The counting starts with the first kid.
Every n-th toss, the child holding the potato leaves the game.
When a kid leaves the game, it passes the potato to the next kid. Until there is only one kid left.

Simulate the game of Hot Potato. On the first line you will receive kids' names, separated by space.
On the second line you get the n-th toss (int), in which a kid leaves the game.

Print every kid who is removed and print the only kid left in the end.
"""
from collections import deque

kids = deque(input().split())
n = int(input())

while len(kids) > 1:
    kids.rotate(-n)
    print(f"Removed {kids.pop()}")

print(f'Last is {kids.popleft()}')
