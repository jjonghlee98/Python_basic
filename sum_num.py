sum = 0 # 초기값은 +에 항등원
i = 1   # 1부터 10까지 더하기 위해서 하는 것이므로 출발값으로 설정

while i <= 100:  # i값이 최종 도착값이 될 때까지를 의미
    sum += i    # sum에 중간값을 저장하고 sum = sum + i
    i += 1      # 현재 더해진 값의 다음 수로 while 조건식을 변경하는 용도

print(sum)

fact = 1
i = 1

while i <= 100:
    fact *= i
    i += 1
    
print(fact)
