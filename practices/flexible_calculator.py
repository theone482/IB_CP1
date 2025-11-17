# IB 2nd flexible calculator

while True:
    print("Welcome to the flexible calculator!")
    print("Available operations: sum, average, max, min, product")
    operations = input("which operations would you like to perform?: ")
    if operations == "sum" :
        print("enter numbers (type 'done' when finished):")
        num_1sum = input("first number: ")
        num_2sum = input("second number: ")
        num_3sum = input("third number: ")
        num_4sum = input("fourth number: ")
        num_5sum = input("fifith number: ")
        cal_sum = num_1sum + num_2sum + num_3sum + num_4sum +num_5sum
        print(cal_sum)