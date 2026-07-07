# fruits = ["grape", "apple", "pear"]
# for i in fruits:
#     print(i)

# student_scores = [4, 5, 9, 10, 9]
# max = 0
# for i in student_scores:
#    if i > max:
#       max = i
# print(max) 
# total = 0
# for i in range(1, 101):
#     if i % 15 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
import random

letters = ['a', 'e', 'v', 'e']
num = ['1','2','3']
symbols = ['!','*','^']

print("PW generator")
nr_letters = int(input("how many letters?\n"))
nr_num = int(input("how many numbers?\n"))
nr_Symbols = int(input("how many symbols?\n"))
pw = ""
let_counter = 0
num_counter = 0
sym_counter = 0
for i in range(0,nr_letters):
    pw += random.choice(letters)
for i in range(0,nr_num):
    pw += random.choice(num)
for i in range(0,nr_Symbols):
    pw += random.choice(symbols)
pw_list = list(pw)
random.shuffle(pw_list)
passw = ""
for char in pw_list:
    passw += char 
#pw = "".join(pw_list)
print(f"ur pw is {passw}")


#easy
# for i in range(0,nr_letters):
#     pw += random.choice(letters)
# for i in range(0,nr_num):
#     pw += random.choice(num)
# for i in range(0,nr_Symbols):
#     pw += random.choice(symbols)
# print(pw)

        