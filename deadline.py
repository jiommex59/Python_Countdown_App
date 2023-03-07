import datetime

# This block od code requests user input
Username = input("Tell me your name: \n")
UserInput = input("Enter A Goal Followed By Date To Reach The Goals All Separated By A Colon: \n")

# This code block converts the user input into an array
UserInputList = UserInput.split(":")

UserGoal = UserInputList[0]
UserDeadline = UserInputList[1]

# This code block converts string into a datetime format
ConvertStrToDate = datetime.datetime.strptime(UserDeadline, "%d/%m/%Y")

# This code block displays todaay's date
TodayDate = datetime.datetime.today()

# This code block handles and validates a situation where date given is in the past or a later date than today
if ConvertStrToDate < TodayDate:
    print(f"{Username} Kindly enter a Date Greater Than Today's Date")

else:
    GoalDate = (ConvertStrToDate - TodayDate).days
    print(f"Dear {Username}, It Would Take {GoalDate} days to complete the Goal '{UserGoal}'")





