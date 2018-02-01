#subproblems to complete to write the program:
#print current state of the board
#main loop for input
#updated board (save and display)
#who won

#params:must pass in a dictionary with directions as the keys(NW,N,NE,W,E,C,SW,S,SE) with c as the center and the values x,o,or ""
#return: string representation of the board
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

#params: input (string) variable represents the direction typed in, current_board (dictionary) variable represents the current state of the board
#return: if the user does not enter a valid direction or pick an empty spot then it will print pick a direction or pick an empty spot and returns False. If the move is valid it returns true
def valid_move(input,current_board):
    if input not in empty_board: #checks if the user picked a valid direction
        print ('pick a direction')
        return False
    if current_board[input]!=" ": #checks if the user picked an empty spot
        print('pick an empty spot')
        return False
    return True

#params: input (string) variable represents the direction typed in, current_board (dictionary) variable represents the current state of the board, player is a string that keeps track of if the user entered an x or an o
#return: changes the dictionary to add the x or o from the user
def updated_board(input,current_board,player):
    if valid_move(input,current_board): #checks whether it is an unoccupied space and if the user entered a valid direction
        current_board[input]=player #assigning player to be the value of the direction the user picked
        return current_board

#params: current_board (dictionary) variable represents the current state of the board
#return: gives the letter of the winner of the game and if there is no winner then it returns None
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
