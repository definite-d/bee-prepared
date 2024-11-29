'''
Bee Prepared.
A Spelling Bee Practice Tool.

Copyright (c) 2024, Divine Afam-Ifediogor (definite_d)
This project is licensed under the MIT License. See the LICENSE file for more details.
'''
from pathlib import Path
from pyttsx3 import init
from random import choice, randint

VERSION = "1.13"

ENGINE = init()
TALKING_SPEED_FACTOR = 0.7
ENGINE.setProperty("volume", ENGINE.getProperty("volume") * TALKING_SPEED_FACTOR)


def speak(text: str, speed_factor: float = 0.7):
    """
    Speaks the given text aloud using the pyttsx3 text-to-speech engine.

    Args:
        text (str): The text to be spoken.
        speed_factor (float, optional): The speed factor for the speech. Defaults to 0.7.

    Returns:
        None
    """
    ENGINE.say(text)
    ENGINE.runAndWait()


def read_dictionary(path: str):
    """
    Reads a dictionary file from the specified path and returns a list of words.

    Args:
        path (str): The path to the dictionary file.

    Returns:
        list[str]: A list of words read from the dictionary file. If the file is not found, an empty list is returned.
    """
    try:
        with open(Path(path)) as dictionary:
            words = dictionary.readlines()
        return [word.strip() for word in words]
    except FileNotFoundError:
        print(f"Error: File not found at {path}. Please provide a valid path.")
        return []


def get_random_word(words: list[str]):
    """
    Retrieves a random word from the given list of words.

    Args:
        words (list[str]): A list of words, where each word is optionally followed by a definition.

    Returns:
        tuple[str | None, str | None]: A tuple containing the random word and its definition.
            If the input list is empty, returns (None, None).
    """
    if not words:
        return None, None
    word_entry = words.pop(randint(0, len(words) - 1)).split(": ", maxsplit=1)
    return word_entry[0], (
        word_entry[1] if len(word_entry) > 1 else "No definition available."
    )


def main():
    """
    The main function of the Spelling Bee Practice Tool. It handles the entire
    workflow of the application, including reading the dictionary file,
    prompting the user for input, and tracking the user's score and challenging
    words. It also handles exceptions and provides a final message to the user
    when the application exits.

    Parameters:
        None

    Returns:
        None
    """
    art = """

██████╗ ███████╗███████╗                                        
██╔══██╗██╔════╝██╔════╝                                        
██████╔╝█████╗  █████╗                                          
██╔══██╗██╔══╝  ██╔══╝                                          
██████╔╝███████╗███████╗                                        
╚═════╝ ╚══════╝╚══════╝                                        
                                                                
██████╗ ██████╗ ███████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██╔══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██████╔╝██████╔╝█████╗  ██████╔╝███████║██████╔╝█████╗  ██║  ██║
██╔═══╝ ██╔══██╗██╔══╝  ██╔═══╝ ██╔══██║██╔══██╗██╔══╝  ██║  ██║
██║     ██║  ██║███████╗██║     ██║  ██║██║  ██║███████╗██████╔╝
╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═════╝ 

    """
    print(art)
    print(f"Bee Prepared v{VERSION}")
    print(
        "A Spelling Bee Practice Tool, by definite_d\n(https://github.com/definite-d/bee-prepared)\n\nCtrl+C at any point to exit."
    )
    print("Logo from Google's Noto Color Emoji 16.0")
    speak("     Welcome to Bee Prepared: a Spelling Bee Practice Tool, by definite d.")

    dictionary_path = (
        input('\nEnter a path to a dictionary.txt file (default "dictionary.txt"): ')
        or "dictionary.txt"
    )

    words = read_dictionary(dictionary_path)
    if not words:
        return

    print(f"{len(words)} words were found in the given dictionary.")
    speak(f"{len(words)} words were found in the given dictionary.")

    challenging_words: set = set()
    score = 0
    counter = 0

    print("\nLet's begin.\n")
    speak("Let's begin.")

    try:
        while words:
            incorrect_counter = 0
            word, definition = get_random_word(words)
            if not word:
                break
            counter += 1

            while True:
                print(f"Playing word {'*'*len(word)}...")
                speak(word)

                answer = (
                    input(
                        "Type the word (\\a: say again, \\d: define, \\n: next, \\r: reveal): "
                    )
                    .lower()
                    .strip()
                )

                if answer == "\\n":
                    break
                elif answer == "\\a":
                    continue
                elif answer == "\\d":
                    print(f"Definition: {definition}")
                    speak(definition)
                    continue
                elif answer == "\\r":
                    print(f'The word was: "{word}".')
                    speak(f"The word was {word}. It's spelt {' '.join(word)}.")
                    challenging_words.add(word)
                    break
                elif answer != word:
                    print("Incorrect. Try again.")
                    speak(choice(["Incorrect.", "Try again.", "You can do this!"]))
                    incorrect_counter += 1
                    if incorrect_counter > 2:
                        challenging_words.add(word)
                        break
                else:
                    score += 1
                    print("Correct!")
                    speak("Correct!")
                    break

    except (KeyboardInterrupt, EOFError):
        pass
    finally:
        message = (
            f"You dealt with {counter} words out of {counter + len(words)}.\n"
            f"Your score was {score}.\n"
            + (
                "No challenging words."
                if not challenging_words
                else f"Challenging words: {', '.join(challenging_words)}"
            )
        )
        print(message)
        speak(message)
        print("Exiting... Goodbye!")


if __name__ == "__main__":
    main()
