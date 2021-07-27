'''

Description: Program that simulates picking a random card from a deck
Programmer:Chris Dimapasok
Input: Console output of random integer from 0-51 representing an individual card from a deck
Output: Console output that displays type of card
Known Bugs:
Version 1.0
Change list in this version: N/A
Date 06/14/2021

'''


import random

#n= eval(input("A random integer "))
n= random.randint(0,51)
suit= (n//13)
rank= (n%13)

if suit == 0:
    new_suit = "Clubs"
elif suit == 1:
    new_suit= "Diamonds"
elif suit == 2:
    new_suit= "Hearts"
elif suit == 3:
    new_suit= "Spades"

if rank == 0:
    new_rank = "Ace"
elif rank == 1:
    new_rank = "2"
elif rank == 2:
    new_rank = "3"
elif rank == 3:
    new_rank = "4"
elif rank == 4:
    new_rank= "5"
elif rank == 5:
    new_rank= "6"
elif rank == 6:
    new_rank = "7"
elif rank == 7:
    new_rank= "8"
elif rank == 8:
    new_rank= "9"
elif rank == 9:
    new_rank = "10"
elif rank == 10:
    new_rank= "Jack"
elif rank == 11:
    new_rank= "Queen"
elif rank == 12:
    new_rank= "King"


print("The card you picked is the", new_rank, "of", new_suit)


'''
The card you picked is the Ace of Hearts
'''


#Clubs, Diamonds, Hearts, Spades = str(0), str(1), str(2), str(3)
#s= Clubs, Diamonds, Hearts, Spades









