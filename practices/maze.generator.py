# IB 2nd maze generator
# IB, Period 2, Maze Generator

import turtle
import random

# Maze size
grid = 6
cell = 40

# Setup screen
turtle.setup(grid * cell + 100, grid * cell + 100)
turtle.speed(0)
turtle.hideturtle()
turtle.tracer(0, 0)

# Draw wall
def wall(x1, y1, x2, y2):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)

# Check if maze can be solved
def is_solution(row_grid, col_grid):
    size = len(row_grid)
    visited = set()
    stack = [(0, 0)]

    while stack:
        x, y = stack.pop()

        if x == size - 1 and y == size - 1:
            return True

        if (x, y) in visited:
            continue

        visited.add((x, y))

        if x < size - 1 and col_grid[y][x + 1] == 0:
            stack.append((x + 1, y))
        if y < size - 1 and row_grid[y + 1][x] == 0:
            stack.append((x, y + 1))
        if x > 0 and col_grid[y][x] == 0:
            stack.append((x - 1, y))
        if y > 0 and row_grid[y][x] == 0:
            stack.append((x, y - 1))

    return False

# Make maze
def make_maze():
    row_grid = [[0 for _ in range(grid)] for _ in range(grid)]
    col_grid = [[0 for _ in range(grid)] for _ in range(grid)]

    # Random walls
    for y in range(grid):
        for x in range(grid):
            if x < grid - 1:
                col_grid[y][x + 1] = random.choice([0, 1])
            if y < grid - 1:
                row_grid[y + 1][x] = random.choice([0, 1])

    # Try again if not solvable
    while not is_solution(row_grid, col_grid):
        for y in range(grid):
            for x in range(grid):
                if x < grid - 1:
                    col_grid[y][x + 1] = random.choice([0, 1])
                if y < grid - 1:
                    row_grid[y + 1][x] = random.choice([0, 1])

    return row_grid, col_grid

# Draw maze
def draw_maze(row_grid, col_grid):
    for y in range(grid):
        for x in range(grid):
            sx = x * cell
            sy = y * cell
            if x < grid - 1 and col_grid[y][x + 1] == 1:
                wall(sx + cell, sy, sx + cell, sy + cell)
            if y < grid - 1 and row_grid[y + 1][x] == 1:
                wall(sx, sy, sx + cell, sy)

    # Border
    wall(0, 0, grid * cell, 0)
    wall(0, 0, 0, grid * cell)
    wall(grid * cell, 0, grid * cell, grid * cell)
    wall(0, grid * cell, grid * cell, grid * cell)

# Mark start and end
def mark():
    t = turtle.Turtle()
    t.penup()
    t.color("green")
    t.goto(5, grid * cell - cell + 5)
    t.write("Start", font=("Arial", 12, "bold"))
    t.color("red")
    t.goto(grid * cell - cell + 5, 5)
    t.write("End", font=("Arial", 12, "bold"))
    t.hideturtle()

# Run it
rows, cols = make_maze()
draw_maze(rows, cols)
mark()
turtle.done()
