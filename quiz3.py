#site = "http://naver.com"
site = "http://google.com"
print(site[7:])
my_site = site.replace("http://","")
print(my_site)
site1 = site[7:]
print(site1[:-4])
site2 = site1[:-4]
print(site2)
my_site1 = my_site[:my_site.index(".")] # my_site에서 . 이 나오는 위치 직전까지
print(my_site1)

# 비밀번호 생성
print("생성된 비밀번호 : "+site2[:3]+str(len(site2))+str(site2.count("e"))+"!")
password = my_site1[:3] + str(len(my_site1)) + str(my_site1.count("e")) + "!"
print("{0}의 생성된 비밀번호는 {1}입니다".format(site,password))