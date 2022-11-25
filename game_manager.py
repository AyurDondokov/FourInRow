

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
    def __init__(self, players):
        self.__is_playing = False
        self.__players = players

    def start_game(self):
        self.__is_playing = True
        print("Игра началась")

    def end_game(self, player_winner=None):
        self.__is_playing = False
        if player_winner:
            print(f"Победил {player_winner.get_name}")
        else:
            print("Ничья")

