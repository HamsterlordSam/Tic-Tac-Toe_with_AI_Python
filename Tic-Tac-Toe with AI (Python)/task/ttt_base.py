import re


class TicTacToe:
    """create a TicTacToe object for playing tic-tac-toe without bots"""
    game_grid = {}
    grid_fill = 0

    def __init__(self):
        self.game_grid = {"11": ' ', "12": ' ', "13": ' ',
                          "21": ' ', "22": ' ', "23": ' ',
                          "31": ' ', "32": ' ', "33": ' '}

    def game_menu(self, command):
        """receive string command
        return 1 for valid start command
        return -1 for valid exit command
        return 0 otherwise
        """
        if command == 'exit':
            return -1
        if command == 'start':
            return 1
        print("Bad parameters!")
        return 0

    def play(self):
        while True:
            if self.grid_fill % 2 == 0 or self.grid_fill == 0:
                turn = 'X'
            else:
                turn = 'O'
            self.get_user_input(turn)
            if not self.check_state(turn):
                break
        self.reset_game_board()

    def print_game_board(self):
        print("---------")
        for i in range(1, 4):
            print("|", end=" ")
            for j in range(1, 4):
                print(self.game_grid[str(i)+str(j)], end=" ")
            print("|")
        print("---------")

    def reset_game_board(self):
        self.game_grid = {"11": ' ', "12": ' ', "13": ' ',
                          "21": ' ', "22": ' ', "23": ' ',
                          "31": ' ', "32": ' ', "33": ' '}
        self.grid_fill = 0

    def check_rows_columns(self, key):
        """return 1
        for win
        return 0
        otherwise"""
        for i in range(1, 4):
            count_row = 0
            count_column = 0
            for j in range(1, 4):
                if self.game_grid[f'{i}{j}'] == key:
                    count_row += 1
                if self.game_grid[f'{j}{i}'] == key:
                    count_column += 1
            if count_row == 3 or count_column == 3:
                return 1
        return 0

    def check_diagonals(self, key):
        """return 1
        for win
        return 0
        otherwise"""
        if self.game_grid['11'] == key and self.game_grid['22'] == key and self.game_grid['33'] == key:
            return 1
        elif self.game_grid['13'] == key and self.game_grid['22'] == key and self.game_grid['31'] == key:
            return 1
        else:
            return 0

    def check_state(self, key):
        """return 0
        if game over (win or draw)
        return 1
        otherwise"""
        if key == 1:
            key = 'O'
        if key == 0:
            key = 'X'
        if self.grid_fill >= 3:
            if self.check_rows_columns(key) or self.check_diagonals(key):
                print(f"{key} wins")
                return 0
        if self.grid_fill == 9:
            print("Draw")
            return 0
        return 1

    def check_coordinate(self, coord):
        if self.game_grid[coord] == ' ':
            return 1
        else:
            return 0

    def set_coordinate(self, x, y, x_or_o):
        if x_or_o:
            x_or_o = 'O'
        else:
            x_or_o = 'X'
        digits = '[0-9]+'
        if re.match(digits, x) is not None and re.match(digits, y) is not None:
            x = int(x)
            y = int(y)
            if 0 < x < 4 and 0 < y < 4:
                coord = f'{x}{y}'
                if self.check_coordinate(coord):
                    self.game_grid[coord] = x_or_o
                    self.grid_fill += 1
                    self.print_game_board()
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")

    def initial_state(self, state_str):
        template = '[XO_]'
        if len(state_str) == 9 or re.match(template, state_str) is not None:
            i = 0
            for key in self.game_grid:
                if state_str[i] == '_':
                    self.game_grid[key] = ' '
                else:
                    self.game_grid[key] = state_str[i]
                    self.grid_fill += 1
                i += 1
        else:
            print("Please input 9 symbols that are X, O or _  (the latter represents an empty cell)")

    def get_user_input(self, turn):
        try:
            x, y = input("Enter the coordinates:").split()
            self.set_coordinate(x, y, turn)
        except UnboundLocalError:
            print("You should enter numbers!")
        except ValueError:
            print("You should enter numbers!")
