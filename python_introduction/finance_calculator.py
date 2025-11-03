# 1. Define the annual interest rate
ANNUAL_INTEREST_RATE = 0.05
MONTHS_IN_YEAR = 12
# 2. Get user input for income and expenses
# Use float() to allow for decimal values in currency
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
# 3. Calculate Monthly Savings
monthly_savings = monthly_income - monthly_expenses
# 4. Calculate Projected Annual Savings
# Savings without interest: monthly_savings * 12
annual_savings_base = monthly_savings * MONTHS_IN_YEAR
# Calculate total projected savings with the simple interest formula:
# Projected Savings = Base Savings + (Base Savings * Interest Rate)
projected_savings = annual_savings_base + (annual_savings_base * ANNUAL_INTEREST_RATE)
# 5. Output Results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:,.0f}.")