import os
import requests
import threading
import time
from gtts import gTTS
from random import randint
from getpass import getpass

print("Spell the word correctly within the time limit!\n")

# Import pygame and disable default text
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from pygame import mixer

LIST_OF_WORDS = []
CORRECT_WORDS = {}

# Function to load the words from 'words.txt'
def load_words_from_file():
    try:
        with open("words.txt", "r") as file:
            word = [line.strip() for line in file]
            LIST_OF_WORDS.extend(word)
    except FileNotFoundError:
        print("File not found!")

# Function to get the meaning of word
def get_meaning(word):
    try:
        response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)
        word_data = response.json()
        if response.status_code == 200:
            return word_data
        else:
            return "Failed to fetch a definition."
    except Exception as e:
        raise Exception(f"Error fetching definition: {e}")
    
# Function to format and print definitions
def print_meaning(word):
    meaning = get_meaning(word)
    try:
        print(f"1 - Definition: {meaning[0]["meanings"][0]["definitions"][0]["definition"]}\n")
    except Exception as e:
        return f"No Definition Found!"
    try:
        print(f"2 - Definition: {meaning[0]["meanings"][1]["definitions"][0]["definition"]}\n")
    except Exception as e:
        return f""
    try:
        print(f"3 - Definition: {meaning[0]["meanings"][2]["definitions"][0]["definition"]}\n")
    except Exception as e:
        return f""
    return True

def main(x):

    # get random word from words.txt
    word = get_random_word(x)

    # create audio for that word using gTTS and play audio using mixer from pygame 
    get_word_audio(word)
    play_audio()

    # get input from user to chech spelling
    ans = get_input()
    word, ans = validate_answer(ans, word) # returns the word, answer and correct(bool) -> True if ans matches word
    
    # add correct words to a dictionary
    CORRECT_WORDS[word] = ans
    mixer.quit()

# function to get input using getpass so that text is not shown
def get_input():
    ans = getpass("Spell\n")
    return ans

# fuction to validate the answer
def validate_answer(ans, word):
    if ans.lower() == word.lower():
        print(ans + "\n")
        print("Correct!\n")
        print("Spelling -> " + word + "\n")
        print_meaning(word.lower())
        return word, ans
    else:
        print(ans + "\n")
        print("\nIncorrect!")
        print("Spelling -> " + word + "\n")
        print_meaning(word.lower())
        return word, ans


# pygame -> mixer to play the audio
def play_audio():
    mixer.init()
    mixer.music.load("word.mp3")
    mixer.music.play()

# generate word audio
def get_word_audio(word):
    # save word audio to 'word.mp3' using gTTS
    audio = gTTS(text=word, lang="en", slow=False)
    audio.save("word.mp3")

# get word from words.txt using random index
def get_random_word(x):
    # generate random index to get random word
    load_words_from_file()
    rand_idx = randint(0, len(LIST_OF_WORDS)-1)
    word = (LIST_OF_WORDS[x])
    return word

# run a timer on a thread
sec = 10000
def timer(sec):
    while sec > 0:
        time.sleep(1)
        sec -= 1
    return True
timer = threading.Thread(target=timer, args=(sec,), daemon=True)
timer.start()

# while timer is not finished
x = 0
while timer.is_alive():
    x += 1
    main(x)

# if timer is finished print correct and incorrect words
if not timer.is_alive():
    print("\nQuiz completed! Here are the results:")
    for item, value in CORRECT_WORDS.items():
        if value == item.lower():
            print(f"{item.lower()} : {value} -> Correct")
        elif value != item.lower():
            print(f"{item.lower()} : {value} -> Incorrect")
