# task reminder program
# prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")
# process the task based on priority
match priority:
    case "high":
        message = f"Reminder: {task} is a high priority task "
    case "medium":
        message = f"{task} is a medium priority task "
    case "low":
        message = f"Note: {task} is a low priority task "
    case _:
        message = f"{task} has unknown priority level "
# modify reminder is time-bound
if time_bound == "yes":
    message += "that requires immediate attention today!"
elif time_bound == "no" and priority == "low":
    message += ". Consider completing it when you have free time."
else:
    message += "it is important and should be scheduled for completion soon."
# display the customized reminder
print(f"{message}")