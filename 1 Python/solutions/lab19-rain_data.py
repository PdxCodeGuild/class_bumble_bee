

import re
from datetime import datetime


with open('./data/hayden_island.rain', 'r') as file:
    text = file.read()


# using string methods
# lines = text.split('\n')
# lines = lines[11:]
# for line in lines:
#     data = line.split()
#     print(data[0], data[1])

data = re.findall(r'(\d+-\w+-\d+)\s+(\d+)', text)

# use a list of tuples
# for i in range(len(data)):
#     date = datetime.strptime(data[i][0], '%d-%b-%Y')
#     daily_total = round(int(data[i][1])*0.01*2.54, 4) # daily total in cm
#     data[i] = (date, daily_total)



# using a dictionary with the dates as the keys and the daily totals as the values
# data_dict = {}
# for row in reversed(data):
#     date = datetime.strptime(row[0], '%d-%b-%Y')
#     daily_total = round(int(row[1])*0.01*2.54, 4) # daily total in cm
#     data_dict[date] = daily_total

# average_daily_rainfall = 0
# for date in data_dict:
#     average_daily_rainfall += data_dict[date]
# average_daily_rainfall /= len(data)
# print(average_daily_rainfall)


class RainDataRow:
    def __init__(self, date, daily_total):
        self.date = date
        self.daily_total = daily_total
    
    def __str__(self):
        return f'{self.date.strftime("%Y/%m/%d")} {self.daily_total}cm'

    def __repr__(self):
        # return str(self)
        return self.__str__()
    
    

# list of class instances
for i in range(len(data)):
    date = datetime.strptime(data[i][0], '%d-%b-%Y')
    daily_total = round(int(data[i][1])*0.01*2.54, 4) # daily total in cm
    data[i] = RainDataRow(date, daily_total)

average_daily_rainfall = 0
for row in data:
    average_daily_rainfall += row.daily_total
average_daily_rainfall /= len(data)
print(average_daily_rainfall)



















