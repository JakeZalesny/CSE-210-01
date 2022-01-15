"""
Jake Zalesny
Bro. Kay
Tic-Tac-Toe Game
CSE-210

"""
# I defined this as global so it could be used in every scope and easily modify it. 
CHAR = None

# This sets the board up into a string
def set_the_board() :
    board = []
    for line in range(1,10):
        board.append(line)
    return board

# This displays the board
def display_board(board) :
    counter = 0
    for value in board:
        counter += 1
        print(f"{value} |", end=" ")
        if counter == 3 or counter == 6 :
            print("\n--+---+---+")

# This gets the x player's input
def get_x_turn() :
    try :
        x = int(input("\nIt's x's turn to choose a square (1-9) "))
    except :
        print("Error: not a valid number")
    return x 

# This gets the o player's input
def get_o_turn() :
    try :
        o = int(input("\nIt's o's turn to choose a square (1-9) "))
    except :
        print("Error: not a valid number")
    return o 

# This inserts the player's letter into the board
def insert_into_board(insert,board,player) :
    entry = insert - 1
    if isinstance(board[entry],int) == True :
        board.pop(entry)
        board.insert(entry,player)
        return board
    else :
        print("Ooops, there goes that turn: ")
    return board

# This checks to see if any player has one yet
def game_over(board,winner) :
    if board[0] == winner and board[1] == winner and board[2] == winner :
        return True
    
    elif board[3] == winner and board[4] == winner and board[5] == winner :
        return True
    
    elif board[6] == winner and board[7] == winner and board[8] == winner :
        return True
    
    elif board[0] == winner and board[3] == winner and board[6] == winner :
        return True
    
    elif board[1] == winner and board[4] == winner and board[7] == winner :
        return True
    
    elif board[2] == winner and board[5] == winner and board[8] == winner :
        return True

    elif board[0] == winner and board[4] == winner and board[8] == winner :
        return True    
    
    elif board[2] == winner and board[4] == winner and board[6] == winner :
        return True
    
    else :
        return False

# This checks to see if the game is a cat
def is_a_draw(board) :
    for square in range(9) :
        if board[square] != "x" and board[square] != "o" :
            return False
    
    return True

# This runs all the functions and has a functionality to itself        
def main() :
    board = set_the_board()
    display_board(board)
    done = False
    winner = None
    is_a_draw(board)

# This While loop checks to to see if the game has finished yet  
    while done == False and is_a_draw(board) == False :

# This is the start of the X player's turn
        x = get_x_turn()
        CHAR = "x"
        insert_into_board(x,board,CHAR)

# If the game is over it breaks out of the loop and sets the winner
        if game_over(board,CHAR) == True :
            done = True
            winner = CHAR
            display_board(board)
            break

# This checks to see if it's a cat game, if it is it breaks out of the loop
        if is_a_draw(board) == True :
            break
        
        display_board(board)

# This is the start of the O player's turn 
        CHAR = "o"
        o = get_o_turn()
        insert_into_board(o,board,CHAR)

# If the game is over it breaks out of the loop and sets the winner 
        if game_over(board,CHAR) == True :
            done = True
            winner = CHAR
            display_board(board)
            break

# This checks to see if it's a cat game, if it is it breaks out of the loop
        if is_a_draw(board) == True :
            break

        display_board(board)

# If the game is a cat game it prints out this solution
    if is_a_draw(board) == True :
        print("\nCat!")

# If it's not a cat game that means someone one therefore: 
    else :
        print(f"\nWell played {winner}!")

# This calls the function main and runs the program. 
main()