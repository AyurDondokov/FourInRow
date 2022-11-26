import time
from constants import *
import pygame.draw

class Block:
    def __init__(self, screen, pos, color=STANDARD_BLOCK_COLOR,
                 size=(WIDTH / COUNT_OF_COLUMNS, HEIGHT / COUNT_OF_ROWS)):
        self.__screen = screen
        self.__position = pos
        self.__color = color
        self.__size = size
        self.__cord_on_scene = (pos[0] * self.__size[0], pos[1] * self.__size[0])
        self.__rect = pygame.Rect(self.__cord_on_scene, self.__size)
        offset_inner = self.__size[0] / 100 * 5
        self.__inner_rect = self.__rect.inflate(-offset_inner, -offset_inner)
        self.__is_colored = False
        self.__whose_block = None

    def output(self):
        pygame.draw.rect(self.__screen, (0, 0, 0), self.__rect)
        pygame.draw.rect(self.__screen, self.__color, self.__inner_rect)

    def change_color(self, player):
        self.__color = player.get_color
        self.__whose_block = player
        self.__is_colored = True

    def make_default(self):
        self.__color = STANDARD_BLOCK_COLOR
        self.__is_colored = False

    @property
    def is_colored(self):
        return self.__is_colored

    @property
    def whose_block(self):
        return self.__whose_block


class Map:
    def __init__(self, screen, size):
        self.__screen = screen
        self.__size = size
        self.__array = [[Block(self.__screen, (column_num, row_num)) for column_num in range(self.__size[0])]
                        for row_num in range(self.__size[1])]

    def output(self):
        for row in range(self.__size[1]):
            for column in range(self.__size[0]):
                self.__array[column][row].output()

    def make_move(self, manager, click_cord):
        block_row = click_cord[0] // (HEIGHT // COUNT_OF_ROWS)
        block_column = click_cord[1] // (WIDTH // COUNT_OF_COLUMNS)
        if not self.__array[block_column][block_row].is_colored:
            self.__array[block_column][block_row].change_color(manager.get_player_who_move)
            if manager.is_falling_blocks:
                self.__remove_block((block_column, block_row), manager)
            else:
                self.__check_of_line((block_column, block_row), manager)
                manager.change_turn()

    def __remove_block(self, block_cord, manager):
        if block_cord[0] + 1 < COUNT_OF_ROWS and not self.__array[block_cord[0] + 1][block_cord[1]].is_colored:
            self.__make_pause()
            self.__array[block_cord[0] + 1][block_cord[1]].change_color(manager.get_player_who_move)
            self.__array[block_cord[0]][block_cord[1]].make_default()
            self.__remove_block((block_cord[0] + 1, block_cord[1]), manager)
        else:
            self.__check_of_line(block_cord, manager)
            manager.change_turn()

    def __make_pause(self):
        self.output()
        pygame.display.flip()
        time.sleep(FALLING_TIME)

    def __check_of_line(self, block_cord, manager):
        directions = [1, 1, 1, 1]
        for i in range(1, manager.count_blocks_for_win):
            directions[0] += self.__check_block_in_step(block_cord, manager, i, 0)
            directions[0] += self.__check_block_in_step(block_cord, manager, -i, 0)
            directions[1] += self.__check_block_in_step(block_cord, manager, 0, i)
            directions[1] += self.__check_block_in_step(block_cord, manager, 0, -i)
            directions[2] += self.__check_block_in_step(block_cord, manager, i, i)
            directions[2] += self.__check_block_in_step(block_cord, manager, -i, -i)
            directions[3] += self.__check_block_in_step(block_cord, manager, -i, i)
            directions[3] += self.__check_block_in_step(block_cord, manager, i, -i)
            for d in range(4):
                if directions[d] >= manager.count_blocks_for_win:
                    manager.end_game(manager.get_player_who_move)
        if manager.is_playing and self.__is_map_full():
            manager.end_game()

    def __check_block_in_step(self, cord, manager, vert, horizon):
        if 0 <= cord[0] + vert < self.__size[0] and 0 <= cord[1] + horizon < self.__size[1] \
                and self.__array[cord[0] + vert][cord[1] + horizon].is_colored \
                and self.__array[cord[0] + vert][cord[1] + horizon].whose_block == manager.get_player_who_move:
            return True
        else:
            return False

    def __is_map_full(self):
        for row in self.__array:
            for block in row:
                if not block.is_colored:
                    return False
        return True
