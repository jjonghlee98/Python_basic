# 빈도 계산
a = [ 1, 3, 2, 4, 7, 2, 3, 1, 3, 2, 3, 4, 5, 2, 6, 1, 2, 2, 2 ]

histo = {}

for k in a:
    if k in histo: histo[k] += 1
    else: histo[k] = 1

print(histo)
