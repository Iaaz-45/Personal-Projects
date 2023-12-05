import subprocess
import requests
import webbrowser
from constants import *
from utils import save_sites_to_file, save_joke_to_file

# Function to execute the action based on user input
def execute_action(action):
    if action == "parrot.live":
        subprocess.run(["curl", "parrot.live"])
    elif action == "visit_site":
        visit_site()
    elif action == "open_url":
        open_url()
    elif action == "add_site":
        add_site()
    elif action == "joke":
        joke()
    elif action == "dad_joke":
        dad_joke()
    elif action == "dark_joke":
        dark_joke()
    elif action == "quote":
        quote()
    else:
        print("Invalid action!\n")
        return False
    return True

# Function to prompt user for a valid website from the predefined list
def get_valid_website():
    while True:
        website = input("What website would you like to go to? ").lower()
        if website in LIST_OF_SITES:
            return website
        print("Invalid site! Please choose a valid site.\n")

# Function to prompt user for a search query if desired
def get_search_query():
    user_response = input("Do you want to search? 'y' or 'n': ").lower()
    return input("What do you want to search? ").lower() if user_response == "y" else "n"

# Function to open the specified website with or without search
def open_website(website, search):
    url = f"https://www.{website}.com"
    if search != "n":
        url += f"/search?q={search}"
    webbrowser.open(url)

# Function to allow the user to add a new site temporarily to the list
def add_site():
    site = input("Add site: ").lower()
    LIST_OF_SITES.append(site)
    print(f"Added {site} to the list!\n")
    save_sites_to_file()  # Call the new function to save sites to file
    return True

# Function to open a specific URL directly
def open_url():
    url = input("Enter the URL you want to open: ")
    webbrowser.open(url)
    return True

# Function to handle visiting a prompted site and searching on those sites
def visit_site():
    print(f"List of sites: {LIST_OF_SITES} \n")
    website = get_valid_website()
    search = get_search_query()
    open_website(website, search)
    return True

# Function to fetch a random quote from the Quotable API
def get_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            quote_data = response.json()
            return f'"{quote_data["content"]}" - {quote_data["author"]}'
        else:
            return "Failed to fetch a quote."
    except Exception as e:
        return f"Error: {e}"

# Function to display the Quote of the Day
def quote():
    quote = get_quote()
    print(f"Quote of the Day: {quote}\n")
    return True

# Function to fetch a dark humor joke from the JokeAPI
def get_dark_joke():
    try:
        response = requests.get("https://sv443.net/jokeapi/v2/joke/Dark")
        joke_data = response.json()
        if response.status_code == 200 and joke_data["type"] == "twopart":
            return f"{joke_data['setup']} {joke_data['delivery']}"
        else:
            return "Failed to fetch a dark humor joke."
    except Exception as e:
        return f"Error: {e}"

# Function to display the Dark Humor Joke of the Day
def dark_joke():
    joke = get_dark_joke()
    print(f"Dark Humor Joke of the Day: {joke}\n")
    save = input("Save joke? 'y' or 'n': ")
    if save == "y":
        save_joke(joke)
    else:
        return True

# Function to fetch a random dad joke from the icanhazdadjoke API
def get_dad_joke():
    try:
        response = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
        if response.status_code == 200:
            joke_data = response.json()
            return joke_data["joke"]
        else:
            return "Failed to fetch a dad joke."
    except Exception as e:
        return f"Error: {e}"

# Function to display a Dad Joke
def dad_joke():
    joke = get_dad_joke()
    print(f"Dad Joke of the Day: {joke}\n")
    save = input("Save joke? 'y' or 'n': ")
    if save == "y":
        save_joke(joke)
    else:
        return True

# Function to fetch a random joke from the JokeAPI
def get_joke():
    try:
        response = requests.get("https://v2.jokeapi.dev/joke/Any")
        joke_data = response.json()
        if response.status_code == 200 and joke_data["type"] == "single":
            return joke_data["joke"]
        elif response.status_code == 200 and joke_data["type"] == "twopart":
            return f"{joke_data['setup']} {joke_data['delivery']}"
        else:
            return "Failed to fetch a joke."
    except Exception as e:
        return f"Error: {e}"

# Function to display the Joke of the Day
def joke():
    joke = get_joke()
    print(f"Joke of the Day: {joke}\n")
    save = input("Save joke? 'y' or 'n': ")
    if save == "y":
        save_joke(joke)
    else:
        return True

# Function to save joke to a file
def save_joke(joke):
    LIST_OF_JOKES.append(joke)
    print(f"Saved joke to the list!\n")
    save_joke_to_file()  # Call the new function to save joke to file
    return True