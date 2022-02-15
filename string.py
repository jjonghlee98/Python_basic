# 문자열 거꾸로 출력하기

s = input("문자열: ")

slen = len(s)

for i in range(slen):
    print(s[slen-i-1], end="")
print()

for i in range(-1, -slen-1, -1):
    print(s[i], end="")
print()

for i in range(slen-1, -1, -1):
    print(s[i], end="")
print()

print(s[::-1])
