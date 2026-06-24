# I'ini Bohnet hangman
import random

# (day 1) variable list:
# list of possible words
words = ["cactus", "whisper", "lantern", "puzzle", "harbor", "galaxy", "crimson", "voyage", "thicket", "zephyr", "velocity", "quasar", "labyrinth", "cascade", "serendipity", "nebula", "ephemeral", "mirage", "paradox", "solitude", "luminary", "echo", "silhouette", "quicksand", "momentum", "eclipse", "utopia","pinnacle","alchemy","resonance","wanderlust", "zenith", "vigor", "incandescent"]
# body part? => num of wrong guesses
wrong = 0
# guessed letters: list
guessed = []
# specific words for this round : str
word = random.choice(words)
# (day 2) function to print scaffold at correct wrong level (take in the wrong guesses)
# conditional to check level and print the correct image
def print_scaffold(wrong):
# ex:
    if wrong == 0:
        print("""____
|  |
|
|
|
|_____
""")
    elif wrong == 1:
        print("""____
|  |
|  O
|
|
|_____
""")
    elif wrong == 2:
        print("""____
|  |
|  O
| /
|
|_____
""")
    elif wrong == 3:
        print("""____
|  |
|  O
| /|
|
|_____
""")
    elif wrong == 4:
        print("""____
|  |
|  O
| /|\\
|
|_____
""")
    elif wrong == 5:
        print("""____
|  |
|  O
| /|\\
| /
|_____
""")
    elif wrong == 6:
        print("""____
|  |
|  O
| /|\\
| / \\
|_____
""")
    else:
        print("sorry my code broke try again")


# (day 1) function for word display (takes in guessed letters, word)
def word_display(guessed, word):
# variable that has our current display
    display = ""
# look at each letter in the word
    for letter in word:
# check to see if the letter is in the guessed list
        if letter in guessed:
# add the letter to the current display
            display += letter + " "
        else:
# otherwise add an _ to the current display
            display += "_ "
# return the current display
    return display.strip()
# randomly select word from a list of possible words
# while true: (day 2)
while True:
# call function to print the scaffold (day 2)
    print_scaffold(wrong)
# print function to display word (day 2)
    print("Word:", word_display(guessed, word))
# print guessed
    print(f"{guessed}")
#(day2)creat letter variable equal to user input asking for letter (add.strip() and .lower())
    guessed_letter = input("give me a letter: ").strip().lower()
    #(day 2)add letter to guessed letters
    guessed.append(guessed_letter)
    #(day 3)if the letter is not in the world
    if guessed_letter not in word:
        #increase wrong guessed
        wrong += 1
    #(day 3)check if word matches word disaplay function.
    if word == word_display:
        #tell the user they won
        print("you won")
        #stop the loop
        break
    #(day 3)check if 6 wrong guesses
    elif wrong == 6:
        #tell user they lost
        print("you lost")
        #call scaffold function
        print_scaffold
        #show correct word
        print(f"this was the word: {word}")
        #stop the loop
        playagain = input("do you want to play again(yes or no): ")
        if playagain == "no":
            print("thanks for playing")
            break
    else:
        print("")
