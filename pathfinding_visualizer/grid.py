import random
import pygame

from colors import WHITE, GREY
from node import Spot


def make_grid(rows, width):
    grid = []
    gap = width // rows

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)

    return grid


def generate_maze(grid):
    for row in grid:
        for spot in row:
            if random.random() < 0.3:
                spot.make_barrier()


def draw_grid(win, rows, width):
    gap = width // rows

    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width, algo):
    win.fill(WHITE)

    for row in grid:
        for spot in row:
            spot.draw(win)

    draw_grid(win, rows, width)

    font = pygame.font.SysFont("arial", 20)
    text = font.render(f"Algorithm: {algo}", True, (0, 0, 0))
    win.blit(text, (10, 10))

    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    x, y = pos

    col = x // gap
    row = y // gap

    return row, col
