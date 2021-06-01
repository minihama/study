absent = [2,5] #결석
no_book = [7] #책을 안 가지고옴
for studnet in range(1,11):
    if studnet in absent:
        continue
    elif studnet in no_book:
        print("오늘 수업은 여기까지. {0}는 교무실로 따라와".format(studnet))
        break
    print("{0}, 책을 읽어봐".format(studnet))

