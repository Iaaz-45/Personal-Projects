import os

from constants import *

SUBJECTS_FILE_PATH = "./subjects/subjects.txt"

def c_subject():
    print(SUBJECTS)
    subject = input("Subject Name: ").lower()
    try:
        os.makedirs(os.path.join("./subjects", subject))
        topic_file = open(f"./subjects/{subject}/topics.txt", "w")
        topic_file.close()
        print("Successfully created a new subject!")
        SUBJECTS.append(subject)
        save_subjects()
    except FileExistsError as e:
        print("That subject name already exists!")

def save_subjects():
    with open(SUBJECTS_FILE_PATH, "w") as file:
        for subject in SUBJECTS:
            file.write(subject + "\n")

def load_subjects():
    try:
        with open(SUBJECTS_FILE_PATH, "r") as file:
            subjects = [line.strip() for line in file]
            SUBJECTS.extend(subjects)
    except FileNotFoundError:
        print("Error: File Not Found!")

def c_topic():
    print(SUBJECTS)
    subject = input("Choose Subject: ").lower()
    if subject not in SUBJECTS:
        print("Subject name does not exist!")
        return 1

    topic_name = input("Topic Name: ").lower()
    topics = load_topics(subject)
    if topic_name in topics:
        print("Topic name already exists!")
        return 1
    
    topics.append(topic_name)
    save_topic(subject, topics)
    c_top_file(subject, topic_name)
    

def load_topics(subject):
    topics = []
    try:
        with open(f"./subjects/{subject}/topics.txt", "r") as file:
            topic = [line.strip() for line in file]
            topics.extend(topic)
            return topics
    except FileNotFoundError:
        print("Error: File Not Found!")
    
def save_topic(subject, topics):
    with open(f"./subjects/{subject}/topics.txt", "w") as file:
        for topic in topics:
            file.write(topic + "\n")

def c_top_file(subject, topic):
    topic_file = open(f"./subjects/{subject}/{topic}.txt", "w")
    topic_file.close()
        
def c_lesson():
    pass
