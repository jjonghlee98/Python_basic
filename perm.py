# 순열 구하기
from itertools import permutations
def perm(v, s, r):
    # 탈출 조건 필수
    if r == 0:
        print(s)
        return

    for e in v:
        # e가 이미 s에 존재한다면, 예외 처리
        if e in s:
            continue
        perm(v, s + (e, ), r-1)

friends = input('친구들: ').split()

k = int(input('k : '))

perm(friends, tuple(), k)


print('-' * 20)

for i in permutations(friends, k):
    print(i)
