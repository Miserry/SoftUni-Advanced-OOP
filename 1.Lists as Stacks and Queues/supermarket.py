from collections import deque

name = input("Enter a name: ")
line = deque()

while not name == "End":
    if name == "Paid":
        while line:
            print(line.popleft())
    else:
        line.append(name)
    name = input("Enter a name: ")

print(f'{len(line)} people remaining')