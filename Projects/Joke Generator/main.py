import os
from actions import execute_action
from utils import load_sites_from_file, get_user_action

# The main function serving as the entry point
def main():
    os.system("cls")
    print("Type 'quit' to stop the program")
    
    # Load sites from file at the beginning of the program
    load_sites_from_file()
    while True:
        action = get_user_action()
        if action == "quit":
            print("Exiting the program. Goodbye!")
            break
        execute_result = execute_action(action)
        if not execute_result:
            print("Failed to execute the action. Please try again.\n")

if __name__ == "__main__":
    main()
