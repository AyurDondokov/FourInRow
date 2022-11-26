import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Text:
    def __init__(self, screen, text,  cord, size, color, back_color=WHITE, font_way=None):
        self.__screen = screen
        self.__color = color
        self.__back_color = back_color
        self.__cord = cord
        self.__font = pygame.font.Font(font_way, size)
        self.__text = self.__font.render(text, False, color)
        self.__rect = self.__text.get_rect(center=self.__cord)

    def out(self):
        pygame.draw.rect(self.__screen, self.__back_color, self.__rect)
        self.__screen.blit(self.__text, self.__rect)

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = self.__font.render(text, False, self.__color)
        self.__rect = self.__text.get_rect(center=self.__cord)

    def change_text(self, text):
        self.__text = self.__font.render(text, False, self.__color)
        self.__rect = self.__text.get_rect(center=self.__cord)

    def change_color(self, color):
        self.__color = color
