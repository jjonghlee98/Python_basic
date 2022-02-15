# 요세푸스 문제 풀기

n, k = map(int, input('n, k = ').split())

# 1. 1 ~ n까지의 숫자들을 큐에 넣습니다.
queue = list(range(1, n+1))

# 2. queue가 비어있지 않는 한 계속 반복문
while len(queue) > 0:
    # 3. k-1개를 큐에서 제거하고 다시 넣는다.
    # 수행문을 k-1번 단순 실행할 경우에 사
    for _ in range(k-1):
        c = queue.pop(0)
        queue.append(c)

    # 4. queue에서 값을 가져와서 출력
    c = queue.pop(0)
    print(c)

# , , 3,  6,  2   7    1 4, 5,

# 3 6 2 7
