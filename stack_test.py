# 후위 연산자

# 3 2 + 4 2 - * = 10

# 1 2 3 4 + * 5 + * = 19

expr = input('수식: ').split()

stack = []

for e in expr:
    if e == '+' or e == '-' or e == '*' or e == '/':
        b = stack.pop()
        a = stack.pop()
        if e == '+':
            r = a + b
        elif e == '-':
            r = a - b
        elif e == '*':
            r = a * b
        elif e == '/':
            r = a / b
        stack.append(r)
    else:
        stack.append(float(e))

print(stack[0])
