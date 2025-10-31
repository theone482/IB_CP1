# Iv, 2nd period, Turtle Race

import turtle
import random

# --- Function to set up the race ---
def setup_race():
    screen = turtle.Screen()
    screen.setup(width=1000, height=600)
    screen.title("Turtle Race")

    # Draw finish line
    line = turtle.Turtle()
    line.hideturtle()
    line.speed(0)
    line.penup()
    line.goto(450, 250)
    line.right(90)
    line.pendown()
    line.pensize(3)
    line.forward(500)

    # Create turtles
    colors = ["green", "pink", "blue", "red", "purple"]
    positions = [0, 100, 200, -100, -200]
    turtles = []

    for color, y in zip(colors, positions):
        racer = turtle.Turtle(shape="turtle")
        racer.color(color)
        racer.penup()
        racer.goto(-450, y)
        turtles.append(racer)

    return screen, turtles

# --- Function to run the race ---
def race(turtles):
    winner = None
    while not winner:
        for racer in turtles:
            racer.forward(random.randint(1, 10))
            if racer.xcor() >= 450:   # finish line check
                winner = racer
                break
    return winner

# --- Function to announce the winner ---
def announce_winner(winner):
    color = winner.color()[0].capitalize()
    print(f"{color} turtle won!")

    announcer = turtle.Turtle()
    announcer.hideturtle()
    announcer.penup()
    announcer.goto(0, 0)
    announcer.write(f"{color} turtle wins!",
                    align="center", font=("Arial", 24, "bold"))

# --- Main program ---
def main():
    screen, turtles = setup_race()
    winner = race(turtles)
    announce_winner(winner)
    screen.mainloop()

if __name__ == "__main__":
    main()