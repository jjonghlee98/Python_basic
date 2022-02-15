n = int(input("n = "))

divCount = 0

for i in range(1, n+1):
    if n % i == 0:
        divCount += 1

print(f"{n}의 약수의 개수는 {divCount}입니다.")