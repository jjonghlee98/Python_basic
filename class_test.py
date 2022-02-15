class MyClass:
    def __init__(self):
        print('MyClass 객체를 생성합니다.')
        print('생성자는 주로 멤버변수를 초기화하는 역할을 합니다.')
        self.memberVariable = 0 # 생성
        
    def __del__(self):
        print('MyClass 객체를 소멸합니다.')
        print('소멸자는 거의 사용이 안 됩니다.')
        
    def foo(self):
        print('foo')

    def roo(): # 객체함수 X
        print('roo')

class DerivedClass(MyClass):
    def __init__(self):
        print('Derived Class Constructor')

    def foo(self, x = 0): # default 값이 0
        MyClass.foo(self) # 부모의 foo를 부(꼭 부모 클래스는 아님)
        print('New Derived Class foo %s' % x)
        
    def func(self, x):
        # self.foo() # 위의 def foo를 부름
        # MyClass.foo(self) # 부모의 foo를 부름
        print('Derived Class function %s' % x)
        
            
# obj = MyClass()     # obj란 변수에 MyClass 객체를 생성합니다.

# obj.foo()           # obj가 MyClass 객체이므로 MyClass.foo(obj)로 해석
# MyClass.foo(obj)    # obj.foo()와 동일

# obj.roo()         # self가 들어가 있지 않은 경우
# MyClass.roo()       # 

# del(obj)            # obj란 객체를 삭제(소멸)합니다.


obj = DerivedClass()
obj.foo(10)
obj.func('abc')
