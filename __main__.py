"""
Bee Prepared.
A Spelling Bee Practice Tool.

Copyright (c) 2024, Divine Afam-Ifediogor (definite_d)
This project is licensed under the MIT License. See the LICENSE file for more details.
"""

from .tts import speak
from ._ascii_art import art
from .wordbank import WordBank, Word
from random import randint, choice

from pathlib import Path


VERSION = "1.15"
DEFAULT_WORDBANK = "./wordbanks/easy.txt"


class Session:

    def __init__(self):
        self.challenging_words: set[str] = set()
        self.easy_words: set[str] = set()
        self.accuracy: float = 0
        self.words_encountered: int = 0
        self.wordbank: WordBank | None = None

    def reset(self):
        self.challenging_words = set()
        self.easy_words = set()
        self.accuracy = 0
        self.words_encountered = 0

    @staticmethod
    def introduce():
        print(art)

        print(f"Bee Prepared v{VERSION}")
        print(
            "A Spelling Bee Practice Tool, by definite_d\n"
            "(https://github.com/definite-d/bee-prepared)\n\n"
            "Ctrl+C at any point to stop."
        )
        print("Logo from Google's Noto Color Emoji 16.0")

        speak(
            "     Welcome to Bee Prepared: a Spelling Bee Practice Tool, by definite d."
        )

    def set_up_wordbank(self):
        wordbank_path = None
        while not wordbank_path:
            wordbank_path = Path(
                input(f"\nEnter a path to a wordbank file: ") or DEFAULT_WORDBANK
            )
            if not wordbank_path.exists():
                print("File not found. Please try again.")
                wordbank_path = None
                continue
        self.wordbank = WordBank(wordbank_path)
        print(f"\n{self.wordbank}")
        speak(
            f"Wordbank: {self.wordbank.title if self.wordbank.title else ''}, "
            f"{self.wordbank.word_count} words found."
        )
        print("\nLet's begin\n")
        speak("Let's begin")

    def run(self):

        self.introduce()
        self.set_up_wordbank()
        incorrect_counter: int = 0
        speak_at_start_of_loop: bool = True
        words = self.randomized_practice()

        try:
            while words:
                word = next(words)
                self.words_encountered += 1
                incorrect_counter = 0
                answer = None

                while answer != word.word:

                    if not speak_at_start_of_loop:
                        speak_at_start_of_loop = True

                    else:
                        print(f"Playing word...")
                        speak(word.pronunciation or word.word)
                    answer = input("Type the word or a command (\h for help): ").lower()
                    if answer == word.word.lower():
                        print("Correct!")
                        speak("Correct!")
                        self.accuracy = (
                            (self.accuracy * self.words_encountered) + 1
                        ) / (self.words_encountered + 1)
                        if not incorrect_counter:
                            self.easy_words.add(word.word)
                        break
                    elif answer == "\\h":
                        help_text = (
                            "\n"
                            "Commands:\n"
                            "\\h: Help - Show this help message.\n"
                            "\\a: Again - Repeat the word.\n"
                            "\\s: Slowly - Repeat the word, slowly.\n"
                            "\\d: Define - Get the definition of the word.\n"
                            "\\r: Reveal - Reveal the word and move to the next word.\n"
                            "\\q: Quit - Quit the program."
                            "\nCommands are non-case-sensitive.\n"
                            "\n"
                        )
                        print(help_text)
                        speak_at_start_of_loop = False
                    elif answer == "\\a":
                        print(f"Playing word...")
                        speak(word.pronunciation or word.word)
                        speak_at_start_of_loop = False
                    elif answer == "\\s":
                        print(f"Playing word...")
                        speak(word.pronunciation or word.word, 0.6)
                        speak_at_start_of_loop = False
                    elif answer == "\\d":
                        if not word.definition:
                            print(
                                "The word has no definition in the wordbank. Looking up online..."
                            )
                            speak("Undefined word. Looking up.")
                            try:
                                self.wordbank.update_definition_online(word)
                            except ValueError:
                                print("Failed to fetch the definition from Wiktionary.")
                                speak("Failed to fetch the definition.")
                                continue
                            else:
                                if not word.definition:
                                    print("No definition found.")
                                    speak("No definition found.")
                                    continue
                        print(f"Definition: {word.definition}")
                        speak(word.word)
                        if word.part_of_speech:
                            speak(word.part_of_speech)
                        speak(word.definition)
                        speak_at_start_of_loop = False
                    elif answer == "\\r":
                        print(f'The word was: "{word.word}".')
                        speak(
                            f"The word was {word.pronunciation or word.word}. It's spelt,"
                        )
                        speak(", ".join(word.word), 0.84)
                        speak(f", {word.pronunciation or word.word}.")
                        self.challenging_words.add(word.word)
                        break
                    elif answer == "\\q":
                        raise KeyboardInterrupt
                    else:
                        print("Incorrect. Try again.")
                        speak(choice(["Incorrect.", "Wrong.", "Try again."]))
                        incorrect_counter += 1
                        if incorrect_counter > 2:
                            self.challenging_words.add(word.word)
                            incorrect_counter = 0
        except (KeyboardInterrupt, EOFError):
            pass

        finally:

            def _word(integer: int):
                return "words" if integer > 1 else "word"

            def _these(integer: int):
                return "these" if integer > 1 else "this"

            message = f"\n\nYou dealt with {self.words_encountered} {_word(self.words_encountered)} out of {self.wordbank.word_count}, with an average accuracy of {self.accuracy*100:.0f}%.\n"
            message += (
                ""
                if not self.challenging_words
                else (
                    f"You found {_these(len(self.challenging_words))} {len(self.challenging_words)} {_word(len(self.challenging_words))} challenging: "
                    f"\n{', '.join(self.challenging_words)}\n"
                )
            ) + (
                ""
                if not self.easy_words
                else (
                    f"You found {_these(len(self.easy_words))} {len(self.easy_words)} {_word(len(self.easy_words))} easiest: "
                    f"\n{', '.join(self.easy_words)}\n"
                )
            )
            self.wordbank.save_to_file()
            print(message)
            speak(message)
            input("Press enter to exit.")
            print("Exiting... Goodbye!")

    def randomized_practice(self):
        word_list = self.wordbank.word_list
        while word_list:
            index = randint(0, len(word_list) - 1)
            word = self.wordbank[word_list.pop(index)]
            yield word


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
    session = Session()
    session.run()
    return


if __name__ == "__main__":
    main()
