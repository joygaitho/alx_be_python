# simple calculator using match/case
def calculator():
    # prompt user input
    try:
        num1 = int(input("Enter the first number:"))
        num2 = int(input("Enter the second number:"))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return 
    operation = input("Choose the operation (+, -, *, /):")
    match operation:
        case '+':
            result = num1 + num2
            print(f"The result is {result}.")
        case '-':
            result = num1 - num2
            print(f"The result is {result}.")
        case '*':
            result = num1 * num2
            print(f"The result is {result:,}.")
        case '/':
            if num2 == 0:
                print("Cannot divide by zero.")
            else:
                result = num1 / num2
                print(f"The result is {result:,.0f}.")
        case _:
            print("Invalid operation. Please choose one of +, -, * or /.")
calculator()
