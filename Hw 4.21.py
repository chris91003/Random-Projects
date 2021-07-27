'''

Description: Displays day of the week when given year, month and day
Programmer:Chris Dimapasok
Input: Console input that prompts user to enter a year, month, and day of the month
Output: Console output that displays name of the day of the week
Known Bugs:
Version 1.0
Change list in this version: N/A
Date 06/14/2021
'''


year = eval(input("Enter year: (e.g., 2008): "))

m = eval(input("Enter month 1-12: "))
if m == 1:
    month = "January"
    m = 13
    year = year - 1
elif m == 2:
    month = "February "
    m = 14
    year = year - 1
elif m == 3:
    month = "March"

elif m == 4:
    month = "April"
elif m == 5:
    month = "May"
elif m == 6:
    month = "June"
elif m == 7:
    month = "July"
elif m == 8:
    month = "August"
elif m == 9:
    month = "September"
elif m == 10:
    month = "October"
elif m == 11:
    month = "November"
elif m == 12:
    month = "December"
else:
    print("invalid input")
    quit()
q = eval(input("Enter the day of the month: "))
j = year // 100

k = year % 100

h = (q + ((26 * (m + 1)) // 10) + k + (k // 4) + (j // 4) + (5 * j)) % 7
if h == 0:
    print("Day of the week is: Saturday")
elif h == 1:
    print("Day of the week is: Sunday")
elif h == 2:
    print("Day of the week is: Monday")
elif h == 3:
    print("Day of the week is: Tuesday")
elif h == 4:
    print("Day of the week is: Wednesday")
elif h == 5:
    print("Day of the week is: Thursday")
elif h == 6:
    print("Day of the week is: Friday")

'''
Enter year: (e.g., 2008): 2013
Enter month 1-12: 1
Enter the day of the month: 25
Day of the week is: Friday
'''

'''
Enter year: (e.g., 2008): 2012
Enter month 1-12: 5
Enter the day of the month: 12
Day of the week is: Saturday

'''