from random import *
#lt_all=[1,2,3,4,5,6,7,8,9,10]
#lt_add=max(lt_all)
#lt_add+=1
#lt_all.append(lt_add)
#
#lt_min=min(lt_all)
#lt_max=max(lt_all)
#lt = randint(lt_min,lt_max)
#print("치킨 당첨자 : {}".format(lt))
#lt_all.remove(lt)

#lst=[1,2,3,4,5]
#print(lst)
#shuffle(lst)
#print(lst)
#print(sample(lst,1))

users = range(1,21) #1부터 20까지 숫자 생성
users = list(users)
#print(type(users))

shuffle(users)
winners = sample(users,4)

print("--당첨자 발표--")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--축하합니다.--")