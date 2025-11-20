# IB 2nd mapping
numbers = [651,984,5619,135,4,6501,68,7,123,54,6,4]
divided= []
for num in numbers:
	divided.append(num/2)
	
def divided(number):
	return number/2

Divided = list(map(lambda num: num/2, numbers))

print(divided)

#For i, num in enumerate(numbers):
	#print(f”{num} divided by 2 is {divided[i]}”)
