student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for key in student_scores:
    print(key)
    if student_scores[key] > 90:
      student_grades[key] = "Outstanding"
    elif 81 <= student_scores[key] <= 90:
      student_grades[key] = "Exceeds Expectations" 
    elif 71 <= student_scores[key] <= 80:
      student_grades[key] =  "Acceptable" 
    elif student_scores[key] < 71:
      student_grades[key] = "Fail"

print(student_grades)

# travel_log = {
#   "france": {"visited" : ["paris", "lillie"]} ,
#   "visited" : 12
# }
# print(travel_log["france"]["visited"][1])

# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }
# for key in dict:
#   dict[key] += 1

# print(dict)

# starting_dictionary = {
#     "a": 9,
#     "b": 8,
# }


# final_dictionary = {
#     "a": 9,
#     "b": 8,
#     "c": 7,
# }
# final_dictionary = starting_dictionary
# starting_dictionary["c"] = 7
# print(starting_dictionary)

auction_info = {}
Maxprice = 0
winner = ""

Trueor = "yes"

while Trueor == "yes":
  name = input("name please ")
  price = int(input("price "))
  auction_info[name] = price
  Trueor = input("more people? Yes or No ").lower()
  print("\n" * 100)

print(auction_info)

winner = max(auction_info, key = auction_info.get)
Maxprice = auction_info[winner]

print(f"Winner is {winner} with {Maxprice}$")

# for key in auction_info:
#   if auction_info[key] > Maxprice:
#     Maxprice = auction_info[key] 
#     winner = key

print(f"Winner is {winner} with {Maxprice}$")