# factorial function

def factorial(n):
    # 탈출조건이 있는 재귀함수
    # 탈출조건이 없으면 무한 호출로 인해 에러 발생
    if n == 0: return 1
    return n * factorial(n-1)

#이런 형태로 하는 경우가 많음 (forward program)
def fac(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

n = int(input('n = '))

print(f"{n}! =  {factorial(n)}")

# 반복함수 사용
def myfact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
        yield f

for i in myfact(n):
    print(i)
    
