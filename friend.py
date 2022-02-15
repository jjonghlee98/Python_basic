friends = input("당신의 친구들의 이름을 입력하세요: ")
friendsList = friends.split()

print("나의 친구들은 %s입니다." % "-".join(friendsList))
