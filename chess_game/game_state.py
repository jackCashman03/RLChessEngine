"""
Chess Game Module

Implementation of the GameState of the Chess Game.

Author: Jack Cashman
Version: 0.1.0 (not stable)
License: MIT
"""

# Global Constants that define initial location of the pieces.
INIT_WHITE_PAWNS = (1 << 8) | (1 << 9) | (1 << 10) | (1 << 11) | (1 << 12) | (1 << 13) | (1 << 14) | (1 << 15)
INIT_WHITE_KNIGHTS = (1 << 1) | (1 << 6)
INIT_WHITE_BISHOPS = (1 << 2) | (1 << 5)
INIT_WHITE_ROOKS = 1 | (1 << 7)
INIT_WHITE_QUEEN = (1 << 3)
INIT_WHITE_KING = (1 << 4)

INIT_BLACK_PAWNS = (1 << 48) | (1 << 49) | (1 << 50) | (1 << 51) | (1 << 52) | (1 << 53) | (1 << 54) | (1 << 55)
INIT_BLACK_KNIGHTS = (1 << 57) | (1 << 62)
INIT_BLACK_BISHOPS = (1 << 58) | (1 << 61)
INIT_BLACK_ROOKS = (1 << 56) | (1 << 63)
INIT_BLACK_QUEEN = (1 << 59)
INIT_BLACK_KING = (1 << 60)

class GameState:
    def __init__(self,
                 w_pawns=INIT_WHITE_PAWNS,
                 w_knights=INIT_WHITE_KNIGHTS,
                 w_bishops=INIT_BLACK_BISHOPS,
                 w_rooks=INIT_WHITE_ROOKS,
                 w_queen=INIT_WHITE_QUEEN,
                 w_king=INIT_WHITE_KING,
                 b_pawns=INIT_BLACK_PAWNS,
                 b_knights=INIT_BLACK_KNIGHTS,
                 b_bishops=INIT_BLACK_BISHOPS,
                 b_rooks=INIT_BLACK_ROOKS,
                 b_queen=INIT_BLACK_QUEEN,
                 b_king=INIT_BLACK_KING):
        """
        Uses a 64 bit-board representation, where each of the parameters side_piece is an integer representing
        the location of the piece on the board. See: https://pages.cs.wisc.edu/~psilord/blog/data/chess-pages/rep.html
        Note that encoding is left -> right, bottom -> top
        """

        self.w_pawns = w_pawns
        self.w_knights = w_knights
        self.w_bishops = w_bishops
        self.w_rooks = w_rooks
        self.w_queen = w_queen
        self.w_king = w_king

        self.b_pawns = b_pawns
        self.b_knights = b_knights
        self.b_bishops = b_bishops
        self.b_rooks = b_rooks
        self.b_queen = b_queen
        self.b_king = b_king

        # Define a mapping between square names and number to bit-board representation:
        self.notation_mapping = {}
        self.num_mapping = {}

        num = 0
        for n in range(1, 9):
            for l in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                self.notation_mapping[l + str(n)] = (1 << num)
                self.num_mapping[num] = (1 << num)
                num += 1

    def check_legal_move(self):
        pass

    def make_move(self, side, start_loc, end_loc, piece):
        pass

