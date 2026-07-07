
# def format(f_name, l_name):
#   fname = f_name.title()
#   lname = l_name.title()
#   return f"{fname} {lname}"

# print(format(f_name = "kyLe", l_name = "BAE"))

# def is_leap_year(year):
#   """
#   윤년계산식
#   이런식 저럭식
#   123
#   """
#   fre = False
#   hre = False
#   fhre = False
#   Leap = False

#   if year % 4 == 0:
#     fre = True
#   if year % 100 == 0:
#       hre = True
#   if  year % 400 == 0:
#       fhre = True

#   if fre == False:
#     return False
#   elif fre == True:
#     if hre == False:
#       return True
#     elif hre == True and fhre == False:
#       return False
#     elif fhre == True:
#         return True
#     # Write your code here. 
#     # Don't change the function name.

# print(is_leap_year(2000))

def add(n1,n2):
    return n1 + n2
def substract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add, 
    "-" : substract, 
    "*" : multiply, 
    "/" : divide
    }

def calculator():
  n1 = float(input("first number"))
  for key in operations:
    print(key)
  ops = input("your operations")
  n2 = float(input("another numbner"))

  conti = True

  while conti == True:

    print(f"The result is {operations[ops](n1,n2)}")
    check = input("want to continue? y or n").lower()
    if check == "y":
        n1 = operations[ops](n1,n2)
        n2 = float(input("another numbner"))
        ops = input("your operations")
        conti = True
    else:
        conti = False
  calculator()    

calculator()