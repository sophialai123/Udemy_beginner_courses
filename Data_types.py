"""
Data Types:
string = "Hello"
Integer = 12
Float = 1.20
Boolean : True , False


"""
#TODO  Subscript : to access characters from the string
print("Hello"[0]) # output : h
print("hello"[-1]) # output : o
print(123_456_789) # large integer output: 123456789

"""
type check function : type()
covert to different data types
str(), int(), float()
"""
# num_char = len(input("What is your name ? "))
# print(type(num_char)) # <class 'int'>
# print("Your name has " + str(num_char) + " characters")
print(str(70) + str(100))
a = float(123)
print(a)
print(type(a)) #<class 'float'>

#TODO Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8
# Warning.** Do not change the code on lines 1-3. Your program should work for different inputs.
# e.g. any two-digit number. Input: 39 output: 3 + 9 = 12
# two_digit_number = input("Type a two digit number: ")
# print(type(two_digit_number))
# print(int(two_digit_number[0]) + int(two_digit_number[1]))


#TODO Mathematic operation in python
"""
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	 ---- float
%	Modulus	x % y	
**	Exponentiation	x ** y	两次方  
//	Floor division	x // y  ------int 
"""
print((6//3)) # output 2 - int
print(6/3) # output 2.0 -- float
x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2
print(3*3+3/3-3)

#TODO BMI Calculator
weight = 80
height = 1.75
bmi = weight / (height**2)
print(round(bmi))

# height = float(input("enter your height in m: "))
# weight = int(input("enter your weight in kg: "))
# bmi = weight / (height**2)
# print(round(bmi))

#TODO Your life in Weeks
'''
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live 
until 90 years old. It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Hint:

There are 365 days in a year, 52 weeks in a year and 12 months in a year.
Try copying the example output into your code and replace the relevant parts so that the sentence is formated the same way.
'''
# age = int(input("What is your current age?: "))
# days = 365 * (90-age)
# weeks = 52 * (90-age)
# months = 12 * (90-age)
# print(f"You have {days} days, {weeks} weeks, {months} months left until 90 years old. ")

#TODO tip-calculator
"""
#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
#HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python
https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places
format with 2 decimal place
"""

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?: $ "))
tip = float(input("What percentage tip would you like to give? 10, 12 or 15?: ")) / 100
people = int(input("How many people to split the bill?: "))
average_bill = round(((bill / people) * (1+tip)), 2)
average_bills ='{0: .2f}'.format(average_bill) # format with 2 decimal place
print(f"Each person should pay: ${average_bills}")

