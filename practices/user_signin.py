# IB 2nd user sign in

username = input("What is your username: ")
password = input("What is the password to your username:")

if username == "theone482": 
    print(f"hey that is not your it is mine")
elif username == username:
    print(f"welcome {username}")
else:
    print("what. this shouldn't happened")

if password == password:
    print(f"So {password} is your password, thanks for giving me your password.")
elif password == "000":
    print(f"maybe you should change your password it is too easy.")
else:
    print("whattt. This sholdn't have happened.")