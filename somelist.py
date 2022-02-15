# for 문을 사용한 방법
numbers = []
for k in range(1, 11):
    numbers.append(k)

print(numbers)
# 리스트 내포를 이용한 방법
numbers = [k for k in range(1, 11)]
print(numbers)

# 반복 함수를 사용한 방법
numbers = list(range(1, 11))
print(numbers)


# 1 ~ 10까지의 수중에 2 또는 3의 배수가 아닌 수를 리스트로 만들기

ns = [k for k in range(1, 11) if k%2 != 0 and k%3 != 0]
print(ns)

# 일반적인 for문으로 코딩한 경우
ns = []
for k in range(1, 11):
    if k%2 != 0 and k%3 != 0:
        ns.append(k)
print(ns)

# 중첩 반복문 리스트 내포도 존재함

# 구구단 리스트
for dan in range(2, 10):
    for m in range(1, 10):
        print(f"{dan}x{m}={dan*m}")

# 구구단 리스트 내포
gugudan = [f"{dan}x{m}={dan*m}" for dan in range(2, 10)
           for m in range(1, 10)]
print(gugudan)

for g in gugudan:
    print(g)
