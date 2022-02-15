import random as rd
import time

def insertionSort(v):
    n = len(v)
    for i in range(1, n):
        t, last = v[i], i
        while last > 0 and v[last-1] > t:
            v[last] = v[last-1]
            last -= 1
        v[last] = t

def bubbleSort(v):
    n = len(v)
    for i in range(n-1):
        isDirty = False
        for j in range(n-i-1):
            if v[j] > v[j+1]:
                v[j], v[j+1] = v[j+1], v[j]
                isDirty = True
        if not isDirty: break
        
v = [ rd.randint(1, 10000000) for _ in range(20000) ]
# v = [ _+1 for _ in range(20000) ]
v.append(0)

start = time.time()
# insertionSort(v)
bubbleSort(v)
elapsed = time.time() - start
print(f'Elapsed: {elapsed * 1000:.1f}ms')
