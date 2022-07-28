"""
Find the index of the matching parenthesis in the expression given.
"""
expression = "1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5"

par_stack = []        #This is a stack. We move items there and then pull them out. LIFO method.

for i in range(len(expression)):
    if expression[i] == "(":
        par_stack.append(i)
    elif expression[i] == ")":
        start_index = par_stack.pop()
        print(expression[start_index:i+1])