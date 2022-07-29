from collections import deque
n = "1"
line = deque()

for index in range(len(n)-1,-1,-1):
    if n[index].isdigit():
        line.append(int(n[index]))

for i in range(len(line)):
    print(line[i], end = ' ')