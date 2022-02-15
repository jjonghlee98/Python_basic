while True:
    cmd = input(">> ").split()

    if cmd[0] == 'quit': break
    a = float(cmd[1])
    b = float(cmd[2])
    if cmd[0] == 'add': print(a + b)
    elif cmd[0] == 'sub': print(a-b)
    elif cmd[0] == 'mul': print(a*b)
    elif cmd[0] == 'div': print(a/b)

print("_" * 10)
