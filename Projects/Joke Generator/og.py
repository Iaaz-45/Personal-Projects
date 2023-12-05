import webbrowser
import subprocess

# list of actions you can do in this program and the list of sites
LIST_OF_ACTIONS = ["visit_site", "add_site", "parrot.live"]
LIST_OF_SITES = ["youtube", "google", "reddit", "discord", "spotify"]

# handles visiting prompted site and seatching on those sites
def visit_site(LIST_OF_SITES):
    print(f"List of sites: {LIST_OF_SITES} \n")

    # check if website is in the list_of_sites
    website = input("What website would you like to go to? ").lower()
    if website not in LIST_OF_SITES:
        print("Invalid site!\n")
        return visit_site()

    # if 'y' then search equals what you prompted
    # else search equals 'n'
    if input("Do you want to search? 'y' or 'n': ").lower() == "y":
        search = input("What do you want to search? ").lower()
    else:
        search = "n"

    if search != "n":
        webbrowser.open(f"https://www.{website}.com/search?q={search}")
        main()
    elif search == "n":
        webbrowser.open(f"https://www.{website}.com")
        main()


def add_site():
    # only adds site temporarily
    site = input("Add site: ").lower()
    LIST_OF_SITES.append(site)
    print(f"Added {site} to list!\n")
    main()


def execute_action(action):
    # match functions to actions
    if action in LIST_OF_ACTIONS:
        match action:
            case "visit_site":
                visit_site()
            case "add_site":
                add_site()
            case "parrot.live":
                subprocess.run(["curl", "parrot.live"])
                main()
    else:
        print("Invalid action!\n")
        return 2


def main():
    print("Type 'quit' to stop program")
    action = input(f"Enter action, {LIST_OF_ACTIONS} : \n").lower()
    if action == "quit":
        return 1
    elif action not in LIST_OF_ACTIONS:
        print("Invalid action!\n")
        return main()  # Recursively call main to prompt for a valid action
    else:
        execute_action(action)

main()
