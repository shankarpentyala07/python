from helper import validate_and_execute , user_input_message
from datetime import datetime, timezone
import os
import logging


logger = logging.getLogger("MAIN")
logger.error("Error happened in the app")

print(os.name)
""""
user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    if user_input == "exit":
        break
    days_and_unit = user_input.split(":")
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1].lower()}
    print(days_and_unit_dictionary)
    validate_and_execute(days_and_unit_dictionary)
    print(datetime.now())
    """