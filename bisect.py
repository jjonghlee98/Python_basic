# 가장 긴 길이의 증가하는 부분 수열의 길이 구하기
# LIS (Longest Incremental Subsequence)
from bisect import *
v = list(map(int, input('>> ').split()))

d = []

for e in v:
    if d == [] or d[-1] < e: d.append(e)
    else:
        idx = bisect_left(d, e)
        d[idx] = e
    print(f'{e} : {d}')

print(len(d))

