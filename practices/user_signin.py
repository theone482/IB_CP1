# IB 2nd user sign in
username = "theone482"
password = "300587"
username2 = input("What is your username: ")
password2 = input("What is the password to your username:")

if username2 == username: 
    print(f"{username} is right ")
else:
    print(f"nope wrong username. try again")

if password2 == password:
    print(f"{password} is correct. ")
elif password == "000":
    print(f"Did you forget your password?. try again")
else:
    print("worng password try again.")

if username == username2 and password == password2:
    print("you are signed in")
else:
    print("you didn't get in try again")