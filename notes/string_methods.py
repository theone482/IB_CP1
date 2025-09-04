# IB 2nd strings methods notes

name = input("What is your name").strip().title()
# .lower() => makes it all lower case
# .upper() => all upper case
#.capitalize() => capitalizes the first letter
# .title() => capita;izes the first letter of every word

print("hello "+ name +", it is nice to meet You!")

age = input("bro how old are you")

print(age.isdigit())

print("really? "+ age + "is old")

sentence = "The quick brown fox jumps pver the lazy dog"

word = "brown"
start = sentence.find("fox")
length = len("fox")
print(sentence.replace(word, "yellow"))
age =int(input("Bro how ld are you?"))
print("hello {} , it is nice to meet You! I can't believe you are{:%}".format(name,age))


print(f"hello {name} , it is nice to meet You! I can't believe you are{age:.1f}".format(name,age))
