import sys


class TicTacToe:
    def __init__(self):
        self.table_array = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.table = f'''---------
|       |
|       |
|       |
---------'''
        print(self.table)  # prints en empty table and the beginning
        self.game()

    def game(self):
        winning_combinations = [[[0, 0], [0, 1], [0, 2]], [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]],
                                [[0, 0], [1, 0], [2, 0]], [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]],
                                [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]]]
        table_array = self.table_array
        xs = 0
        os = 0
        while True:
            input_coordinates = input('Enter the coordinates:').split(' ')
            coordinate1 = int(input_coordinates[1]) - 1
            coordinate2 = int(input_coordinates[0]) - 1
            if coordinate1 == 0:
                coordinate1 += 2
            elif coordinate1 == 2:
                coordinate1 -= 2  # translates human coordinates format to the list format
            if not input_coordinates[0].isdigit() or not input_coordinates[1].isdigit:
                print('You should enter numbers!')  # checks if input coordinate is a number
            elif 1 < int(input_coordinates[0]) > 3 or 1 < int(input_coordinates[1]) > 3:
                print('Coordinates should be from 1 to 3!')  # checks if input coordinate is in valid range
            elif table_array[coordinate1][coordinate2] == 'X' or table_array[coordinate1][coordinate2] == 'O':
                print('This cell is occupied! Choose another one!')  # checks if chosen cell is empty
            elif table_array[coordinate1][coordinate2] == ' ':
                if xs <= os:
                    table_array[coordinate1][coordinate2] = 'X'  # assignment to the specific cell
                    xs += 1
                else:
                    table_array[coordinate1][coordinate2] = 'O'  # assignment to the specific cell
                    os += 1
            print(f'''---------
| {table_array[0][0]} {table_array[0][1]} {table_array[0][2]} |
| {table_array[1][0]} {table_array[1][1]} {table_array[1][2]} |
| {table_array[2][0]} {table_array[2][1]} {table_array[2][2]} |
---------''')  # prints table after player's move
            for combination in winning_combinations:  # checks if there's a winning combination on the table
                if all([table_array[coordinates[0]][coordinates[1]] == 'X' for coordinates in combination]):
                    print('X wins')
                    sys.exit()
                elif all([table_array[coordinates[0]][coordinates[1]] == 'O' for coordinates in combination]):
                    print('O wins')
                    sys.exit()
            if Xs + Os == 9:  # Draw if the table is full and there's no winning combination
                print('Draw')
                sys.exit()


play = TicTacToe()
play.game()
