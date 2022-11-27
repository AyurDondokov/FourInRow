import sys
from map import Map
from game_manager import *
from user_interface import *
from constants import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(GAME_NAME)
clock = pygame.time.Clock()

player_1 = Player("Ayur", COLORS["green"])
player_2 = Player("Ivan", COLORS["red"])
player_3 = Player("Vadim", COLORS["blue"])

text = Text(screen, "", (WIDTH//2, HEIGHT//2), TEXT_SIZE, player_1.get_color)

game_manager = GameManager((player_1, player_2, player_3), COUNT_BLOCKS_FOR_WIN, text, False)
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
