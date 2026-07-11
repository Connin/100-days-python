import csv
import pandas

# data = []
# content = []

# with open("weather_data.csv") as file:
#     data = csv.reader(file) # iterator = data를 하나씩 꺼내는 객체(메모리에 들어가지 않음)
#     temp = []
#     # for row in data:
#     #     print(row)
#     next(data)
#     for row in data:
#         temp.append(int(row[1]))
        
# print(temp)


# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20260625.csv")

Count_Gray = 0
Count_Cinnamon = 0
Count_Black = 0
color = []
data_list = data["Primary Fur Color"].to_list()
print(data_list)
for item in data_list:
    if item == 'Gray':
        Count_Gray += 1
    if item == 'Cinnamon':
        Count_Cinnamon += 1
    if item == 'Black':
        Count_Black += 1

color = {
    "color":["gray", "Cinnamon","Black"],
    "count":[Count_Gray, Count_Cinnamon, Count_Black]
}
gray = len(data[data["Primary Fur Color"] == "Gray"])
print(data[data["Primary Fur Color"] == "Gray"])

df = pandas.DataFrame(color)
df.to_csv("color.csv")

# avg = 0
# total = 0
# print(data["temp"].max())
# print(data["condition"])
# print(data[data.temp == max(data.temp)])

