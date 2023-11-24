"""
Evaluation function for MinMax Algorithm

Author: Jack Cashman
Version: 0.1.0 (not stable)
License: MIT
"""

# Imports
from game_board import GameBoard

def eval(game_board: GameBoard) -> float:
    """
    Evaluation function for MinMax algorithm
    :param game_board: The Chess Board to be evluated
    :return: quantitative measure or how desirable the board state is
    """
    return -1