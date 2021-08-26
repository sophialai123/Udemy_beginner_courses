"""
print does not return
return does not print
"""
'''
def format_name(f_name, l_name):
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  f"Result: {formatted_f_name} {formatted_l_name}"

#Storing output in a variable
formatted_name = format_name(input("Your first name: "), input("Your last name: "))
print(formatted_name)
#or printing output directly
print(format_name(input("What is your first name? "), input("What is your last name? ")))

#Already used functions with outputs.
length = len(formatted_name)

#Return as an early exit
def format_name(f_name, l_name):
  """Take a first and last name and format it 
  to return the title case version of the name."""
  if f_name == "" or l_name == "":
    return "You didn't provide valid inputs."
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"Result: {formatted_f_name} {formatted_l_name}"

'''

"""
Days in Month
Instructions
In the starting code, you'll find the solution from the Leap Year challenge. First, convert this function is_leap() 
so that instead of printing "Leap year." or "Not leap year." it should return True if it is a leap year and return False
if it is not a leap year.

You are then going to create a function called days_in_month() which will take a year and a month as inputs, e.g.

days_in_month(year=2022, month=2)
And it will use this information to work out the number of days in the month, then return that as the output, e.g.:

28
The List month_days contains the number of days in a month from January to December for a non-leap year. A leap year has 29 days in February.

Hint
Look at the function call at the bottom of the code to see the positional arguments. The order is very important.

Feel free to choose your own parameter names.

Remember that month_days is a List and Lists in Python start at position 0. So the number of days in January is month_days[0]

Be careful with indentation.

"""

"""
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "It is an invalid input."
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]



# 🚨 Do NOT change any of the code below


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
"""

logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""



def add(n1,  n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add,
             "-": substract,
             "*": multiply,
             "/": divide
}

def calculator():
    num1 = float(input("What is your first number: "))

    for symbol in operations:
        print(symbol)

    while True:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is your next number: "))

        function = operations[operation_symbol]
        answer = function(num1, num2)
        print(f"{num1} {operation_symbol}{num2} = {answer}")
        choice = input(f"Type 'y' to continue with {answer}, type 's' to star a new calculator, or type 'n' to exit: ").lower()
        if choice == "y":
            num1 = answer
            continue
        elif choice == "s":
            calculator()
        else:
            return # to break the loop, you can use return to stop in function.

calculator()








