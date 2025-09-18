# IB 2nd booleans notes!
#boolean only give True or False
over = False

print(over)

name = "LaRose"

print(name.isdecimal()) # if it is just a decimal
print(name.isnumeric()) # if it is just a number
print(name.isalpha()) # if it only has letters
print(name.isupper()) # if all the letters are upper case
print(name.islower()) # if all letters are lower case

name2 = 0.1
print(bool(name2))
# if string is empty bool will look if the varablie has a vaule

import time 

current_time = time.localtime()

print(f"Time: {current_time}")

current_time2 = time.time()
readable_time = time.ctime(current_time2)
print(f"Current time in seconds since jamuary 1 1970(epochtime): {current_time2}")
print(f'Current time: {readable_time}')

import datetime as date

now = date.datetime.now()
hour = now.strftime("%H")
# Month = %m ( %b, %B )
# Day = %d
# Year = %Y,%y
# Hour = %H
#minutes = %M
# secounds = %S

print(f"current time according to datetime: {now}") #doesn't give you the day of the week
print(f"Hour: {hour}") #it gives you just the hour
print(f"My hour variable is a string: {isinstance(hour, str)}")
print(f"My hour variable is a integer: {isinstance(hour, int)}")
print(f"My hour variable is a float: {isinstance(hour, float)}")

now2 = date.datetime.today()
current_hour = now.hour()

print(f"current time according to datetime: {now2}") #doesn't give you the day of the week
print(f"Hour: {current_hour}") #it gives you just the hour
print(f"My hour variable is a string: {isinstance(current_hour, str)}")
print(f"My hour variable is a integer: {isinstance(current_hour, int)}")
print(f"My hour variable is a float: {isinstance(current_hour, float)}")