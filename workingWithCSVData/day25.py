# Day 25 #

# working with CSV Data and the Pandas Library.

# Definition: CSV = Comma Separated Values
DATA_FILE_PATH = "workingWithCSVData/weather_data - Sheet1.csv"
def csv_files():
    # import built-in csv library
    import csv
    # opening the CSV file and add each line into a list
    weather_data_list = []
    with open(DATA_FILE_PATH, "r") as weather_data:
        # unstriped_weather_data = weather_data.readlines()
        # for line in unstriped_weather_data:
        #     weather_data_list.append(line.strip())
        # print(weather_data_list)
        data = csv.reader(weather_data)
        temperatures = []
        # we took each row inside the weather_data.csv file ans separated out each item into a single value.
        # as ['day', 'temp', 'condition'] for example
        for row in data:
            print(row)
            if row[1] != "temp":
                temperatures.append(int(row[1]))
        print(temperatures)

    # we used so many lines to do a simple operation that's why we need the help of Pandas Library.

def panda_library():
    # import pandas library
    import pandas
    data = pandas.read_csv(DATA_FILE_PATH)
    #print(data)
    # or can use [temp] to only get the temperatures colum
    #print(data["temp"])

    # getting the data type
    print(type(data)) # output: <class 'pandas.core.frame.DataFrame'>
    # A DataFrame is the equivalent to the whole table.
    # example: every single sheet inside an excel file or a google sheet file is considered a DataFrame in pandas
    print(type(data["temp"])) # output: <class 'pandas.core.series.Series'>
    # A Series is equivalent to a list (a single colum in the table)

    #convert the data out of the csv file into a dictionary
    data_dict = data.to_dict()
    print(data_dict)

    #convert the series onto a list:
    data_list = data["temp"].to_list()
    print(data_list) # output: [12, 14, 15, 14, 21, 22, 24]

    #calculate the average temperature from the list
    average_temperature = round(sum(data_list) / len(data_list),1)
    print(f"average_temperature = {average_temperature}") #output: average_temperature = 17.4

    # or we can use the method .mean() to return the mean of values over the requested axis.
    print(f"mean value = {round(data['temp'].mean(),1)}") #output: mean value = 17.4

    # get the maximum value of the temperature colum/Series in the DataFrame.
    max_temperature = data['temp'].max()
    print(f"max_temperature = {max_temperature}") #output: max_temperature = 24

    # get data in columns
    # 1st way
    print(data["condition"]) # you are treating DataFrame here as a key.
    # 2nd way
    print(data.condition) # you are treating DataFrame here as an object.

    # get data in rows
    print(data[data.day == "Monday"]) # output: 0  Monday    12     Sunny
    # or
    print(data[data["day"] == "Monday"]) # output: 0  Monday    12     Sunny

    # get the row where we had the highest temperature at the week:
    print(data[data.temp == data['temp'].max()]) # output: 6  Sunday    24     Sunny

    # get a specific data from the row:
    monday = data[data.day == "Monday"]
    print(monday.condition) # output: 0    Sunny

    # convert from fahrenheit to celsius
    # C = (F - 32) * 5 / 9

    # convert from celsius to fahrenheit
    # F = 9/5C + 32

    fahrenheit_temp = 9/5 * monday.temp + 32
    print(f"fahrenheit_temp = {fahrenheit_temp}") #output: fahrenheit_temp = 0    53.6

    # create a dataFrame from scratch
    data_dict1 = {
        "students": ["Amy", "James", "Angela"],
        "scores": [76, 56, 65]
    }
    data1 = pandas.DataFrame(data_dict1)
    data1.to_csv("workingWithCSVData/new_data.csv")

def the_great_squirrel_census_data_analysis():
    # Goal is to create a small table called "squirrel_count.csv"
    # that has Fur, Color and Count columns
    import pandas
    squirrels_data = pandas.read_csv("workingWithCSVData/Central_Park_Squirrel_Census__Squirrel_Data.csv")
    fur_color_list = squirrels_data['Primary Fur Color'].to_list()
    gray_squirrels_amount = 0
    red_squirrels_amount = 0
    black_squirrels_amount = 0
    #print(fur_color_list)
    for color in fur_color_list:
        if color == "Gray":
            gray_squirrels_amount += 1
        elif color == "Cinnamon":
            red_squirrels_amount += 1
        elif color == "Black":
            black_squirrels_amount += 1
    #print(f"gray_squirrels_amount = {gray_squirrels_amount}, red_squirrels_amount = {red_squirrels_amount}, black_squirrels_amount = {black_squirrels_amount}")
    squirrel_count_dict = {
        "Fur Color": ["gray", "red", "black"],
        "Count": [gray_squirrels_amount, red_squirrels_amount, black_squirrels_amount]
    }
    data = pandas.DataFrame(squirrel_count_dict)
    data.to_csv("workingWithCSVData/squirrel_count.csv")

def the_great_squirrel_census_data_analysis2():
    import pandas

    data = pandas.read_csv("workingWithCSVData/Central_Park_Squirrel_Census__Squirrel_Data.csv")
    gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
    red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
    black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
    print(gray_squirrels_count) # output: 

    data_dict = {
        "Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
    }

    df = pandas.DataFrame(data_dict)
    df.to_csv("workingWithCSVData/squirrel_count.csv")

the_great_squirrel_census_data_analysis2()
