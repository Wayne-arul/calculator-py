#Calculator
from calc_art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": sub,
    "*": multiply,
    "/": divide
}



def calculator():
    num1 = float(input("Enter the first number: "))
    for op in operations:
        print(op)

    should_continue = True
    while should_continue:
        operator = input("Enter the operator: ")
        num2 = float(input("Enter the second number: "))
        function = operations[operator]
        result = function(num1, num2)
        print(f"{num1} {operator} {num2} = {result}")

        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start new.:") == 'y':
            num1 = result
        else:
            should_continue = False
            calculator()  #here we are calling calculator() function inside calculator() function, this is called as recursive function

calculator()







