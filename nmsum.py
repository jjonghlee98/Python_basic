# 배수의 합 계산하기
def sum(n, m):
    msum = 0
    for i in range(1, n+1):
        if i%m != 0: continue
        msum += i
    return msum

n, m = map(int, input('n, m = ').split())


print(f"1부터 {n}까지의 {m}의 배수의 합은 {sum(n, m)}입니다.")
