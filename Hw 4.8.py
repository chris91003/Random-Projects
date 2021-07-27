'''


Description: Program that Sorts integers into increasing order
Programmer:Chris Dimapasok
Input: Console input of 3 random integers
Output: Console output that displays integers in order
Known Bugs:
Version 1.0
Change list in this version: N/A
Date 06/14/2021

'''

a, b, c= eval(input("Enter three integers: "))
if (a < b < c):
    print(a,b,c)
elif (a < c < b):
    print(a, c, b)
elif (b < a < c):
    print (b, a, c)
elif (b < c < a):
    print ( b, c, a)
elif (c < a < b):
    print( c, a ,b)
elif (c < b < a):
    print (c, b, a)

'''
Enter three integers: 9, 5, 15
5 9 15

'''


