# import json

# python object ----->> json string

# person = {
#     "name" : "joy",
#     "age" : 22,
#     "city" : "cumilla",
#     "haschildren" : False,
#     "titles" : ["engineer", "programer"]
# }

# personjson = json.dumps(person, indent = 4)
# print(personjson)


# json string  ------>> python object

# personjson ='{"name": "joy", "age":22, "city":"cumilla"}'
# personobj = json.loads(personjson)
# print(personobj['name'])


# --------------------------------------------------------------------
# python object ----->> json string + File Write

# person = {
#     "name" : "joy",
#     "age" : 22,
#     "city" : "cumilla",
#     "haschildren" : False,
#     "titles" : ["engineer", "programer"]
# }

# with open("person.json","w") as personJSONFile:
#     json.dump(person,personJSONFile, indent=4)


#-------------------------------------------------------

# with open("person.json","r") as personJSONFile:
#     personobj=json.load(personJSONFile)
#     person = json.dumps(personobj, indent=4)
#     print(person)


# -----------------------------------------------------------
#                     datetime   ------- class 3    --------
# -----------------------------------------------------------

# import datetime

# current_datetime = datetime.datetime.now()

# formated_datetime = current_datetime.strftime("%d/%m/%Y %H:%M:%S")

# print(formated_datetime)


# -------------------------------------------------

# import datetime

# date1 = datetime.datetime(year=2024, month=12, day=10)
# date2 = datetime.datetime(year=2004, month=2, day=7)
# different = date1 - date2
# print(different)

# new_date = date1 + datetime.timedelta(day=10)
# print(new_date)


# ------------------------------------------------
#                 class_4 
# ------------------------------------------------

# def add(a,b):
#     return a + b


# def sub(a,b):
#     return a - b


# def dev(a,b):
#     return a / b


# def mul(a,b):
#     return a * b



# print(add(a=5, b=2))



#----------------------------------------------------------
#              class-5       

# import math

# r = math.sqrt(16)
# print(r)

# ----------------------------
import os
r = os.getcwd()
print(r)


















