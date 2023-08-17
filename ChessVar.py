class ChessVar:
    def __init__(self):
        """
        Initialize the ChessVar game with the starting position.
        """
        # Initialize an empty 8x8 board
        self.board = [['' for _ in range(8)] for _ in range(8)]

        # Initialize starting positions of pieces
        self.board[0] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        self.board[1] = ['P' for _ in range(8)]
        self.board[6] = ['p' for _ in range(8)]
        self.board[7] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']

        self.turn = 'white'  # White starts the game
        self.game_state = 'UNFINISHED'
        self.move_history = []

    def get_game_state(self):
        """
        Get the current game state.




        """
        return self.game_state

    def make_move(self, from_square, to_square):
        """
        Make a move on the board.



        """
        if self.game_state != 'UNFINISHED':
            return False

        if not self.is_valid_move(from_square, to_square):
            return False

        captured_piece = self.move_piece(from_square, to_square)
        self.update_game_state(to_square)
        self.switch_turn()

        self.move_history.append((from_square, to_square, captured_piece))
        return True

    def is_valid_move(self, from_square, to_square):
        """
        Check if a move is valid.



        """
        if not self.is_within_board(from_square) or not self.is_within_board(to_square):
            return False

        if from_square == to_square:
            return False

        piece = self.board[int(from_square[1]) - 1][ord(from_square[0]) - ord('a')]
        target_piece = self.board[int(to_square[1]) - 1][ord(to_square[0]) - ord('a')]

        # Check if it's the player's turn to move
        if piece.isupper() and self.turn == 'black':
            return False
        if piece.islower() and self.turn == 'white':
            return False


        return True

    def is_within_board(self, square):
        """
        Check if a given square is within the board's boundaries.



        """
        return 'a' <= square[0] <= 'h' and '1' <= square[1] <= '8'

    def move_piece(self, from_square, to_square):
        """
        Move a piece on the board.



        """
        from_rank, from_file = int(from_square[1]) - 1, ord(from_square[0]) - ord('a')
        to_rank, to_file = int(to_square[1]) - 1, ord(to_square[0]) - ord('a')

        piece = self.board[from_rank][from_file]
        captured_piece = self.board[to_rank][to_file]

        self.board[from_rank][from_file] = ''
        self.board[to_rank][to_file] = piece

        return captured_piece

    def update_game_state(self, last_move_square):
        """
        Update the game state based on the last move.



        """
        if last_move_square[1] == '8':
            if self.turn == 'white':
                self.game_state = 'WHITE_WON'
            else:
                self.game_state = 'BLACK_WON'
        elif last_move_square[1] == '7' and self.turn == 'black':
            self.game_state = 'TIE'



    def switch_turn(self):
        """
        Switch the turn to the next player.
        """
        self.turn = 'black' if self.turn == 'white' else 'white'


















 # testing
# Create an instance of the ChessVar class
# chess_game = ChessVar()
#
# # Make some moves
# chess_game.make_move('e2', 'e4')
# chess_game.make_move('e7', 'e5')
# chess_game.make_move('d2', 'd4')
# chess_game.make_move('d7', 'd5')
# chess_game.make_move('e4', 'd5')
# chess_game.make_move('e8', 'd7')
# chess_game.make_move('d1', 'd2')
# chess_game.make_move('c7', 'c5')
# chess_game.make_move('d2', 'd1')
# chess_game.make_move('d7', 'd8')
# chess_game.make_move('d1', 'd2')
# chess_game.make_move('d8', 'e8')
# chess_game.make_move('d2', 'd1')
# chess_game.make_move('e8', 'd8')
# # Get the current game state
# game_state = chess_game.get_game_state()
# print("Current Game State:", game_state)

