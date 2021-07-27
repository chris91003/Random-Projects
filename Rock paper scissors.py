#Rock paper scissors game

import random

print("Welcome to Rock-Paper-Scissors")

#Prompt user to start the game
start= input("Ready to start the game? Yes or No? ")

#Define a list that will be randomly chosen by computer 
list= ["Rock", "Paper", "Scissors"]


#Prompts user and computer to enter a move and goes through series of if else statments
def Game():
    if start == "Yes":
        first_move= input("Enter move: ")
        comp= random.choice(list)
    if first_move== "Rock" and comp== "Scissors":
        print("Computer chose: ", comp)
        print("You win!")
    elif first_move== "Rock" and comp== "Paper":
        print("Computer chose: ", comp)
        print("You lose!")
    elif first_move== "Rock" and comp== "Rock":
        print("Computer chose: ", comp)
        print("Tied try again!")
        Game()

    if first_move== "Scissors" and comp== "Paper":
        print("Computer chose: ", comp)
        print("You win!")
    elif first_move== "Scissors" and comp== "Rock":
        print("Computer chose: ", comp)
        print("You lose!")
    elif first_move== "Scissors" and comp== "Scissors":
        print("Computer chose: ", comp)
        print("Tied try again!")
        Game()

    if first_move== "Paper" and comp== "Rock":
        print("Computer chose: ", comp)
        print("You win!")
    elif first_move== "Paper" and comp== "Scissors":
        print("Computer chose: ", comp)
        print("You lose!")
    elif first_move== "Paper" and comp== "Paper":
        print("Computer chose: ", comp)
        print("Tied try again!")
        Game()
    

    else:
        quit()
    

Game()

        

    






    
