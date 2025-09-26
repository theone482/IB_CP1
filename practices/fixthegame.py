# Ib 2nd fix the game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0
    game_over = False
    while not game_over:
        guess = input("Enter your guess: ")
        guess = int(guess) # I made the guess a int so the code won't be confused and it will be supported
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess < number_to_guess: # i switch the less thena nd greater then  because if it was no greater then it would get stick for me
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")  
        continue
    print("Game Over. Thanks for playing!")
start_game()