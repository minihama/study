cabinet = {3:"유재석",100:"김태호"}
print(cabinet[3])
print(cabinet[100])
print(cabinet.get(3))
#print(cabinet[5]) #오류 발생으로 프로그램 종료
print(cabinet.get(5)) # 오류 발생 없이 넘어감
print(cabinet.get(5,"사용가능")) # 이렇게 쓰면 5가 없으면 뒤에 내용 출력

print(3 in cabinet)
print(5 in cabinet)

cabinet1 = {"A-3":"유재석","B-100":"김태호"}
print(cabinet1.get("A-3"))
print(cabinet1["B-100"])

print(cabinet1)
cabinet1["A-3"]="김종국"
cabinet1["C-20"] = "조새호"
print(cabinet1)

del cabinet1["A-3"]
print(cabinet1)

print(cabinet1.keys())
print(cabinet1.values())
print(cabinet1.items())

cabinet1.clear()
print(cabinet1)