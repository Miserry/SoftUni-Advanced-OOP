n = int(input())
stack = []

for i in range(n):
    x = input()
    if x.startswith("1"):
        stack.append(int(x[2:]))
    elif x.startswith("2") and len(stack) > 0:
        stack.pop()
    elif x.startswith("3"):
        print(max(stack))
    elif x.startswith("4"):
        print(min(stack))

stack.reverse()
print(*stack, sep = ', ')
