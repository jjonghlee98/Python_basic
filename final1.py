import random
import time

v = [ random.randint(1, 1000000) for _ in range(100000) ]
s = [ random.randint(1, 1000000) for _ in range(10000) ]

# 시간이 적게 걸림
start = time.time() # 현재 시간을 초단위로 출력
t = set(v)
count = 0
for k in s:
    if k in t: count += 1
print(count)
elapsed = time.time() - start
print(elapsed)

print('-'*20)

# 시간이 오래 걸림
start = time.time() # # 현재 시간을 초단위로 출력
count = 0
for k in s:
    if k in v:
        count += 1
print(count)
elapsed = time.time() - start
print(elapsed)
