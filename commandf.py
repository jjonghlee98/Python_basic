
friendList = set()

while True:
    cmds = input(">> ").split()
    if cmds[0] == 'quit': break
    if cmds[0] == 'add':
        friendList.add(cmds[1])
    elif cmds[0] == 'list':
        for x in friendList:
            print(x, end=' ')
        print('')
    elif cmds[0] == 'find':
        if cmds[1] in friendList:
            print(f"{cmds[1]}은(는) 당신의 친구입니다.")
        else:
            print(f"{cmds[1]}은(는) 당신의 친구가 아닙니다.")
