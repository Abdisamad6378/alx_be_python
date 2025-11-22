"""Daily reminder system that provides task reminders based on priority and time constraints."""

Task = input("Enter your task:").lower()
Time_bound = input("is it time bound (yes or no): " ).lower()
Priority = input("priority (high, medium, low): ").lower()


match Priority:
    case "high":
        if Time_bound == "yes":
            print(f"\nReminder: '{Task}' is high priority task "
                  f"it requires immediate attention today!")
        else:
            print(f"\nReminder: '{Task}' is high priority task please adddress it soon")
    case "medium":
        if Time_bound == "yes":
            print(f"\nNote: '{Task}' is medium priority task that should be completed today")
        else:
            print(f"\nNote: '{Task}' is medium priority task that should be completed this week ")
    case "low":
        if Time_bound == "low":
            print(f"\nNote '{Task}' is low priority task that should be completed this month")
        else:
            print(f"\nNote '{Task}' is low priority task "
                  f"that should be completed when you have free time")
    case _:
        print("\nInvalid priority level! please use high, medium, low.")
