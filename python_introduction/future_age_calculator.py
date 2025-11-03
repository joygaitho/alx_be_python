# 1. Prompt the user for their current age and store the input.
# The input() function returns a string, so we must convert it to an integer (int()).
current_age = int(input("How old are you? "))
# 2. Define the year difference (2050 - 2023 = 27)
years_to_add = 27
# 3. Calculate the future age
future_age = current_age + years_to_add
# 4. Print the result in the specified format
print(f"In 2050, you will be {future_age} years old.")