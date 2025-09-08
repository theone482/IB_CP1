# IB 2nd format outputs notes

name = "Eric"
age = 999999999999999999999999999999999999999999999999999999999999999999999999999999

print("hello {}, Nice to meet you!. You are {:,}, that is really old".format(name,age))

name = "Jake"
age = 21

print("hello {}, Nice to meet you!. You are {:b}, that is really old".format(name,age))

name = "Jake"
age = 21

print("hello {}, Nice to meet you!. You are {:E}, that is really old".format(name,age))

name = "Jake"
age = 21
grade = .75

print("hello {}, Nice to meet you!. You are {:b}, that is really old! You have a {:%} in this class".format(name,age, grade))

name = "Jake"
age = 21
grade = .875
money =25
print(f"hello {name}, Nice to meet you! \nYou are {age:b}, that is really old! \nYou have a {grade:%} in this class. \nYou have ${money:.2f}, that is a lot of money")