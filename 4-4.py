print("a"+"b")
print("a","b")

# 방법1
print("나는 %d살입니다." % 20) #d는 정수를 의미
print("나는 %s을 좋아해요" % "파이썬") #s는 문자열
print("Apple 은 %c로 시작해요." % "A")
# %s로만써도 됨
print("나는 %s색과 %s 색을 좋아해요." %("파란","빨강"))
# 방법2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아해요." .format("빨강","파란"))
print("나는 {0}색과 {1}색을 좋아해요." .format("빨강","파란"))
print("나는 {1}색과 {0}색을 좋아해요." .format("빨강","파란"))

# 방법3
print("나는 {age} 살이며, {color}색을 좋아해요.".format(age=20, color="빨강"))

# 방법4 (v3.6이상에서)
age = 30
color = "파랑"
print(f"나는 {age} 살이며, {color}색을 좋아해요.")
