#Calculator
from art import logo
from clear_library import clear
#Add
def add(n1, n2):
	return n1+n2

#Subtract
def subtract(n1, n2):
	return n1-n2

#Multiply
def multiply(n1, n2):
	return n1*n2


#Divide
def divide(n1, n2):
	return n1/n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    clear()
    print(logo)
    
    keep_calculating = True
    num1 = float(input("What's the first number?: "))

    for symbol in operations:
        print (symbol)

    while keep_calculating:
        operator = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operator](num1, num2)

        print(f"{num1} {operator} {num2} = {answer}")
        
        cnt = input(f"Type 'y' to continue calcualating with {answer}, or type 'n' to exit.: ")
        if cnt.lower() != 'y':
            keep_calculating = False
            calculator()
        else:
            num1 = answer

calculator()