customer ="토르"
index = 5
while index >=1:
    print("{0}, 손님 커피가 완료 되었습니다. {1}번남았습니다.".format(customer,index))
    index-=1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")

customer = "아이언맨"
index = 1
while True:
    print("{0}, 커피가 준비 되었습니다. 흐출{1}회".format(customer,index))
    index+=1    
    break

customer = "토르"
person = "Unknown"

while person != customer:
    print("{0},님 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")