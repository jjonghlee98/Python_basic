friendList = input("친구들의 이름을 입력하세요: ").split()

friend = input("이름을 입력하세요: ")

if friend in friendList:
    print(f"{friend}은(는) 당신의 친구입니다.")
else:
    print(f"{friend}은(는) 당신의 친구가 아닙니다.")
