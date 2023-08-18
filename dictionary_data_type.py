
def days_to_units(num_of_days,name_of_unit):
    if name_of_unit == "hours":
         calculation_to_units = 24
    else:
         calculation_to_units= 24*60
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute(days_and_unit_dictionary):
    num = days_and_unit_dictionary["days"]
    try:
        user_input_number = int(num)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number,days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You enetered a 0, please enter a valid positive number")
        else:
            print("You enetered a negative, please enter a valid positive number")
    except ValueError:
        print("Your input is not a valid number, Don't ruin my program")

user_input = ""
while user_input != "exit":   
        user_input = input("Hey user , enter a number of days and conversion unit Ex: 20:hour\n")
        if user_input == "exit":
             break
        days_and_unit = user_input.split(":")
        days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1].lower()}
        print(days_and_unit_dictionary)
        validate_and_execute(days_and_unit_dictionary)







#Data Types
message = "enter some value"
days = 20
price = 9.99
valid_number = True
exit_input = False
list_of_days = [20,40,20,100]
list_of_months = ["January", "February", "June"]
set_of_days = {20, 45, 100}
days_and_unit = {"days": 10 , "unit": "hours"}