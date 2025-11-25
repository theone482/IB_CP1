#Ib 2nd factorial calculator

# ask user for input"enter #" to make variable for original_num.
original_num = input("Enter a number: ")


#check if user inputed int. # i changed the pseudocode by not checking if  og num can turn into float
def is_integer(value):
    try:
        int(value)   # Try converting to int
        return True
    except ValueError:   # If it fails, it's not an integer
        return False
# Definf factorial_calc()
def factorial_calc(num):
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total
    
    
    #for I in range()< make empthy list = total = num
    #take the num var, and 0-1 it, and print so e.g: 3-1 2-1 1
    #get it tinot a list.
    #when list[num] == 0
        #break
        #while true
while True:
    if is_integer(original_num):
        num = int(original_num)
        print("The factorial of", num, "is", factorial_calc(num))
        break
    else:
        print("Invalid input, try again.")
        original_num = input("Enter a number: ")

    #product(list) or
    #call factorial_calc
factorial_calc()

#  changed 'valuerror' to 'ValueError' because Python requires exact error names
#  removed stray factorial_calc() call at the end since it needs an argument
