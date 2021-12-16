import random
import os

FILENAME = "A:\\Python Projects\\Assignments\Assignment10\\hangman\\words.txt"

def read_words():
    try:
        # if os.path.isfile(FILENAME)
        words = []
        with open(FILENAME) as f:
            words = f.readlines()
        return words
    except FileNotFoundError:
        print("Could not find " + FILENAME + " file.")
        return ""
    except Exception as e:
        print(type(e),e)
        return ""

def get_random_word():
    word = random.choice(read_words())
    # We need to strip off the new line character
    word = word.rstrip("\n")
    return word

def main():
    """
    A simple test thay will displat a single
    random word from the list of words
    """
    word = get_random_word()
    print(word)

if __name__ == "__main__":
    main()