## 📝 Single Task Reminder Generator
def create_task_reminder():
    # --- Prompt for a Single Task ---
    task = input("Enter your task: ")
    
    # Use .lower() to ensure the priority check works regardless of user capitalization
    priority = input("Priority (high/medium/low): ").lower()
    
    # Use .lower() to ensure the time_bound check works
    time_bound = input("Is it time-bound? (yes/no): ").lower()

    # Initialize the base message for the reminder
    base_message = f"Note: '{task}' is a "
    
    # Initialize the action required suffix
    action_suffix = ""

    # --- Process the Task Based on Priority ---
    match priority:
        case 'high':
            base_message += "high priority task"
        case 'medium':
            base_message += "medium priority task"
        case 'low':
            base_message += "low priority task"
        case _:
            # Handle invalid priority input
            print("\nError: Invalid priority entered. Please try again.")
            return

    # --- Modify the Reminder Based on Time Sensitivity ---
    # Check if the task is time-bound (case-insensitive check handled by .lower() above)
    if time_bound == 'yes':
        # Overwrite the base message to include the immediate action phrase
        action_suffix = " that requires immediate attention today!"
    elif time_bound == 'no' and priority == 'low':
        # Add a gentle suggestion for low-priority, non-time-bound tasks
        action_suffix = ". Consider completing it when you have free time."
    else:
        # For medium/high non-time-bound tasks, simply finish the sentence.
        action_suffix = "."

    # --- Provide a Customized Reminder ---
    # Combine the base message and the action suffix
    final_reminder = base_message + action_suffix
    
    print("\nReminder:", final_reminder)

# Run the function
create_task_reminder()