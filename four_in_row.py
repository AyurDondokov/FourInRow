import sys
import pygame
from map import Map
from game_manager import *
from user_interface import *

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

player_1 = Player("Ayur", (0, 255, 0))
player_2 = Player("Ivan", (255, 0, 0))

text = Text(screen, "", (WIDTH//2, HEIGHT//2), 50, player_1.get_color)

game_manager = GameManager((player_1, player_2), 4, text)
game_map = Map(screen, (COUNT_OF_ROWS, COUNT_OF_COLUMNS))

game_manager.start_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game_manager.is_playing:
                game_map.make_move(game_manager, pygame.mouse.get_pos())

    screen.fill(SCREEN_COLOR)
    clock.tick(FPS)
    game_map.output()
    game_manager.get_ui_text.out()
    pygame.display.flip()
