import random
from ttt_base import TicTacToe


def main():
    tic_tac_toe = TicTacToeAI()
    while True:
        menu_loop = tic_tac_toe.game_menu(input("Input command:").split())
        if menu_loop == 1:
            tic_tac_toe.play()
        if menu_loop == -1:
            break


class TicTacToeAI(TicTacToe):
    """create TicTacToeAI object for playing tic-tac-toe with easy, medium and hard AI"""
    player_one = ' '
    player_two = ' '
    ai_flag = ' '
    ai_game_board = {}
    ai_grid_fill = 0

    def game_menu(self, *args):
        command = args[0][0]
        game_modes = ["user", "easy", "medium", "hard"]
        if command == 'exit':
            return -1
        if command == 'start':
            if len(args[0]) == 3:
                if args[0][1] in game_modes and args[0][2] in game_modes:
                    self.player_one = args[0][1]
                    self.player_two = args[0][2]
                    self.print_game_board()
                    return 1
        print("""'start' command must be structured like following: start player player
player = user, easy, medium or hard
'exit' command does NOT require parameters""")

    def play(self):
        while True:
            if self.grid_fill % 2 == 0 or self.grid_fill == 0:
                turn = 0
                self.player_move(self.player_one, turn)
            else:
                turn = 1
                self.player_move(self.player_two, turn)
            if not self.check_state(turn):
                break
        self.reset_game_board()

    @staticmethod
    def get_empty_spaces(board):
        """return a list of empty positions on the game board"""
        return [key for key in board if board[key] == ' ']

    def check_rows_columns(self, key):
        """return 1
        for win
        return 0
        otherwise"""
        for i in range(1, 4):
            count_row = 0
            count_column = 0
            flag_row = ' '
            flag_col = ' '
            for j in range(1, 4):
                if self.game_grid[f'{i}{j}'] == key:
                    count_row += 1
                if self.game_grid[f'{i}{j}'] == ' ':
                    flag_row = f'{i}{j}'
                if self.game_grid[f'{j}{i}'] == key:
                    count_column += 1
                if self.game_grid[f'{j}{i}'] == ' ':
                    flag_col = f'{j}{i}'
            if count_row == 3 or count_column == 3:
                return 1
            if count_row == 2 and flag_row != ' ':
                self.ai_flag = flag_row
            if count_column == 2 and flag_col != ' ':
                self.ai_flag = flag_col
        return 0

    def check_diagonals(self, key):
        """return 1
        for win
        return 0
        otherwise"""
        count_first_diag = 0
        count_second_diag = 0
        flag_first = ' '
        flag_second = ' '
        for i in range(1, 4):
            if self.game_grid[f'{i}{i}'] == key:
                count_first_diag += 1
            if self.game_grid[f'{i}{i}'] == ' ':
                flag_first = f'{i}{i}'
            if self.game_grid[f'{i}{4-i}'] == key:
                count_second_diag += 1
            if self.game_grid[f'{i}{4-i}'] == ' ':
                flag_second = f'{i}{4-i}'
            if count_first_diag == 3 or count_second_diag == 3:
                return 1
            if count_first_diag == 2 and flag_first != ' ':
                self.ai_flag = flag_first
            if count_second_diag == 2 and flag_second != ' ':
                self.ai_flag = flag_second
        return 0

    def player_move(self, player, turn):
        if player == 'user':
            self.get_user_input(turn)
        elif player == 'easy':
            self.easy_bot(turn)
        elif player == 'medium':
            self.medium_bot(turn)
        elif player == 'hard':
            self.hard_bot(turn)

    def easy_bot(self, turn):
        print('Making move level "easy"')
        empty_spaces = self.get_empty_spaces(self.game_grid)
        choice = random.choice(empty_spaces)
        self.set_coordinate(choice[0], choice[1], turn)

    def medium_bot(self, turn):
        print('Making move level "medium"')
        if turn != 0:
            self.check_state(0)
        if turn != 1:
            self.check_state(1)
        self.check_state(turn)
        if self.ai_flag != ' ':
            self.set_coordinate(self.ai_flag[0], self.ai_flag[1], turn)
        else:
            empty_spaces = self.get_empty_spaces(self.game_grid)
            choice = random.choice(empty_spaces)
            self.set_coordinate(choice[0], choice[1], turn)
        self.ai_flag = ' '

    @staticmethod
    def check_coordinate_ai(game_board, coord):
        if game_board[coord] == ' ':
            return 1
        else:
            return 0

    def set_coordinate_ai(self, coord, game_board, turn):
        """ return game board update for minimax algorithm, after setting a coordinate"""
        if turn:
            turn = 'O'
        else:
            turn = 'X'
        if self.check_coordinate_ai(game_board, coord):
            game_board[coord] = turn
        return game_board

    @staticmethod
    def unset_coordinate_ai(coord, game_board):
        """ return game board update for minimax algorithm, after removing a coordinate"""
        game_board[coord] = ' '
        return game_board
    
    def check_rows_columns_ai(self, game_board, key):
        """return 1
        for win
        return 0
        otherwise
        (used for minimax algo)"""
        for i in range(1, 4):
            count_row = 0
            count_column = 0
            flag_row = ' '
            flag_col = ' '
            for j in range(1, 4):
                if game_board[f'{i}{j}'] == key:
                    count_row += 1
                if game_board[f'{i}{j}'] == ' ':
                    flag_row = f'{i}{j}'
                if game_board[f'{j}{i}'] == key:
                    count_column += 1
                if game_board[f'{j}{i}'] == ' ':
                    flag_col = f'{j}{i}'
            if count_row == 3 or count_column == 3:
                return 1
            if count_row == 2 and flag_row != ' ':
                self.ai_flag = flag_row
            if count_column == 2 and flag_col != ' ':
                self.ai_flag = flag_col
        return 0

    def check_diagonals_ai(self, game_board, key):
        """return 1
        for win
        return 0
        otherwise
        (used for minimax algo)"""
        count_first_diag = 0
        count_second_diag = 0
        flag_first = ' '
        flag_second = ' '
        for i in range(1, 4):
            if game_board[f'{i}{i}'] == key:
                count_first_diag += 1
            if game_board[f'{i}{i}'] == ' ':
                flag_first = f'{i}{i}'
            if game_board[f'{i}{4 - i}'] == key:
                count_second_diag += 1
            if game_board[f'{i}{4 - i}'] == ' ':
                flag_second = f'{i}{4 - i}'
            if count_first_diag == 3 or count_second_diag == 3:
                return 1
            if count_first_diag == 2 and flag_first != ' ':
                self.ai_flag = flag_first
            if count_second_diag == 2 and flag_second != ' ':
                self.ai_flag = flag_second
        return 0

    def check_state_ai(self, game_board, grid_fill, key):
        """return 0
        if game over (win)
        return -1
        if game over (draw)
        return 1
        otherwise
        (used for minimax algo)"""
        if key:
            key = 'O'
        else:
            key = 'X'
        if grid_fill >= 3:
            if self.check_rows_columns_ai(game_board, key) or self.check_diagonals_ai(game_board, key):
                return 0
        if grid_fill == 9:
            return -1
        return 1
    
    def minimax(self, turn, turn_ai, ai_game_board, grid_fill):
        """Implementation of the minimax algorithm for tic-tac-toe

        Return scores for the moves that can be done by the hard bot
        """
        state = self.check_state_ai(ai_game_board, grid_fill, turn)
        if state == -1:
            return 0
        if turn != turn_ai and state == 0:  # AI loses
            return -10
        if turn == turn_ai and state == 0:  # AI wins
            return 10
        empty_spaces = self.get_empty_spaces(ai_game_board)
        scores = []
        turn ^= 1  # toggle turns between hard bot and opponent
        grid_fill += 1
        # depth -= 10
        for empty_space in empty_spaces:
            self.set_coordinate_ai(empty_space, ai_game_board, turn)
            scores.append(self.minimax(turn, turn_ai, ai_game_board, grid_fill))
            self.unset_coordinate_ai(empty_space, ai_game_board)
        if turn == turn_ai:
            return max(scores)
        if turn != turn_ai:
            return min(scores)

    def hard_bot(self, turn):
        print('Making move level "hard"')
        empty_spaces = self.get_empty_spaces(self.game_grid)
        if self.grid_fill == 0:
            self.set_coordinate('2', '2', turn)
        else:
            self.ai_game_board = self.game_grid.copy()
            self.ai_grid_fill = self.grid_fill
            scores = []
            best_move = 0
            for i in range(0, len(empty_spaces)):
                self.set_coordinate_ai(empty_spaces[i], self.ai_game_board, turn)
                self.ai_grid_fill += 1
                scores.append(self.minimax(turn, turn, self.ai_game_board, self.ai_grid_fill))
                self.ai_game_board = self.game_grid.copy()
                self.ai_grid_fill = self.grid_fill
                if scores[i] > scores[best_move]:
                    best_move = i
            self.set_coordinate(empty_spaces[best_move][0], empty_spaces[best_move][1], turn)
            

if __name__ == "__main__":
    main()
