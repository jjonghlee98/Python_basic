# O(N) 알고리즘 
import random
import time

n = int(input('n >> '))
start = time.time()
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1
print(count)
elapsed = time.time() - start
print(elapsed)
