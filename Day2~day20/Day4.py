import random

# random_int = random.randint(4,6)
# print(random_int)

# random_float1 = random.random() * 10
# print(random_float1)

# random_float = random.uniform(4.3,5.2)
# print(random_float)

# if random_int < 5:
#     print("Heads")
# else:
#     print("Tails")

#List = [순서가, 중요, 내용 변경 가능] print(List[2] = 변경 가능)
# 반복 가능한 객체(iterable) 는 for 문으로 하나씩 꺼낼수 있는 객체
# for x in [1, 2, 3]:
# print(x)

# friend = ["alic", "bob", "jane", "anna", "david"]
# random_int = random.randint(0,4)
# print(f"{friend[random_int]} will pay the bill")

# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
# dirty_dozen = [fruits, vegetables]

# print(dirty_dozen[0])
# print(dirty_dozen[1])

# print(dirty_dozen[0][2])
# print(dirty_dozen[0][3])

urchoice = int(input("u choose\n"))
if urchoice == 0:
    print("Rock")
elif urchoice == 1:
    print("Paper")
else:
    print("Sessiors")

computer = random.randint(0,2)
print(computer)
if urchoice == 0 and computer == 0 or urchoice == 1 and computer == 1 or urchoice == 2 and computer == 2:
    print("draw")
elif urchoice == 0 and computer == 1 or urchoice == 1 and computer == 2 or urchoice == 2 and computer == 0:
    print("u lost")
else:
    print("u won")
