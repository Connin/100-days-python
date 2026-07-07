print("Hello"[-1]) # same as print("Hello"[4])
print(123,456,789 + 100,333,222)
print(123456789 + 999_333_922)
print(type(True))
print(int("12") // int("44")) 
print(int("12") ** int("44")) 
print((2 + 2 )/ 2) 
print(int("12") / int("44")) #Implicit typecasting(암시적 형 변환): Python이 자동으로 자료형(type)을 변환해 주는 것. 이경우는 Float으로 자동으로 바뀜
#flooring : 소수점 너머는 무조건 지움
#round(): 반올림
print(round(int("12") / int("44"), 3))
#print("num of letters: " + str(len(input("ur name"))))
print(f"") # F-string: 일일이 type를 바꿀 필요 없이 {} 안에만 variable을 넣으면 자동으로 바뀜
interger = 3
print(f"내일은 {interger}")
bill = float(input("bill"))
another = bill +1.2
print(f"another calculation is {another}")
print(bill + 1)