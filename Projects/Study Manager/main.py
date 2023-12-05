import os
from create_methods import c_subject, c_topic, c_lesson, load_subjects, load_topics
from view_methods import v_topic
from constants import *

def get_user_action():
    action = input(f"Enter action, {LIST_OF_ACTIONS} : ").lower()
    return action

def execute_action(action):
    if action == "create":
        create()
    elif action == "remove":
        remove()
    elif action == "view":
        view()

def create():
    os.system("cls")
    print("Type 'back' to go back\nMethods: ")

    for method in CREATE_METHODS:
        if method == "cs":
            print("Type 'cs' to create a new subject")
        elif method == "ct":
            print("Type 'ct' to create a new topic")
        elif method == "cl":
            print("Type 'cl' to create a new lesson")

    while True:
        method = input("Type method: ").lower()
        if method in CREATE_METHODS:
            break
        else:
            print("Invalid method!")

    if method == "cs":
        c_subject()
    elif method == "ct":
        c_topic()
    elif method == "cl":
        c_lesson()

def remove():
    pass

def view():
    print("Current Subjects:")
    for subject in SUBJECTS:
        print(subject)
    view_sub = input("Choose Subject: ").lower()
    if view_sub not in SUBJECTS:
        print("Subject name does not exist!")
        view()

    topics = load_topics(view_sub)
    if not topics:
        print("Subject has no topics!")
        view()
    print(topics)
    topic_name = input("Choose Topic: ").lower()
    if topic_name not in topics:
        print("Topic name does not exist!")
        view()
    

def main():
    load_subjects()

    while True:
        action = get_user_action()
        if action == "quit":
            print("Exiting the program!")
            break
        execute_action(action)
        if action not in LIST_OF_ACTIONS:
            print("Failed to execute the action!")

if __name__ == "__main__":
    main()
