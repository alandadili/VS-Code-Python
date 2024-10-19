def main():
    #add loops for each to error check if the user enters something other than a float
    number1 = float(input("Enter a number into the calculator "))  
    

    operation = input("Enter operation ")
   

    number2 = float(input("Enter another number into the calculator ")) #
    
    
    
    if operation == "+":
        print("Total= ",addition(number1, number2))
    
    if operation == "-":
        print("Total= ",subtraction(number1, number2))
    
    if operation == "*":
        print("Total= ",multiplication(number1, number2))
    
    if operation == "/":
        print("Total= ",division(number1, number2))

    if operation == "^":
        print("Total= ",exponent(number1, number2))

def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    return number1 / number2

def exponent(number1, number2):
    return number1 ** number2


main()