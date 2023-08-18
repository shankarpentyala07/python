from datetime import datetime


user_input = input("Enter you goal with deadline seperated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]
#file_name.class_name.definiton_name
deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
#calculate how many days now from till deadline
today_date = datetime.today()
time_till = deadline_date-today_date
print(f"Dear user! Time remaining for your goal {goal}: {time_till.days}")

"""
sample input
learn python:12.12.2024
"""