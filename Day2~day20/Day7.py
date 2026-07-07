# Hangman
import random
life = 6
word_list = ["camel", "adverse", "rayman"]
answer = random.choice(word_list)
answer_list = list(answer)
blanklist = []
for i in range(0, len(answer)):
  blanklist[:] += "_"

word = "".join(blanklist)
print(word)


while life > 0 and "_" in blanklist:
    user_input = input("Guess a letter\n")
    found = False
    for i in range(0,len(answer)):
        if user_input == answer_list[i]:
          print("correct\n")
          blanklist[i] = user_input
          word = "".join(blanklist)
          print(word)
          found = True,
    if found == False:
      #print(answer_list)
      #print(user_input)
      print("You lose a life\n")
      life -= 1
      #print(f"{life}")
      if life == 5:
        print("life is 5")
      elif life == 4:
        print("life is 4")
      elif life == 3:
        print("life is 3")
      elif life == 2:
        print("life is 2")
      elif life == 1:
        print("Only 1 life")   
        


if life > 0:
  print("you won")
else:
   print("game over")
