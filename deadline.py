import datetime

Username = input("Tell me your name: \n")
UserInput = input("Enter A Goal Followed By Date To Reach The Goals All Separated By A Colon: \n")

UserInputList = UserInput.split(":")

UserGoal = UserInputList[0]
UserDeadline = UserInputList[1]

ConvertStrToDate = datetime.datetime.strptime(UserDeadline, "%d/%m/%Y")

TodayDate = datetime.datetime.today()

if ConvertStrToDate < TodayDate:
    print(f"{Username} Kindly enter a Date Greater Than Today's Date")

else:
    GoalDate = (ConvertStrToDate - TodayDate).days
    print(f"Dear {Username}, It Would Take {GoalDate} days to complete the Goal '{UserGoal}'")




#Learn Golang: 2.5.2023
