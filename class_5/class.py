
# Working with dates and times (datetime)

# import datetime

# current_date = datetime.datetime.now()

# print(current_date.year)
# print(current_date.month)
# print(current_date.day)

# print(current_date.hour)
# print(current_date.minute)


import datetime

current_date = datetime.datetime.now()
format_date = current_date.strftime("%H:%M:%S")
print(format_date)

date1 = datetime.datetime(2024,9,1)
date2 = datetime.datetime(2023,10,1)

different = date1 - date2
print(different)