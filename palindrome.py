# palindrome 개수 구하기

# 반복함수를 이용한 부분 문자열 만들기
def substring(s):
    #중복을 허용하지 않게 하기 위해서 집합 자료형을 생성
    dup = set()
    # 부분 문자열 찾아보기
    n = len(s)
    for i in range(n):
        for j in range(i+1, n+1):
            # 중복 검사
            if s[i:j] in dup: continue
            dup.add(s[i:j])
            yield s[i:j]

def isPalindrome(s): # s : str
    # 안 좋은 방법
    # if s == s[::-1]: return True
    # else: return False
    # return True if s == s[::-1] else False

    # 좋고 깔끔한 방법 *****
    return s == s[::-1]

s = input('문자열: ')

pcount = 0
for i in substring(s):
    if isPalindrome(i):
        pcount += 1

print(f'{s}의 부분문자열 중 중복되지 않은 팰린드롬의 개수는 {pcount}입니다.')
