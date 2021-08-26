# TODO Average Height
"""Instructions:
You are going to write a program that calculates the average student height from a List of heights.
e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]

The average height can be calculated by adding all the heights together and dividing by the total number of heights.

e.g. 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146

There are a total of 7 heights in student_heights : 1146 ÷ 7 = 163.71428571428572

Average height rounded to the nearest whole number = 164

Important You should not use the sum() or len() functions in your answer. You should try to replicate their
functionality using what you have learnt about for loops.

Example Input
156 178 165 171 187
In this case, student_heights would be a list that looks like: 156, 178, 165, 171, 187

Example Output
171
e.g. When you hit run, this is what should happen:

https://cdn.fs.teachablecdn.com/Nzb8hUVsQJ6STAGnvDCP

Hint
Remember to use the round() function to round the average height before you print it.
"""

# 180 124 165 173 189 169 146
# student_heights = input("Input a list of student heights: ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])
#
# total = 0
# for x in student_heights:
#   total += x
# print(f"Total height = {total}")
# print(f"numbers of students = {n+1}.")
# average = total / (n+1)
# print(f"The average height is {round(average)}.")


# solution from udemy
# total_height = 0
# for height in student_heights:
#   total_height += height
# print(f"total height = {total_height}")
#
# number_of_students = 0
# for student in student_heights:
#   number_of_students += 1 # runs a number of times = len (student_height)
# print(f"number of students = {number_of_students}")
#
# average_height = round(total_height / number_of_students)
#print(average_height)

#TODO Highest Score
"""Instructions
You are going to write a program that calculates the highest score from a List of scores.
e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
Important you are not allowed to use the max or min functions. The output words must match the example. i.e
The highest score in the class is: x
Example Input
78 65 89 86 55 91 64 89
In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]
Example Output
The highest score in the class is: 91
e.g. When you hit run, this is what should happen:
https://cdn.fs.teachablecdn.com/DnSPgYNSTgeHRJ3MinHg
"""

#78 65 89 86 55 91 64 89
# student_scores = input("Input a list of student scores: ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)
#
# highest_score = 0
# for score in student_scores:
#     if score > highest_score:
#       highest_score = score
# print(f"The highest score is {highest_score}.")



#TODO adding 1 to 100.
# total = 0
# for x in range(1, 101):
#   total += x
# print(total)

#TODO Password Generator Project
"""
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
"""
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#easy level
password = " "
for letter in range(nr_letters):
    # letter = random.choice(letters)
    # password += letter
    password += random.choice(letters)

for symbol in range(nr_symbols):
    password += random.choice(symbols)

for num in range(nr_numbers):
    password += random.choice(numbers)

print(f"Your password is{password}.")

# hard level
password = []
for letter in range(nr_letters):
    password.append(random.choice(letters))

for symbol in range(nr_symbols):
    password.append(random.choice(symbols))

for num in range(nr_numbers):
    password.append(random.choice(numbers))
random.shuffle(password)
new_password = ''.join(password)

print(f"Your new password is{new_password}.")


#Random password generator
# https://towardsdatascience.com/10-python-mini-projects-that-everyone-should-build-with-code-769c6f1af0c4
import random
pass_len = int(input("enter the length of password: "))
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p = " ".join(random.sample(s, pass_len))
print(p)

