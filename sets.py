calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"


def validate_and_execute(num):
        
    try:
        user_input_number = int(num)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("You enetered a 0, please enter a valid positive number")
        else:
            print("You enetered a negative, please enter a valid positive number")
    except ValueError:
        print("Your input is not a valid number, Don't ruin my program")

user_input = ""
while user_input != "exit":   
        user_input = input("Hey user , enter a number of days as a comma seperated values and I will convert it to hours!\n")
        list_of_days = user_input.split(",")
        print(set(list_of_days))
        for num_of_days_element in set(list_of_days):
             validate_and_execute(num_of_days_element)