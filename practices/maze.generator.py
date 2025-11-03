# IB 2nd maze generator
import turtle
import random
def steup_maze():
    screen = turtle.Screen()
    screen.setup(row_grid=6, col_grid=6)
    screen.title("Maze generator")
















def is_soluvion(row_grid, col_grid):
    size = len(row_grid) - 1
    visited = []
    stack = [(0,0)]

    while stack:
        x, y = stack.pop()

        if x == size - 1 and y == size -1:
            return True
        
        if(x, y) in visited:
            continue

        visited.add((x, y))

        if x < size - 1 and col_grid[y][x+1] == "":
            stack.append((x+1, y))


        if y < size - 1 and row_grid[y+1][x] == 0:
            stack.append((x, y+1))

        
        if x > 0 and col_grid[y][x] == 0:
            stack.append((x-1, y))

        if y > 0 and row_grid[y][x] == 0:
            stack.append((x, y-1))