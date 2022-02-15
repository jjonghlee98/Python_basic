# 홀수 리스트 만들기

odds = []

for i in range(1, 101, 2):
    odds.append(i)

print(odds)

# 다른 방법 ( 더 느림 )
odds = []

for i in range(1, 101, 2):
    odds += [i]

print(odds)


