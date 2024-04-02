class CheckSpleen:
    def __init__(self):
        # Initialize the game board with an 8x8 grid and populate it with pieces
        self.board = [['-' for _ in range(8)] for _ in range(8)]
        self.populate_board()

    def populate_board(self):
        # Populate the initial pieces on the board
        # 'X' represents one player's pieces, 'O' represents the other player's pieces
        # Empty squares are represented by '-'
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 0:
                    self.board[row][col] = 'X'
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 0:
                    self.board[row][col] = 'O'

    def print_board(self):
        # Print the current state of the game board
        for row in self.board:
            print(' '.join(row))

    def move_piece(self, start, end):
        # Move a piece from the start position to the end position
        start_row, start_col = start
        end_row, end_col = end
        self.board[end_row][end_col] = self.board[start_row][start_col]
        self.board[start_row][start_col] = '-'

    def is_valid_move(self, start, end):
        # Check if a move from the start position to the end position is valid
        start_row, start_col = start
        end_row, end_col = end
        if self.board[start_row][start_col] == '-':
            return False  # Can't move from an empty square
        if self.board[end_row][end_col] != '-':
            return False  # Can't move to a non-empty square
        return True



if __name__ == "__main__":
    # Create a CheckSpleen game instance and print the initial board state
    game = CheckSpleen()
    game.print_board()
