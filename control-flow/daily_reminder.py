"""Daily reminder system that provides task reminders based on priority and time constraints."""

task = input("Enter your task:")
priority = input("priority (high, medium, low): ").lower()
time_bound = input("is it time bound (yes or no): " ).lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is high priority task "
                  f"it requires immediate attention today!")
        else:
            print(f"\nReminder: '{task}' is high priority task please adddress it soon")
    case "medium":
        if time_bound == "yes":
            print(f"\nNote: '{task}' is medium priority task that should be completed today")
        else:
            print(f"\nNote: '{task}' is medium priority task that should be completed this week ")
    case "low":
        if time_bound == "low":
            print(f"\nNote '{task}' is low priority task that should be completed this month")
        else:
            print(f"\nNote '{task}' is low priority task "
                  f"that should be completed when you have free time")
    case _:
        print("\nInvalid priority level! please use high, medium, low.")
