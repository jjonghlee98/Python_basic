# 클래스 변수 & 클래스 메소드

class tcl:
    cv = 10.0

    def foo(a, b):
        print(a * b * tcl.cv) # tcl에 있는 cv

    def __init__(self):
        self.a = 10.0

    def f1(self, a, b):
        print(f'{self.a}, {self.b}, {a}, {b}')
tcl.foo(3, 4)
print(tcl.cv)
