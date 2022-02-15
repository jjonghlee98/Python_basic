# 약수를 구하는 프로그램
n = int(input("n = "))

# list
divisors = []

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)

print(divisors)


# continue 사용
# continue는 부정적인 의미가 있다. *****
# continue는 예외처리
# 예외처리의 장점 : 들여쓰기 수준 감소
for i in range(1, n + 1):
    if n%i != 0: continue
    divisors.append(i)

print(divisors)

# 깔끔하게 프로그래밍 하는 경우 continue를 많이 사용함.
for i in range(1, n + 1):
    if i%2 == 0: continue
    if i%3 == 0: continue
    divisors.append(i)

print(divisors)
            
# while문의 경우 조심할 필요가 있음.
# 문제 있는 코드
sum = 0
i = 1

while i <= n:
    if i%2 == 0: continue
    if i%3 == 0: continue
    # continue로 인해 아래의 두 줄이 동작을 안하고 무한루프에 빠짐
    sum += i
    i += 1

print(divisors)

# 문제 없는 코드

while i <= n:
    if i%2 != 0:
        if i%3 != 0:
            sum += i
    i += 1

print(sum)

# 또 다른 방법

while i <= n:
    k = i
    i += 1
    if k%2 == 0: continue
    if k%3 == 0: continue
    sum += k

print(sum)
