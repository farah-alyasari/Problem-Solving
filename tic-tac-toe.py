'''
Software Requirement Specification – Tic Tac Toe Game

1.	Introduction
1.1.	Purpose: The tic-tac-toe game demonstrate skills in using Python for solving complex problems by integrating programming techniques in one program consisting of various parts.
1.2.	Intended Audience: the SRS document is to be accessible by the General public through GitHub
1.3.	Intended Use: the source code can used per the license for this project. The license is available in the project folder
1.4.	Scope: the goal of this project is developing a console software application to play tic-tac-toe with the end-user 
2.	Overall Description
2.1.	User Needs
2.1.1.	The computer should play the game using the ‘X’ symbol
2.1.2.	The user should play the game using the ‘O’ symbol
2.1.3.	The first move belongs to the computer
2.1.4.	The computer picks a first move in a pseudorandom approach 
2.1.5.	All squares are numbered row by row starting with ‘1’ and ending with ‘9’
2.1.6.	The user inputs their move by entering the number of the square they choose - the number must be valid. It must be an integer, it must be greater than ‘0’ and less than ‘10’, and it cannot point to a field which is already occupied.
2.1.7.	The program checks if the game is over, and decided to continue the game, end the game with one side wining, or end the game because there is a tie between the computer and the player
2.2.	Dependencies
2.2.1.	The user needs to have a Python interpreter installed on the machine to execute the program
2.3.	Activity diagram representing one game session

3.	System Features and Requirements
3.1.	Functional Requirements
3.1.1.	If the user inputs an integer outside the minimum and the maximum allowed row number, then the program must warn the user and give the user another chance to give an input
3.1.2.	If the user inputs a value for an already occupied field, the program must warn the user and give the user another chance to give an input
3.1.3.	If the user inputs a non-integer value,  the program must warn the user and give the user another chance to give an input
3.1.4.	If the user wants inputs “Ctrl + C” to exit the program, the program must exit gracefully by not giving an error
3.2.	External Interface Requirements 
3.2.1.	The padding for the board game must be symmetrical across the x-axis and symmetrical across the y-axis
3.3.	Nonfunctional requirements  
3.3.1.	The code for the program must meet PEP8 standards with at least 95 % rating

'''

# author: farah alyasari


# packages
import random
import sys

# make an empty board
board = [[3 * j + i + 1 for i in range(3)] for j in range(3)]
min = 1
max = 9
player_symbol = "O"
computer_symbol = "X"

#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#


def DisplayBoard(board):
    print("+-------" * 3, "+", sep="")
    for row in range(3):
        print("|       " * 3, "|", sep="")
        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")
        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")

#
# the function accepts the board current status,
# asks the user about their move,
# checks the input and updates the board according to the user's decision,
# the number must be valid and cannot point to a field that's already occupied
#


def EnterMove(board):
    move = 0
    enteredMove = True
    while enteredMove is True:
        try:
            move = int(input("Pick a move: "))
            assert move <= max and move >= min
        except AssertionError:
            print("Illegal move")
        except ValueError:
            print("Illegal value")
        except KeyboardInterrupt:
            print("Okay, bye")
            sys.exit()
        except BaseException as e:
            print(e)
        for row in board:
            if move in row:
                move_position = row.index(move)
                row[move_position] = player_symbol
                enteredMove = False
        else:
            print("Sorry, ", move, " is occupied")


#
# Browses the board and builds a list of all the free squares;
# list consists of tuples, while each tuple is a pair of row and column numbers
#

def MakeListOfFreeFields(board):
    list = []
    for row in board:
        for col in row:
            if col != player_symbol and col != computer_symbol:
                row_position = board.index(row)
                col_position = row.index(col)
                list.append((row_position, col_position))
    return list

#
# the function analyzes the board status in order to check if
# the player using the specified symbol has won the game
#


def VictoryFor(board, symbol):
    # check if there's a win
    cross_1 = cross_2 = True
    for rc in range(3):
        # checking each possible row combination
        if (board[rc][0] == symbol and
            board[rc][1] == symbol and
                board[rc][2] == symbol):
            return True
        # check each column
        if (board[0][rc] == symbol and
            board[1][rc] == symbol and
                board[2][rc] == symbol):
            return True
        # check the diagnols
        if board[rc][rc] != symbol:
            cross_1 = False
        if board[2 - rc][2 - rc] != symbol:
            cross_2 = False
    if cross_1 or cross_2:
        return True
    return False

#
# the function draws the computer's move and updates the board
# it randomly generates a move based on the available position
#


def DrawMove(board):
    try:
        sequence = MakeListOfFreeFields(board)
        move = random.choice(sequence)
        row = move[0]
        col = move[1]
        board[row][col] = computer_symbol
    except IndexError:
        print("The game should have ended. We shouldn't reach here")
    except BaseException:
        print("unkown error. We shouldn't reach here")

#
# Program entry and program exit
#


def TicTacToe(board):
    free_fields = MakeListOfFreeFields(board)
    computer_turn = True
    computer_status = False
    player_status = False
    while(len(free_fields) > 0):
        if computer_turn:
            print("computer turn: ")
            DrawMove(board)
            computer_status = VictoryFor(board, computer_symbol)
        else:
            EnterMove(board)
            player_status = VictoryFor(board, player_symbol)
        # check victory
        if player_status is True:
            DisplayBoard(board)
            print("You won")
            break
        if computer_status is True:
            DisplayBoard(board)
            print("Computer won")
            break
        computer_turn = not computer_turn
        free_fields = MakeListOfFreeFields(board)
        DisplayBoard(board)
    if computer_status is False and player_status is False:
        print("Tie")


TicTacToe(board)
