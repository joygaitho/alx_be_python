# multiplication table generator
def generate_multiplication_table():
    try:
        number = int(input("Enter a number to see its multiplication table:"))
    except ValueError:
        print("Invalide input! Enter a whole number.")
        return 
    print(f"\n --- Multiplication table for {number} (1,10)---")
    # The range(1, 11) generates numbers from 1 up to (but not including) 11, which is 1, 2, ..., 10.
    for i in range(1,11):
        # calculate the product
        product = number * i
        # print the result in the fomart "X * Y = Z"
        print(f"{number} * {i} = {product}")
# run the function
generate_multiplication_table()