name = input("이름: ")
birthday = input("생년월일: ")

year = int(birthday[:4])
age = 2022 - year

print("-"*40)
print(" 이름  | {0:^10}".format(name))
print(f" 나이 | {age:^10}")
print(f"생년월일 | {year}년 {birthday[4:6]}월 {birthday[6:]}일")
print("-"*40)
