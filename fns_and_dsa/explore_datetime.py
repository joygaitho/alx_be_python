# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Get current date and time
    current_date = datetime.now()
    
    # Format and print
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")

def calculate_future_date(days_to_add):
    # Get today’s date
    current_date = datetime.now()
    
    # Add timedelta
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format and print
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

def main():
    # Part 1
    display_current_datetime()

    # Part 2
    days_input = input("Enter the number of days to add to the current date: ")
    
    try:
        days = int(days_input)
        calculate_future_date(days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
