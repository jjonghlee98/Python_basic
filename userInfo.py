# 사용자 정보 만들기(dictionary)

# 다양한 항목 중 필요한(내용이 있는) 항목만 저장하는 것이 핵심

userInfo = {}

name = input('이름: ')
if name != '':
    userInfo['name'] = name

company = input('회사: ')
if company != '': userInfo['company'] = company

tel = input('전화번호: ')
if tel != '': userInfo['telphone'] = tel

addr = input('주소: ')
if addr != '': userInfo['address'] = addr

birth = input('생년월일: ')
if birth != '': userInfo['birthday'] = birth

print(userInfo)

# 깔끔하게
fmt = "{0:^10} | {1}"  # string format이 깔끔한 정렬에 좋음
print('-'*30)
for k in userInfo:
    print(fmt.format(k, userInfo[k])) # 이
print('-'*30)
