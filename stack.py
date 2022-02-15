# stack 구현 및 테스트
stack = []

while True:
    cmds = input('>> ').split()

    # cmds[0] >> command
    # cmds[1] >> 1st parameterd
    if cmds[0] == 'quit': break

    if cmds[0] == 'push':
        stack.append(cmds[1])
    elif cmds[0] == 'pop':
        print(stack.pop())
    elif cmds[0] == 'top':
        print(stack[-1])
    elif cmds[0] == 'empty':
        print(len(stack) == 0)

