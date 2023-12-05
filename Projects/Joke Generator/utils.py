from constants import *

# Function to prompt the user for an action and validate it
def get_user_action():
    action = input(f"Enter action, {LIST_OF_ACTIONS} : \n").lower()
    return action

# Function to save sites to a file
def save_sites_to_file():
    with open("sites.txt", "w") as file:
        for site in LIST_OF_SITES:
            file.write(site + "\n")

# Function to load sites from the file
def load_sites_from_file():
    try:
        with open("sites.txt", "r") as file:
            sites = [line.strip() for line in file]
            LIST_OF_SITES.extend(sites)
    except FileNotFoundError:
        # Handle the case where the file doesn't exist (first program run)
        pass

# Function to save joke to a file
def save_joke_to_file():
    with open("jokes.txt", "w") as file:
        count = 0
        for joke in LIST_OF_JOKES:
            file.write(str(count) + " - " + joke + "\n")
            count += 1
