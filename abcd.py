# abcd.py

pi = 3.141592

def foo():
    print('abc.py에 정의된 foo() 함수')
    print(__name__)

class abcd:
    def __init__(self):
        print('abcd class')

    def foo(self):
        print('abcd.foo()')

# import 할 때 실행이 안되도록 if문으로 실행할 부분을 감싼다.
if __name__ == '__main__':
    print('-'*20)
    foo()
    print('-'*20)

