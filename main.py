# with open("weather_data.csv") as data:
#     list = data.readlines()
# print(list)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas
# data = pandas.read_csv("weather_data.csv")
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# # average = sum(temp_list)/len(temp_list)
# # print(average)
# #
# # print(data["temp"].max())
#
# print(data[data.temp == data.temp.max()])
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
primary = data["Primary Fur Color"]
grey = len(data[data["Primary Fur Color"] == "Gray"])
red = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])
data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [grey, red, black]
}
data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("squirel_count.csv")


