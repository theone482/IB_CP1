# IB 2nd idiot proof
name = input("What is your full name: ").strip().title()

phone = input("And what is your number (e.g., 1234567890): ").strip()
# Format phone as spaced sets: 123 456 7890
formatted_phone = f"{phone[:3]} {phone[3:6]} {phone[6:]}"

gpa = float(input("Soooo what is your GPA? :) : \n "))
formatted_gpa = round(gpa, 1)

print("Hi", name, "I'm Emma")
print("Your number is:", formatted_phone)
print("Your GPA is:", formatted_gpa)

