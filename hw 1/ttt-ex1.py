import random

#subproblems to complete to write the program:
#print current state of the board
#main loop for input
#updated board (save and display)
#who won

#INPUT:must pass in a dictionary with directions as the keys(NW,N,NE,W,E,C,SW,S,SE) with c as the center and the values x,o,or ""
#OUTPUT: string representation of the board
def board(input):
    return """
   |      |
{}  |  {}   |  {}
------------------
   |      |
{}  |  {}   |  {}
------------------
   |      |
{}  |  {}   |  {}
    """.format(input['NW'],input['N'],input['NE'],input['W'],input['C'],input['E'],input['SW'],input['S'],input['SE'])
empty_board={'NW':" ",'N':" ",'NE':" ",'W':" ",'E':" ",'C':" ",'SW':" ",'S':" ",'SE':" "}

#INPUT: input (string) variable represents the direction typed in, current_board (dictionary) variable represents the current state of the board
#OUTPUT: if the user does not enter a valid direction or pick an empty spot then it will print pick a direction or pick an empty spot and returns False. If the move is valid it returns true
def valid_move(direction,current_board):

    if direction not in empty_board: #checks if the user picked a valid direction
        print ('pick a direction')
        return False
    if current_board[direction]!=" ": #checks if the user picked an empty spot
        print('pick an empty spot')
        return False
    return True

#INPUT: input (string) variable represents the direction typed in, current_board (dictionary) variable represents the current state of the board, player is a string that keeps track of if the user entered an x or an o
#OUTPUT: changes the dictionary to add the x or o from the user
def updated_board(input,current_board,player):
    current_board[input]=player #assigning player to be the value of the direction the user picked
    return current_board

#INPUT: current_board (dictionary) variable represents the current state of the board
#OUTPUT: gives the letter of the winner of the game and if there is no winner then it returns None
def winner(current_board):
    for letter in ['x','o']: #for loop to check if either letter returns a winner
        if current_board['NW']==current_board['N']==current_board['NE']==letter: #checks whether the letter is the same in the 3 spots listed to check for winner
            return letter
        if current_board['W']==current_board['C']==current_board['E']==letter:
            return letter
        if current_board['SW']==current_board['S']==current_board['SE']==letter:
            return letter
        if current_board['NW']==current_board['W']==current_board['SW']==letter:
            return letter
        if current_board['N']==current_board['C']==current_board['S']==letter:
            return letter
        if current_board['NE']==current_board['E']==current_board['SE']==letter:
            return letter
        if current_board['NW']==current_board['C']==current_board['SE']==letter:
            return letter
        if current_board['SW']==current_board['C']==current_board['NE']==letter:
            return letter

def draw(current_board):
    if " " not in current_board.values():
        return True
    return False


gamemode = input("Pick either: Mode (1): One human player or Mode (2): No human players: ")
while int(gamemode) not in [1,2]:
    gamemode = input("Pick either: Mode (1): One human player or Mode (2): No human players: ")

current_player = "x"
current_board = empty_board
while True:
    print(board(current_board))
    if int(gamemode) == 1 and current_player == "x":
        current_move = input("Player {}: enter a direction: ".format(current_player))
        while not valid_move(current_move,current_board): #checks whether it is an unoccupied space and if the user entered a valid direction
            current_move = input("Player {}: enter a direction: ".format(current_player))
        current_board = updated_board(current_move, current_board, current_player)
    else:
        possible_moves = [direction for direction in current_board if current_board[direction] == " "]
        current_board = updated_board(possible_moves[round(random.random()*len(possible_moves)-1)], current_board, current_player)
    if winner(current_board):
        print(board(current_board))
        print("Player {} has won!!".format(winner(current_board)))
        break
    if draw(current_board):
        print(board(current_board))
        print("Draw.")
        break
    if current_player == "x":
        current_player = "o"
    else:
        current_player = "x"
