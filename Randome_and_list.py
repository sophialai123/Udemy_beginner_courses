#TODO Heads or Tails
"""
Instructions
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate a random
number, either 0 or 1. Then use that number to print out Heads or Tails.
e.g.
1 means Heads
0 means Tails

Example Output
Heads
or
Tails
"""

import random

Heads = 1
Tails = 0
random_choice = random.randint(0, 1)
#print(random_choice)

# if random_choice == 1:
#     print("Heads")
# else:
#     print("Tails")

#TODO Who's Paying
"""
Instructions
You are going to write a program which will select a random name from a list of names. The person selected will 
have to pay for everybody's food bill.

Important: You are not allowed to use the choice() function.
Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, 
you must enter all the names as name followed by comma then space. e.g. name, name, name

Example Input
Angela, Ben, Jenny, Michael, Chloe
Note: notice that there is a space between the comma and the next name.

Example Output
Michael is going to buy the meal today!
Hint
You might need the help of the len() function.
https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list

Remember that Lists start at index 0!

# quiz:
aset = {1, "python", ("a", "b"), True} # 1 is True ,that is why True is not printed, 0 is False.
print(aset)


"""
# import random
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
#
# # solution 1:
# # print(names)
# # len_names = len(names)
# # who = random.randint(0, len_names-1)
# # print(f"{names[who]} is going to buy the meal today.")
#
# # solution 2 : easy way to achieve this
# print(f"{random.choice(names)} is going to buy the meal today.")


# https://www.askpython.com/python/string/convert-string-to-list-in-python
# string1 = "Python is great "
# string1 = string1.split() # string covert to a list use split ()
# print(string1)

"""
nested list 
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])
output: "kale"

"""

#TODO Treasure Map
"""
Treasure Map
https://cdn.fs.teachablecdn.com/wiFJAkZZSG2RpGsxYgDO
Instructions
You are going to write a program which will mark a spot with an X.

In the starting code, you will find a variable called map.

This map contains a nested list.
When map is printed this is what the nested list looks like:

['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']
In the starting code, we have used new lines (\n) to format the three rows into a square, like this:

['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']


"""

row1 = ["⬜️","⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ") # position是个二元组吧, 0 and 1
rows = int(position[0]) #
columns = int(position[1]) # 所以行列按照这个二位数的十位和个位来分别定义了,position输入的是一个二位数
map[columns - 1][rows - 1] = "x"
print(f"{row1}\n{row2}\n{row3}")


#TODO rock paper scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choice = [rock, paper, scissors]
import random
user_choice = int(input("What do you choose? Type 0 for rock, 1for paper or 2 for scissors:  "))
print("Your choose: ")
print(choice[user_choice])
computer_choice = random.randint(0, 2)
print("Computer choose: ")
print(choice[computer_choice])
if user_choice >= 3 or user_choice <0:
    print("You typed an invalid number, you lose!")
elif user_choice == computer_choice:
    print("It is a draw.")
elif user_choice == 2 and computer_choice == 0:
    print("Computer wins , you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("Computer loses , you win!")
elif user_choice < computer_choice:
    print("Computer wins , you lose!")
else:
    print("Computer loses , you win!")
