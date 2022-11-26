from constants import *


class Player:
    def __init__(self, name, color):
        self.__name = name
        self.__color = color

    @property
    def get_name(self):
        return self.__name

    @property
    def get_color(self):
        return self.__color


class GameManager:
    def __init__(self, players, count_blocks_for_win, ui_text=None, is_falling_blocks=True):
        self.__is_playing = False
        self.__ui_text = ui_text
        self.__count_blocks_for_win = count_blocks_for_win
        self.__is_falling_blocks = is_falling_blocks
        self.__players = players
        self.__turn = 0

    def change_turn(self):
        if self.__turn + 1 == len(self.__players):
            self.__turn = 0
        else:
            self.__turn += 1

    def start_game(self):
        self.__is_playing = True
        print("Игра началась")
        if self.__ui_text:
            self.__ui_text.change_text("")

    def end_game(self, player_winner=None):
        self.__is_playing = False
        if player_winner:
            text_output = f"Победил {player_winner.get_name}"
            text_color = player_winner.get_color
        else:
            text_output = "Ничья"
            text_color = BLACK
            print(text_output)
        if self.__ui_text:
            self.__ui_text.change_color(text_color)
            self.__ui_text.change_text(text_output)

    @property
    def get_player_who_move(self):
        return self.__players[self.__turn]

    @property
    def is_playing(self):
        return self.__is_playing

    @property
    def is_falling_blocks(self):
        return self.__is_falling_blocks

    @property
    def count_blocks_for_win(self):
        return self.__count_blocks_for_win

    @property
    def get_ui_text(self):
        return self.__ui_text
