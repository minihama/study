python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python","Java"))

index = python.index("n") #n이 몇번째 위치에 있는지
print(index)
index = python.index("n", index +1) #n의 다음번째 위치
print(index)

print(python.find("Java")) # 원하는 값이 변수에 없으면 "-1"를 반환, index를 통한 검색은 오류발생

print(python.count("n"))