# I'ini Bohnet Calculator
#while true is it to loop it 
while True:
    #this is my instructions
    print("Hello welcome to the calulator. I am going to ask you for two numbers")
    print("After you give me your numbers, you will have the option to choose to take your two numbers")
    print("Your choices are + = add,- = subtract, / = divides, % = divides the numbers and give you the left over, * = multiplication, // = integer division, ** = exponets")
    #these are my inputs and yeah they are put in as a float
    num_1 = float(input("Give me a number: "))
    num_2 = float(input("Give me a number: "))
    choice = input("Here are your options:+,-,/,//,%,*,**:please give me the symbol: ")
    print("Here are your results: ")
    #my if else is where it does the math and it will print like  4 + 5 = 9
    if choice == "+":
        print(f"{num_1} + {num_2} = {num_1 + num_2}")
    elif choice == "-":
        print(f"{num_1} - {num_2} = {num_1 - num_2}")
    elif choice == "/":
        print(f"{num_1} / {num_2} = {num_1 / num_2}")
    elif choice == "//":
        print(f"{num_1} // {num_2} = {num_1 // num_1}")
    elif choice == "%":
        print(f"{num_1} % {num_2} = {num_1 % num_2}")
    elif choice == "*":
        print(f"{num_1} * {num_2} = {num_1 * num_2}")
    elif choice == "**":
        print(f"{num_1} ** {num_2} = {num_1 ** num_2}")
    else:
        print("congratulation you broke my code")
    #here i am asking the user if they want to continue to the code yes or no and if they say yes
    #then the code breaks if they say no then then they reloop it
    exit = input("do you want to end the code(yes or no): ")
    if exit == "yes":
        break
    else:
        print("ok here you go again")