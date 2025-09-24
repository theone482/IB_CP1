# IB 2nd what is my grade

grade = float(input(f"what is your grade in CP1 :"))

if grade >= 90:
    print(f"Your grade is A in CP1 with a {grade:.2f}%")
elif grade >= 80:
    print(f"your grade is a B in CP1 with a {grade:.2f}%")
elif grade >= 70:
    print(f"Your grade is C in CP1 with a {grade:.2f}%")
elif grade >= 60:
    print(f"your grade is a D in CP1 with a {grade:.2f}%")
elif grade >= 0:
    print(f"You failed in CP1 with a F with a {grade:.2f}%")
else:
    print(f"you did something wrong")