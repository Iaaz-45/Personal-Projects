import requests
import random

WORDS = []
NOUNS = []
perspective = ["I", "You", "She", "He", "We", "They", "Dogs", "Cats", "Bears", "Godzillas", "Monkeys", "Cars", "Johnny"]
connectors = ["With", "Of", "For", "Out", "Off", "Out of", "a"]

def get_random_verb():
    ran = random.randrange(0, 2)
    no_s = False
    if ran == 0:
        no_s = True
    with open("verbs.txt" , "r") as file:
        WORDS = file.readlines()
    for i in range(len(WORDS)):
        WORDS[i] = WORDS[i].replace("\t", "").replace("\n", "")
        if no_s:
            WORDS[i] = WORDS[i][:len(WORDS[i]) - 1]
    return WORDS[random.randrange(0, len(WORDS))]

def get_random_noun():
    with open("nouns.txt" , "r") as file:
        NOUNS = file.readlines()
    for i in range(len(NOUNS)):
        NOUNS[i] = NOUNS[i].replace("\n", "").capitalize()
    return NOUNS[random.randrange(0, len(NOUNS))]

def sentence(u_input):
    verb = get_random_verb()
    noun = get_random_noun()
    per = perspective[random.randrange(0, len(perspective))]
    con = connectors[random.randrange(0, len(connectors))]
    sentence = [f"{per} {verb} {u_input} {con} {noun}",
                f"{per} {verb} {con} {u_input} {con} {noun}",
                f"{per} {verb} {con} {u_input} {noun}",
                f"{per} {verb} {con} {u_input}",
                f"{per} {verb} {u_input} {noun}",
                f"{per} {verb} {u_input} {noun}",]
    return sentence[random.randrange(0, len(sentence))]

if __name__ == "__main__":
    u_input = input("Enter word: ").lower().capitalize()
    for i in range(10):
        print(sentence(u_input))