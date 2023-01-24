import os
# A Simple TicTacToe Game

# Visual Representation
# User Interaction for an Update
# Update the Program
# Update the Visual Representation

## Visual Representation
def numpad(board):
    n = 0
    while n < 2:
        for i in range(3):
            if n == 0 and i == 1:
                print(" " * 2 + board[1] + " " * 2 + "|" + " " * 2 + board[2] + " " * 2 + "|" + " " * 2 + board[3] + " " * 2)
            elif n == 1 and i == 1:
                print(" " * 2 + board[4] + " " * 2 + "|" + " " * 2 + board[5] + " " * 2 + "|" + " " * 2 + board[6] + " " * 2)
            else:
                print(" " * 5 + "|" + " " * 5 + "|" + " " * 5)
        print("_" * 18)
        n += 1
    for i in range(3):
            if i == 1:
                print(" " * 2 + board[7] + " " * 2 + "|" + " " * 2 + board[8] + " " * 2 + "|" + " " * 2 + board[9] + " " * 2)
            else:
                print(" " * 5 + "|" + " " * 5 + "|" + " " * 5)

## User Interaction for an Update
users = ["User 1", "User 2"]
users_dict = {users[0]: 0, users[1]: 0}

# Choose a Mark for each User
def mark():
    user_1_mark = 0
    user_2_mark = 0
    while user_1_mark not in ["X", "x", "O", "o"]:
        user_1_mark = input(f"Choose a mark for {users[0]} (X or O): ")
    
    user_1_mark = user_1_mark.upper()

    if user_1_mark == "X":
        user_2_mark = "O"
    else:
        user_2_mark = "X"
    
    return user_1_mark, user_2_mark

# Moves of Users
def move(move_count):
    user_move = "Make a Move"
    in_range = False
    
    while user_move.isdigit() == False or in_range == False:
        
        if move_count % 2 == 0:
            user_move = input(f"Make a Move {users[0]} (1-9): ")
        elif move_count % 2 == 1:
            user_move = input(f"Make a Move {users[1]} (1-9): ")
        
        if user_move.isdigit() == False:
            print("Enter a number!")
            continue
        
        if int(user_move) not in range(1,10):
            print("Enter a number in the range 1-9!")
            continue
        else:
            in_range = True
    
    return int(user_move)

## Update the Program
def update_board(board, users_dict, user_move, users, move_count):
    empty = True
    if move_count % 2 == 0:
        while empty:
            if board[user_move] == " ":
                board[user_move] = users_dict[users[0]]
                empty = False
            else:
                print("Choose another space!")
                user_move = move()
            
    elif move_count % 2 == 1:
        while empty:
            if board[user_move] == " ":
                board[user_move] = users_dict[users[1]]
                empty = False
            else:
                print("Choose another space!")
                user_move = move()
    
    return board

## Winning Condition
def end(board, users, move_count):
    for i in range(1, len(board) + 1):
        if (board[1] == board[2] == board[3] == "X" or board[4] == board[5] == board[6] == "X" or board[7] == board[8] == board[9] == "X" 
            or board[1] == board[4] == board[7] == "X" or board[2] == board[5] == board[8] == "X" or  board[3] == board[6] == board[9] == "X" 
            or board[1] == board[5] == board[9] == "X" or board[3] == board[5] == board[7] == "X"):
                print(f"{users[0]} has won!")
                return True
        elif (board[1] == board[2] == board[3] == "O" or  board[4] == board[5] == board[6] == "O" or board[7] == board[8] == board[9] == "O" 
            or board[1] == board[4] == board[7] == "O" or board[2] == board[5] == board[8] == "O" or  board[3] == board[6] == board[9] == "O" 
            or board[1] == board[5] == board[9] == "O" or board[3] == board[5] == board[7] == "O"):
                print(f"{users[1]} has won!")
                return True
        elif move_count == 9:
            print("Draw!")
            return True
        else:
            return False

## Re-match 
def round():
    question = "?"
    while question != "Y" and question != "N":
        question = input("Another round? (Y-N)? ").upper()

    if question == "Y":
        return True
    elif question == "N":
        return False

## The Game
def game(users, users_dict):
    
    move_count = 0
    board = ["*", " ", " ", " ", " ", " ", " ", " ", " ", " "]

    print("Welcome to the TicTacToe Game and Good Luck!")
    print("This is a turn-based game. User 1 will go first.")
    
    # Print the Board
    numpad(board)
    
    # Tuple Unpacking
    user_1_mark, user_2_mark = mark()
    users_dict[users[0]] = user_1_mark
    users_dict[users[1]] = user_2_mark
    print(f"Mark of User 1: {users_dict[users[0]]}")
    print(f"Mark of User 2: {users_dict[users[1]]}")
    #print(users_dict)

    game_on = True
    while game_on:
        # User's Moves
        user_move = move(move_count)
        os.system("clear")

        # Update the Board
        board_update = update_board(board, users_dict, user_move, users, move_count)
        move_count += 1

        # Update the Visual Representation
        numpad_update = numpad(board_update)

        # Show the Updated Visual Representation
        numpad_update

        #Check for the End
        if end(board, users, move_count):
            game_on = False

    rematch = round()
    if rematch:
        os.system("clear")
        move_count = 0
        game(users, users_dict)
    else:
        pass

# Run
game(users, users_dict)