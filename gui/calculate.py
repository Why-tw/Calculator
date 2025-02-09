import math

validChar = ['+', '-', '*', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def calculate(string):
    for i in range(len(string)):
        if (string[i]) not in validChar:
            return "Invalid input"
    try:
        return str(eval(string))
    except:
        return "Error"

