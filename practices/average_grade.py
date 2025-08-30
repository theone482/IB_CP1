# IB 2nd grade average grade
# Collect grades for each period
period_1 = int(input("Hey, what is your grade in your first period?\n"))
period_2 = int(input("What is your grade in second period?\n"))
period_3 = int(input("What is your grade in third period?\n"))
period_4 = int(input("What is your grade in fourth period?\n"))
period_5 = int(input("What is your grade in fifth period?\n"))
period_6 = int(input("What is your grade in sixth period?\n"))
period_7 = int(input("What is your grade in seventh period?\n"))

# Calculate average
total = period_1 + period_2 + period_3 + period_4 + period_5 + period_6 + period_7
grade_average = round(total / 7, 2)

# Display result
print("Your grade average is:", grade_average)
