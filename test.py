n = int(input("1부터 n까지의 합을 구하기 위해 n을 입력하세요: "))
sum = 0
for i in range(1, n + 1):
    sum += i

print("1부터 %d까지의 합은 %d입니다." % (n, sum))
