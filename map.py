
import pygame.draw, time

# Game values
WIDTH = 720
HEIGHT = 720
COUNT_OF_ROWS = 6
COUNT_OF_COLUMNS = 6
STANDARD_BLOCK_COLOR = (50, 50, 50)


class Block:
    def __init__(self, screen, pos, color=STANDARD_BLOCK_COLOR):
        self.__screen = screen
        self.__position = pos
        self.__color = color
        self.__width = WIDTH/COUNT_OF_COLUMNS
        self.__height = HEIGHT/COUNT_OF_ROWS
        self.__size = (self.__width, self.__height)
        self.__cord_on_scene = (pos[0] * self.__width, pos[1] * self.__height)
        self.__rect = pygame.Rect(self.__cord_on_scene, self.__size)
        self.__inner_rect = self.__rect.inflate(-10, -10)
        self.__is_colored = False

    def output(self):
        pygame.draw.rect(self.__screen, (0, 0, 0), self.__rect)
        pygame.draw.rect(self.__screen, self.__color, self.__inner_rect)

    def change_color(self, color):
        self.__color = color
        self.__is_colored = True

    def make_default(self):
        self.__color = STANDARD_BLOCK_COLOR
        self.__is_colored = False

    @property
    def is_colored(self):
        return self.__is_colored

class Map:
    def __init__(self, screen, size):
        self.__screen = screen
        self.__size = size
        self.__array = [[Block(self.__screen, (column_num, row_num)) for column_num in range(self.__size[0])] for row_num in range(self.__size[1])]

    def output(self):
        for row in range(self.__size[1]):
            for column in range(self.__size[0]):
                self.__array[column][row].output()

    def make_move(self, player, click_cord):
        block_row = click_cord[0] // (HEIGHT//COUNT_OF_ROWS)
        block_column = click_cord[1] // (WIDTH//COUNT_OF_COLUMNS)
        if not self.__array[block_column][block_row].is_colored:
            self.__array[block_column][block_row].change_color(player)
            self.remove_block((block_column, block_row), player)

    def remove_block(self, block_cord, player):
        if block_cord[0]+1 < COUNT_OF_ROWS and not self.__array[block_cord[0]+1][block_cord[1]].is_colored:
            self.__array[block_cord[0] + 1][block_cord[1]].change_color(player)
            self.__array[block_cord[0]][block_cord[1]].make_default()
            self.remove_block((block_cord[0] + 1, block_cord[1]), player)


