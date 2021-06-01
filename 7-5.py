def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름:{0}\t나이:{1}\t".format(name,age),end=" ")
    print(lang1,lang2,lang3,lang4,lang5)

profile("유재석", 29, "파이썬","자바","c","c++","C#")
profile("김태호", 30, "","","","","")

def profile(name,age,*language):
    print("이름:{0}\t나이:{1}\t".format(name,age),end=" ")
    for lang in language:
        print(lang,end=" ")
    print()    

profile("유재석", 29, "파이썬","자바","c","c++","C#","자바스크립트")
profile("김태호", 30)