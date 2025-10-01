# Ib 2nd fix the game

import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 0  # Start at 0 since no guesses have been made yet
    game_over = False

    while not game_over:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1  # Count each valid guess

        if guess == number_to_guess:
            print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
            game_over = True
        elif guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")

        if attempts >= max_attempts and not game_over:
            print(f"😢 Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True

    print("Game Over. Thanks for playing!")

start_game()
