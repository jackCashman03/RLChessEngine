from chess_game.game_board import *
from chess_game.game_board import GameBoard


class Engine:
    def __init__(self, colour):
        self.colour = colour    # Whether the engine is black or white

    def generate_possible_moves(self, game_board: GameBoard) -> list:
        """
        Generates a list of all possible moves
        :param game_board: The game_board for moves to be calculated on
        :raises ValueError: If the board passed is not the Engines turn to make a move
        :return: Provides all possible moves of the form (start_loc, end_loc)
        """
        pass

    def eval(self, game_board: GameBoard) -> float:
        """
        Estimates the value of the current game state
        :param game_board: The game_board to be evaluated
        :return: An estimate of how desirable the current position is
        """
        pass

    def make_move(self, game_board: GameBoard) -> (int, int):
        """
        Uses MinMax algorithm to make a move on the board
        :param game_board: The game_board to make a move on
        :return: (start_loc, end_loc) move on the board
        """
        # Use the min_max algorithm
        pass
