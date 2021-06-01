def profile(name, age, main_lang):
    print("이름:{0}\t나이:{1}\t주 사용언어:{2}".format(name,age,main_lang))

profile("유재석",30,"파이썬")
profile("김태호",35,"자바")

def profile(name,age=17,main_lang="파이썬"):
    print("이름:{0}\t나이:{1}\t주 사용언어:{2}".format(name,age,main_lang))

profile("고구마")
profile("우유")    