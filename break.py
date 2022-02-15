card = int(input("카드의 초기 충전 값: "))

while True:
    if card < 1500:
        break
    print("버스를 탑니다.")
    card -= 1500

print(f"남은 잔액는 {card}입니다.")
