#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 13:30:54 2021

@author: aliemirkaragulle
"""
#TIC TAC TOE GAME"

##################################################
print("Welcome to our Tic Tac Toe Game!")
print("May I have the players names please?")

player1_name = input("Please enter the name of the Player 1: ")
player2_name = input("Please enter the name of the Player 2: ")

print(f"{player1_name}, you will be using the label 'X' in this game to play")
print(f"{player2_name}, you will be using the label 'O' in this game to play")
##################################################



##################################################
game_board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
    ]

def display_game(game_board):
    print(game_board[0])
    print(game_board[1])
    print(game_board[2])
##################################################



##################################################
def row_choice_player1():
    
    #VARIABLES
    
    #Initial
    choice = "Wrong" #Make sure the while loop runs
    valid_range = range(0,3) #Our valid values/ range defined (Row indexes are [0,1,2])
    in_range = False 
    
    #While the user input is not a digit or is not between 0 and 2, keep asking for an input from the user.
    
    #We use an "or operator" since we need both conditions to be satisfied,
    #if we try to  use an "and operator", the while loop will not execute when one of the two conditions are met.
    
    while choice.isdigit() == False or in_range == False:
        
        #NEW INPUT FOR PLAYER 1
        choice = input(f"{player1_name}, please choose the row you want to play your move (0-2):")
        
        #DIGIT CHECK  
        #(If user input is not a digit, an error message will be shown to the user)
        if choice.isdigit() == False:
            print(f"{player1_name}, please enter a digit as an input.")
        
        #RANGE CHECK
        #(If input is not in the correct range, an error message will be shown to the user)
        if choice.isdigit() == True:
            if int(choice) in valid_range:
                in_range = True
            else:
                print(f"{player1_name}, please make sure that the number you enter is between 0 and 2, both inclusive.")
                
    return int(choice)
##################################################



##################################################
def row_choice_player2():
    
    #VARIABLES
    
    #Initial
    choice = "Wrong" #Make sure the while loop runs
    valid_range = range(0,3) #Our valid values/ range defined (Row indexes are [0,1,2])
    in_range = False 
    
    #While the user input is not a digit or is not between 0 and 2, keep asking for an input from the user.
    
    #We use an "or operator" since we need both conditions to be satisfied,
    #if we try to  use an "and operator", the while loop will not execute when one of the two conditions are met.
    
    while choice.isdigit() == False or in_range == False:
        
        #NEW INPUT FOR PLAYER 1
        choice = input(f"{player2_name}, please choose the row you want to play your move (0-2):")
        
        #DIGIT CHECK  
        #(If user input is not a digit, an error message will be shown to the user)
        if choice.isdigit() == False:
            print(f"{player2_name}, please enter a digit as an input.")
        
        #RANGE CHECK
        #(If input is not in the correct range, an error message will be shown to the user)
        if choice.isdigit() == True:
            if int(choice) in valid_range:
                in_range = True
            else:
                print(f"{player2_name}, please make sure that the number you enter is between 0 and 2, both inclusive.")
                
    return int(choice)
##################################################



##################################################
def index_choice_player1():
    
    choice = "Wrong"
    valid_range = range(0,3)
    in_range = False
    
     #While the user input is not a digit or is not between 0 and 2, keep asking for an input from the user.
    
    while choice.isdigit() == False or in_range == False:
        
        choice = input(f"{player1_name}, please choose the index you want to play your move (0-2): ")
        
        #Digit CHECK
        if choice.isdigit() == False:
             print(f"{player1_name}, please enter a digit as an input.")
        
        #Range Check
        if choice.isdigit() == True:
            if int(choice) in valid_range:
                in_range = True
            else:
                print(f"{player1_name}, please make sure that the number you enter is between 0 and 2, both inclusive.")
                         
    return int(choice)
##################################################



##################################################
def index_choice_player2():
    
    choice = "Wrong"
    valid_range = range(0,3)
    in_range = False
    
     #While the user input is not a digit or is not between 0 and 2, keep asking for an input from the user.
    
    while choice.isdigit() == False or in_range == False:
        
        choice = input(f"{player2_name}, please choose the index you want to play your move (0-2): ")
        
        #Digit CHECK
        if choice.isdigit() == False:
             print(f"{player2_name}, please enter a digit as an input.")
        
        #Range Check
        if choice.isdigit() == True:
            if int(choice) in valid_range:
                in_range = True
            else:
                print(f"{player2_name}, please make sure that the number you enter is between 0 and 2, both inclusive.")
                         
    return int(choice)
##################################################



##################################################
def player1_move(game_board, player1_row, player1_index):
    
    """
    This function will update the game_board according to the
    player1's row and index choice and return the game_board in an updated form.
    """
    
    #Player 1 will use the label "X" to play the game
    acceptable_move_player1 = "X"
    
    while True:
        player1_move = input(f"{player1_name} make your move which is ('X'): ")
        
        if player1_move not in acceptable_move_player1:
            print("Please input your correct move!")
        else:
            break
    
    #Update the game_board and return the updated version
    game_board[player1_row][player1_index] = player1_move
    return game_board
##################################################



##################################################
def player2_move(game_board, player2_row, player2_index):
    
    """
    This function will update the game_board according to the
    player2's row and index choice and return the game_board in an updated form.
    """
    
    #Player 2 will use the label "X" to play the game
    acceptable_move_player2 = "O"
    
    while True:
        player2_move = input(f"{player2_name} make your move which is ('O'): ")
        
        if player2_move not in acceptable_move_player2:
            print("Please input your correct move!")
        else:
            break
    
    #Update the game board and return the updated version
    game_board[player2_row][player2_index] = player2_move   
    return game_board
##################################################



##################################################

print("\n")


    

for rounds in range(10):

    #Display the game board
    display_game(game_board)




    #Take the player1's row and index choices, then assign them to player1_row and player1_index variables respectively.
    #Then update the game board according to the input provided by the player1.
    #Finally display the updated game board.
    player1_row = row_choice_player1()
    player1_index = index_choice_player1()

    game_board = player1_move(game_board, player1_row, player1_index)

    display_game(game_board)



    #Take the player2's row and index choices, then assign them to player2_row and player2_index variables respectively.
    #Then update the game board according to the input provided by the player2.
    #Finally display the updated game board.
    player2_row = row_choice_player2()
    player2_index = index_choice_player2()

    game_board = player2_move(game_board, player2_row, player2_index)
    
    #Uncommenting the function below would make the game_board display twice at the end of the player2's turn, because,
    #the while loop loops back to the top and exectues the display_game(game_board) again, so the same function would be
    #executed 2 times sequentially, hence creating a duplication. 
    
    #display_game(game_board) 
    
   
print("Thank you for playing!")

##################################################
"""
Problems about this code:
    1) SOLVED
    2) The game does not have a condition to end
"""

