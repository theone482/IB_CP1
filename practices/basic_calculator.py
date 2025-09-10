# IB 2nd basic calculator

first_number = float(input("Enter your first number: "))
second_number = float(input("Enter your second number: "))

addition = round(first_number + second_number, 2)
subtraction = round(first_number - second_number, 2)
multiplication = round(first_number * second_number, 2)
integer_division = rpund(first_number // second_number, 2)

if second_number != 0:
    division = round(first_number / second_number, 2)
else:
    division = "undefined (can't divide by zero)"

print("\nHere are your results:")
print(f"{first_number} + {second_number} = {addition}")
print(f"{first_number} - {second_number} = {subtraction}")
print(f"{first_number} * {second_number} = {multiplication}")
print(f"{first_number} / {second_number} = {division}")
print(f"{first_number} // {second_number} = {integer_division}")
