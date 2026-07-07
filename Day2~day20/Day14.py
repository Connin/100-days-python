from gamedata import data
import random

score = 0
name = ""
follow =""
descrip = ""
country = ""
randdata = {}
randdatb = {}
def ask():
    answ = input("Who has more followers? A or B ").lower()
    return answ

def shuffle(answer):
    numbers = random.sample(range(0,4), 2)
    randdata = data[numbers[0]]
    randdatb = data[numbers[1]]
    print(f"Compare A: {randdata['name']}, {randdata['description']}, from {randdata['country']}")
    print(f"Against B: {randdatb['name']}, {randdatb['description']}, from {randdatb['country']}")
    if answer == "a":
        if randdata["follower"] > randdatb["follower"]:
            return True
        elif randdata["follower"] < randdatb["follower"]:
            return False
    if answer == "b":
        if randdata["follower"] < randdatb["follower"]:
            return True
        elif randdata["follower"] > randdatb["follower"]:
            return False

# print(randdata)
# print(numbers)
# print(randdata["name"])
# if list(randdata.keys())[1] > list(randdatb.keys())[1]:

def checkdata():
    score = 0
    while True:
        answer = ask()
        result = shuffle(answer)
        if result == True:
            score += 1
            print(f"correct current score is {score}")
        elif result == False:
            print(f"WRONG. FINAL SCORE is : {score}")
            break


checkdata()