# 문자열로 원하는 값 찾기 (Dictionary)

# 대응관계(mapping) 형태로 검색하는 경우 dict 자료형을 이용해야 함.

# numdict에 값을 추가해도 되고 안 해도 됨
numdict = { 'one' : 1, 'two' : 2, 'three' : 3,
            'four': 4, 'five': 5, 'six': 6, 'seven': 7,
            'eight': 8, 'nine': 9}

# 무한 반복문
while True:
    cmds = input('$ ').split()

    if cmds[0] == 'quit': break

    if cmds[0] == 'update':
        first = cmds[1]
        second = int(cmds[2])
        numdict[first] = second # 딕셔너리 이용
    elif cmds[0] == 'find':
        key = cmds[1]
        if key in numdict: print(numdict[key])
        else: print('Not Found')
    # 계산기 기능까지 가능
    elif cmds[0] == 'add': 
        first = cmds[1]
        second = cmds[2]
        if first not in numdict or second not in numdict:
            print('Parameter Error')
        else:
            print(numdict[first] + numdict[second])
