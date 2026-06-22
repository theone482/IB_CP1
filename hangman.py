# I'ini Bohnet hangman
import random
#(day 1)variable list:
#list of possiable words
words = ["cactus", "whisper", "lantern", "puzzle", "harbor", "galaxy", "crimson", "voyage", "thicket", "zephyr"]
#body part? => num of wrong guesses
wrong = []
#guessed letters: list
guessed = []
# specific words for this round : str
word = random.choice(words)


#(day 2)function to print scaffold at correct wrong level(take in the wrong guesses)
def scaffold(wrong): 
#conditional to cheach levke and print the correct image
    if wrong == 0:
        print("""____
            #|   |
            #|   
            #|  
            #|  
            #|_____
        # """)
    elif wrong == 1:
        print("""____
            #|   |
            #|   O
            #|  
            #|  
            #|_____
        # """)
    elif wrong == 2:
        print("""____
            #|   |
            #|   O
            #|  /
            #|  
            #|_____
        # """)
    elif wrong == 3: 
        print("""____
            #|   |
            #|   O
            #|  /|
            #|  
            #|_____
        # """)
    elif wrong == 4:
        print("""____
            #|   |
            #|   O
            #|  /|\\
            #|  
            #|_____
        # """)
    elif  wrong == 5:
        print("""____
            #|   |
            #|   O
            #|  /|\\
            #|  / 
            #|_____
        # """)
    elif wrong == 6:
        print("""____
            #|   |
            #|   O
            #|  /|\\
            #|  / \\
            #|_____
        # """)
    else:
        print("sorry my code broke try again")

#(day 1)function for word display (takes in guesses letters, word)
def word_display(guessed, word):
    print("hi")
    # variable thst has our current display
    # look at each letter in the word
        # check to see if the letter is in the guessed letter
    if guessed_letter in guessed:
        # add the letter to the current display
        print("hi")
    #otherwise
    else:
    # add an _ to the current display    
        print("hi")
    
    return 
    # return the current display

# randomly selet word from a list of possible words
#while true: (day 2)
while True:
    # call function to print the scaffold(day2)
    scaffold
    # print function to display word(day 2)
    print(word_display(guessed,word))
    #print guessed letters variables(day 2)

    #(day2)creat letter variable equal to user input asking for letter (add.strip() and .lower())
    guessed_letter = input("give me a letter: ").strip().lower()
    #(day 2)add letter to guessed letters
    
    #(day 3)if the letter is not in the world
    if guessed_letter != word:
        #increase wrong guessed
        wrong += 1

    #(day 3)check if word matches word disaplay function.
    if word == word_display:
        #tell the user they won
        print("you won")
        #stop the loop
        #break
    #(day 3)check if 6 wrong guesses
    elif wrong == 6:
        #tell user they lost
        print("you lost")
        #call scaffold function

        #show correct word
        print({word})
        #stop the loop
        #break
    else:
        print("you broke my code, congrats")
