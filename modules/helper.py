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


user_input_message = "Hey user , enter a number of days and conversion unit Ex: 20:hour\n"