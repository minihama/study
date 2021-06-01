# 리스트 []

subway1 = 10
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

subway_name = ["유재석","조새호","박명수"]
print(subway_name)

print(subway_name.index("조새호"))

subway_name.append("하하")
print(subway_name)

subway_name.insert(1,"정형돈")
print(subway_name)

print(subway_name.pop())
print(subway_name)

print(subway_name.pop())
print(subway_name)

print(subway_name.pop())
print(subway_name)

subway_name.append("유재석")
print(subway_name)
print(subway_name.count("유재석"))

num_list = [5,4,2,3,1]
num_list.sort()
print(num_list)

num_list.reverse()
print(num_list)

num_list.clear()
print(num_list)

max_list = ["조새호", 10, True]
print(max_list)
num_list = [5,4,2,3,1]

num_list.extend(max_list)
print(num_list)
