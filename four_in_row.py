import sys
import pygame
from map import Map

# Game values
GAME_NAME = "Four in row"
WIDTH = 720
HEIGHT = 720
COUNT_OF_ROWS = 6
COUNT_OF_COLUMNS = 6
FPS = 60
SCREEN_COLOR = (234, 255, 208)

# Pet values

# Forces

# Ways for files

# UI

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()

game_map = Map(screen, (COUNT_OF_ROWS, COUNT_OF_COLUMNS))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            game_map.make_move((255, 0, 0), pygame.mouse.get_pos())

    screen.fill(SCREEN_COLOR)
    clock.tick(FPS)
    game_map.output()
    pygame.display.flip()
