calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute():
    if user_input.isdigit(): #isdigit() method is a built-in string method that checks whether all characters in a given string are digits. In other words, it determines if the entire string is composed of numeric characters (0-9).
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You enetered a 0, please enter a valid positive number")
    else:
        print("Your input is not a valid number, Don't ruin my program")


user_input = input("Hey user , enter a number of days and I will convert it to hours!\n")
validate_and_execute()