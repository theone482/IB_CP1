# IB 2nd elife and logical notes

homework = True
chores = True
room = True

if homework and chores and room :
    print("you can go to your friends house.")
elif not chores or not room:
    print("Do your chores and clean your room!")
else:
    print("go do your homework.")


username = input("enter your username: ")
password = input("enter your password: ")

if username == "mslarose":
    if password == "1234":
        print("welcome ms. LaRose")
    else:
         print("incorrect password")
elif username == "Tia" and password == "Password":
        print("welcome Tia")
elif username == "Andrew" and password == "orange":
        print("welcome Andrew")
else:
        print("that is not a valid sign in.")