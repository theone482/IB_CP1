# IB 2nd flexible calculator

while True:
    print("\nWelcome to the flexible calculator!")
    print("You can do: sum, average, max, min, or product")
    operations = input("What do you want to do? (type 'exit' to quit): ").lower()

    if operations == "exit":
        print("Alright, peace out!")
        break

    print("Start typing numbers (type 'done' when you're finished):")
    numbers = []
    while True:
        entry = input("Enter a number: ")
        if entry.lower() == "done":
            break
        try:
            number = float(entry)
            numbers.append(number)
        except:
            print("Oops, that wasn't a number. Try again.")

    if not numbers:
        print("You didn’t give me any numbers!")
        continue

    if operations == "sum":
        result = sum(numbers)
    elif operations == "average":
        result = sum(numbers) / len(numbers)
    elif operations == "max":
        result = max(numbers)
    elif operations == "min":
        result = min(numbers)
    elif operations == "product":
        result = 1
        for num in numbers:
            result *= num
    else:
        print("Hmm, I don’t know that one.")
        continue

    print(f"Here’s your result for {operations}: {result}")

    #hi
