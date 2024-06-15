import pandas

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_series = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_series = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_series = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

print(gray_series, cinnamon_series, black_series)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_series, cinnamon_series, black_series]
}

new_df = pandas.DataFrame(data_dict)
print(new_df)
new_df.to_csv("fur_colors.csv")
