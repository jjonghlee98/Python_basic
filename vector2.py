# 2차원 벡터 클래스

class vector2:
    def __init__(self, x=0.0, y=0.0):
        self.x = x # x라는 멤버 변수
        self.y = y # y라는 멤버 변수

    def __add__(self, other):  # + 연산자
        x = self.x + other.x
        y = self.y + other.y
        return vector2(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return vector2(x, y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'vector2({self.x}, {self.y})'

p1 = vector2(1.3, 2.5)
p2 = vector2(2.1, 3.5)

print(p1+p2)
print(p1-p2)
