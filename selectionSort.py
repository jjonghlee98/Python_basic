# 정렬
import random as rd
import time

def selectionSort(v):
    # v를 정렬
    n = len(v)
    for i in range(n-1):
        m = i
        for j in range(i+1, n):
            if v[j] < v[m]: # 현재의 값보다 j인덱스의 값이 더 작으면
                m = j
        v[i], v[m] = v[m], v[i] # swap

v = [ rd.randint(1, 1000001) for _ in range(20000) ]

start = time.time()
# v.sort()
selectionSort(v)
elapsed = time.time() - start
print(f'Elapsed : {elapsed * 1000:.1f}ms')
