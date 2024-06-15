import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data)
#
# print(data[data.day == data.day.min()])
# # with open("weather_data.csv", "r") as weather_file:
# #     data = weather_file.readlines()
# #     print(data)
# # import csv
# #
# # with open("weather_data.csv", "r") as weather_file:
# #     data = csv.reader(weather_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data["temp"]))
# # print(type(data))
#
# dicta = data.to_dict()
# print(len(dicta))
#
# data_temp = data["temp"].tolist()
# print(data_temp)
#
# # avg_data = sum(data_temp) // len(data_temp)
# print(data["temp"].mean())
#
# # dictionary style of calling pandas
# data_max = data["condition"].min()
# print(data_max)
#
# # object style of calling pandas
# print(data.condition)
# # print(data["condition"])
# # get data in "Row"
# mid = data[data.day == "Monday"]
# print(mid)  # checks for the row where value is equal to Monday

# # to access the row that fits the criteria in the indexed value within the "data" variable
# # by filtering the column with a condition
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp_f = int(monday.temp) * 9/5 + 32
# print(monday_temp_f)
#
# diction = {
#         "country": ["France", "Germany", "Russia"],
#         "visits": [(12, 24, 4), (10, 11, 8), (5, 6, 3)],
#         "cities": [["Paris", "Lille", "Dijon"], ["Berlin", "Hamburg", "Stuttgart"], ["Moscow", "Saint Petersburg", "Kiev"]]
# }
#
# pan_dict = pandas.DataFrame(diction)
# print(pan_dict)
# pan_dict.to_csv("new_data.csv")

sts_score = {
    "student": ["Ange", "Ben", "Ken", "Moyo"],
    "score": [29, 38, 78, 90]
}
sts_score_df = pandas.DataFrame(sts_score)
for key, value in sts_score_df.iterrows():
    if value.student == "Ken":
        print(key, value.score)
