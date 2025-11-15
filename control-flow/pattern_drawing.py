# square parttern generator
def pattern():
    # prompt user to enter only a positive number
    try:
        size = int(input("Enter the size of the pattern:"))
        if size <= 0:
            print("Please enter a positive interger.")
            return
    except ValueError:
        print("Invalid input. Please enter a whole number.")
        return
    # initialize the row counter
    row = 0
    while row < size: # this loop ensures the processes of printing a new row and moving to the next line is repeated exactly "size" number of times. eg 
        for col in range(size):
            print("*", end="")
        print()
        row += 1
pattern()