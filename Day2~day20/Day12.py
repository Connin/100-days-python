

# def is_prime(num):
#     dividnum = []
#     for i in range(2,num):
#         if num % i == 0:
#             dividnum.append(i)
#     if dividnum == []:
#         return True
#     else:
#         return False

# is_prime(4)
import random
answer = random.randrange(1, 100, 1)
life = 0
difficulty = input("difficulty set").lower()
if difficulty  == "easy":
    life = 10
if difficulty  == "hard":
    life = 5

def ask():
    your_ans = int(input("guess number"))
    return your_ans

Correct = False
while life > 0 and Correct == False:
    ans = ask()
    if ans > answer:
        print("Too high")
        life -= 1
        #ask()
    elif ans < answer:
        print("Too low")
        life -= 1
        #ask()
    else:
        print("Correct")
        Correct = True

print("Game over")
    