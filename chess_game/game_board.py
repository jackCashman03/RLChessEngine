"""
Chess Game Module

Implementation of the GameState of the Chess Game.

Author: Jack Cashman
Version: 0.1.0 (not stable)
License: MIT
"""
# Naming conventions (Perhaps you want to call knights as horsies)
PAWNS = 'pawns'
KNIGHTS = 'knights'
BISHOPS = 'bishops'
ROOKS = 'rooks'
QUEEN = 'queen'
KING = 'king'
PIECES = [PAWNS, KNIGHTS, BISHOPS, ROOKS, QUEEN, KING]

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

# Of the form White Kingside, White Queenside, Black Kingside, Black Queenside. 1 if possible. 0 if not.
INIT_CASTLING_RIGHTS = 1 | (1 << 1) | (1 << 2) | (1 << 4)


class GameBoard:
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
                 b_king=INIT_BLACK_KING,
                 whites_turn=True,
                 castling_rights=0,
                 en_passant_square=0):
        """
        Uses a 64 bit-board representation, where each of the parameters side_piece is an integer representing
        the location of the piece on the board. See: https://pages.cs.wisc.edu/~psilord/blog/data/chess-pages/rep.html
        Note that encoding is left -> right, bottom -> top
        """

        self.white_pieces = {PAWNS: w_pawns, KNIGHTS: w_knights, BISHOPS: w_bishops, ROOKS: w_rooks,
                             QUEEN: w_queen, KING: w_king}

        self.black_pieces = {PAWNS: b_pawns, KNIGHTS: b_knights, BISHOPS: b_bishops, ROOKS: b_rooks,
                             QUEEN: b_queen, KING: b_king}

        self.whites_turn = whites_turn
        self.castling_rights = castling_rights
        self.en_passant_square = en_passant_square

        # Define a mapping between square names and number to bit-board representation:
        self.notation_mapping = {}
        self.num_mapping = {}

        num = 0
        for col in range(1, 9):
            for row in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                self.notation_mapping[row + str(col)] = (1 << num)
                self.num_mapping[num] = (1 << num)
                num += 1

    def make_move(self, start_loc: int, end_loc: int):
        """
        Checks if a move is valid, and performs it if possible.
        :param start_loc: Starting square. Indexed left -> right, bottom -> top
        :param end_loc: Ending square. Indexed left -> right, bottom -> top
        :return: -1 if invalid move, 1 if valid move
        """

        # Checks if index is valid
        if not 0 <= start_loc <= 63 or not 0 <= end_loc <= 63:
            return -1

        # Conversion to binary
        start_loc_bin = self.num_mapping[start_loc]
        end_loc_bin = self.num_mapping[end_loc]

        # The type of piece occupying start_loc
        piece_type = None

        # If there is currently a piece of the same colour at end, then break
        if self.whites_turn:
            for piece, info in self.white_pieces.items():
                if info & end_loc_bin > 0:  # There exists a white piece already on this square
                    return -1

                if info & start_loc_bin > 0:    # Type of the piece occupying the square
                    piece_type = piece

        else:
            for piece, info in self.black_pieces.items():
                if info & end_loc_bin > 0:  # There exists a black piece already on this square
                    return -1

                if info & start_loc_bin > 0:    # Type of piece occupying the square
                    piece_type = piece

        # Now, given the piece type, determine whether the transition of start -> end is valid according to indexing
        print(f'The piece at index {start_loc} is {piece_type}')

        if not self.is_valid_move(piece_type, start_loc, end_loc):
            return -1

        # Make the move
        # If there is a piece of the other colour and end_loc, set that piece to low
        pass

        # Change whose turn it is to move
        self.whites_turn = not self.whites_turn

    @staticmethod
    def is_valid_move(piece_type: str, start_loc: int, end_loc: int) -> bool:
        """
        Determines whether a move is valid
        :param piece_type: The piece at start_loc
        :param start_loc: Starting index on the board
        :param end_loc: Finishing index on the board
        :return: Boolean representing whether move is valid or not
        """
        # Left to Right, Bottom from top
        s_row, s_col = start_loc // 8, start_loc % 8
        e_row, e_col = end_loc // 8, end_loc % 8

        d_row = abs(s_row - e_row)
        d_col = abs(s_col - e_col)

        if piece_type == PAWNS:     # TODO: Implement En-Passant movement
            if not():
                return False
        elif piece_type == KNIGHTS:
            if not ((d_row == 1 and d_col == 2) or (d_row == 2 and d_col == 1)):
                return False
        elif piece_type == BISHOPS:     # TODO: Check if something is in the way
            if not (d_row == d_col and d_row != 0):
                return False
        elif piece_type == ROOKS:   # TODO: Check if something is in the way
            if not (d_row == 0 and d_col != 0 or d_row != 0 and d_col == 0):
                return False
        elif piece_type == QUEEN:   # TODO: Check if something is in the way
            if not ((d_row == 0 and d_col != 0 or d_row != 0 and d_col == 0) or (d_row == d_col and d_row != 0)):
                return False
        elif piece_type == KING:    # TODO: Check that the king doesn't move into check
            if not (d_row == 1 or d_col == 1):
                return False

        return True

    def is_checkmate(self) -> bool:
        """
        End of game check
        :return: Boolean representing whether the game is over
        """
        pass

    def is_tied(self) -> bool:
        """
        Checks if the game is tied
        :return: Boolean representing whether the game is tied.
        """
        pass

    def reset(self):
        self.__init__()


a = GameBoard()
print(a.make_move(4, 38))
