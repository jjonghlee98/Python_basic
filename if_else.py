x = float(input("value: "))

# 수식으로 계산 
absx = x * (x > 0) * 2 - x
print("%.2f --> %.2f" % (x, absx))

# if 조건문으로 계산
if x > 0: absx = x
else: absx -x
print("%.2f --> %.2f" % (x, absx))

# 한줄 if 조건문으로 계산
absx = x if x > 0 else -x
print("%.2f --> %.2f" % (x, absx))

# 리스트값을 이용한 
reftbl = (-1.0, 1.0)
absx = x * reftbl[x > 0]
print("%.2f --> %.2f" % (x, absx))
