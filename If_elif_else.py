#TODO
"""
Leap Year: Instructions

Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366,
with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:

[https://www.youtube.com/watch?v=xX96xng7sAE](https://www.youtube.com/watch?v=xX96xng7sAE)

This is how you work out whether if a particular year is a leap year.

> `on every year that is evenly divisible by 4
>   **except** every year that is evenly divisible by 100
>     **unless** the year is also evenly divisible by 400`

e.g. The year 2000:

2000 ÷ 4 = 500 (Leap)

2000 ÷ 100 = 20 (Not Leap)

2000 ÷ 400 = 5 (Leap!)

So the year 2000 is a leap year.

But the year 2100 is not a leap year because:

2100 ÷  4 = 525 (Leap)

2100 ÷ 100 = 21 (Not Leap)

2100 ÷ 400 = 5.25 (Not Leap)

**Warning** your output should match the Example Output format exactly, even the positions of the commas and full stops.

# Example Input 1 : 2400    # Example Output 1 :Leap year.
# Example Input 2: 1989     # Example Output 2: Not leap year.
``
e.g. When you hit **run**, this is what should happen:
 ![](https://cdn.fs.teachablecdn.com/AthNqKoSm6JD4sMom2X2)

# Hint
1. Try to visualise the rules by creating a flow chart on www.draw.io
2. If you really get stuck, you can see the flow chart I created:
"""

# year = int(input("Which year do you want to check? "))
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year.")
#         else:
#             print("Not a leap year.")
#     else:
#         print("Leap year.")
# else:
#     print("Not a leap year.")



#TODO Pizza Order
"""
Pizza Order : Instructions
Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.

Based on a user's order, work out their final bill.
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
Example Input
size = "L"
add_pepperoni = "Y"
extra_cheese = "N"
Example Output
Your final bill is: $28.
e.g. When you hit run, this is what should happen:

https://cdn.fs.teachablecdn.com/p1evEkwQxGNR4WlolIb4

Hint
Think about what you've learnt about multiple if statements and see if you can reduce 
the number of lines of code while having the same functionality.

"""

# print("Welcome to Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M, or L: ").lower()
# add_pepperoni = input("Do you want pepperoni? Y or N: ").lower()
# extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
# bill = 0
# if size == "s":
#     bill += 15
# elif size == "m":
#     bill += 20
# else:
#     bill += 25
#
# if add_pepperoni == "y":
#     if size == "s":
#         bill += 2
#     else:
#         bill += 3
#
# if extra_cheese == "y":
#     bill += 1
#
# print(f"Your final bill is ${bill}.")

# TODO Love Calculator
"""
Instructions
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for 
the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:
"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:
"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:
"Your score is **z**."
e.g.
name1 = "Angela Yu"
name2 = "Jack Bauer"
T occurs 0 times
R occurs 1 time
U occurs 2 times
E occurs 2 times
Total = 5
L occurs 1 time
O occurs 0 times
V occurs 0 times
E occurs 2 times
Total = 3
Love Score = 53
Print: "Your score is 53."
Example Input 1
name1 = "Kanye West"
name2 = "Kim Kardashian"
Example Output 1
Your score is 42, you are alright together.
Example Input 2
name1 = "Brad Pitt"
name2 = "Jennifer Aniston"
Example Output 2
Your score is 73.
"""
#
# print("Welcome to the Love Calculator!")
# name1 = input("What is your name?: ").lower()
# name2 = input("What is their name?: ").lower()
# true_love = name1 + name2
# t = true_love.count("t")
# r = true_love.count("r")
# u = true_love.count("u")
# e = true_love.count("e")
# l = true_love.count("l")
# o = true_love.count("o")
# v = true_love.count("v")
# e = true_love.count("e")
#
# true = t + u + r + e
# love = l + o + v + e
#
# love_score = int(str(true) + str(love))
# if love_score <= 10 or love_score >= 90:
#     print(f"Your score is {love_score}, you go together like coke and mentos.")
# elif love_score >= 40 and love_score <= 50:
#     print(f"Your score is {love_score}, you are alright together.")
# else:
#     print(f"Your love score is {love_score}.")

#TODO Treasure Island
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = input("You're at a cross road. Where do you want to go? Type 'left' or 'right': ").lower()
if direction == "left":
    choice = input("Do you want to swim or wait. Type 'swim' or 'wait': ").lower()
    if choice == "wait":
        choice1 = input("Which door do you want to enter? Type 'red', 'blue' or 'yellow' ").lower()
        if choice1 == "red":
            print("Burned by fire. Game over.")
        elif choice1 == "blue":
            print("Entered by beasts. Game over.")
        elif choice1 == "yellow":
            print("You found the treasure! You win! ")
        else:
            print("You chose a door that doesn't exist.Game over.")
    else:
        print("Attacked by trout. Game over.")
else:
    print("Fall into a hole. Game over.")