# task reminder program
# prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
# process the task based on priority
match priority:
    case "high":
        message = f"{task} is a high priority task "
    case "medium":
        message = f"{task} is a medium priority task "
    case "low":
        message = f"{task} is a low priority task "
    case _:
        message = f"{task} has unknown priority level "
# modify reminder is time-bound
if time_bound == "yes":
    message += "that requires immediate attention today!"
else:
    message += ". Consider completing it when you have free time."
# display the customized reminder
print(f"Reminder: {message}")