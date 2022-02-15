# 클래스로 Queue 구현하기

class queue:
    def __init__(self):
        self.data = list() # 멤버 변수 선언 (비어있음)

    def get(self):
        # 비어있는 경우에는 None(아무것도 없음)을 반환
        if len(self.data) == 0: return None
        return self.data.pop(0)

    def put(self, newitem):
        self.data.append(newitem)

    def empty(self):
        return len(self.data) == 0

    def qsize(self):
        return len(self.data)

q = queue()
while True:
    cmd = input('>> ').split()
    if cmd[0] == 'quit': break

    if cmd[0] == 'get': print(q.get())
    elif cmd[0] == 'put': q.put(cmd[1])
    elif cmd[0] == 'empty': print(q.empty())
    elif cmd[0] == 'qsize': print(q.qsize())
    
