# 출석번호 1 2 3 4, 앞에 100을 붙임
student = [1,2,3,4,5]
print(student)
students = [i+100 for i in student]
print(students)

# 학생 이름을 길이로 변환
student_name = ["i am groot", "thor"]
student_name = [len(i) for i in student_name]
print(student_name)