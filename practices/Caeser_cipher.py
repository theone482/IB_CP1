# IB 2nd ceaser cipher

while True:
    # get the message and stuff
    message = input("Type your message: ")
    choice = input("Type 1 to encode or 2 to decode: ")
    shift = input("How much to shift the letters?: ")

    # make sure shift is a number
    if not shift.isdigit():
        print("Oops! That shift isn't a number.")
        continue

    shift = int(shift)

    # if decoding, flip the shift
    if choice == "2":
        shift = -shift

    new_message = ""

    for letter in message:
        if letter.isalpha():
            if letter.islower():
                start = ord('a')
            else:
                start = ord('A')
            # move the letter
            new_letter = chr((ord(letter) - start + shift) % 26 + start)
            new_message += new_letter
        else:
            new_message += letter  # keep spaces and stuff

    print("Here’s your new message: " + new_message)

    again = input("Wanna do another one? (yes or no): ")
    if again.lower() != "yes":
        print("Okay bye!")
        break
