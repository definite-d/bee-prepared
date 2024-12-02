# Bee Prepared

<img height="10%">![bee](https://github.com/user-attachments/assets/5ab302bc-1598-477f-815d-a9fff3248b52)</img>



_A tool to help anyone practice spelling with ease and confidence. 🐝✨_

Bee Prepared is an simple - yet effective - interactive Python-based spelling practice tool designed to help users hone their spelling skills. It provides random words from a dictionary file, reads them aloud, and allows users to type their spelling. The tool also tracks challenging words to help users focus on improving specific areas.

---

## Purpose

This project was created in under 1 hour to help prepare for the Bells University Student Association Spelling Bee, 2024.

---

## Features

- **Interactive Practice**: Practice spelling by typing the words you hear.
- **Voice Assistance**: Words and definitions are read aloud using `pyttsx3`.
- **Custom Wordbank**: Use your own `wordbank.txt` file for personalized practice.
- **Tracking Challenging Words**: Words you struggle with are recorded for later review.
- **Real-Time Feedback**: Immediate feedback for correct or incorrect spelling.
- **Automatic Definition Search**: Gets the definitions of words that aren't found in the given wordbank from [Wiktionary](https://wiktionary.org).
- **Helpful Commands**:
  - `\h`: Help - Shows the help message.
  - `\a`: Again - Repeat the word.
  - `\s`: Slowly - Repeat the word, slowly.
  - `\d`: Define - Get the definition of the word.
  - `\r`: Reveal - Reveal the word and move to the next word.
  - `\q`: Quit - Quit the program.

---

## Download for Windows

A precompiled version is available for Windows as a GitHub release. Download it directly from the [Releases](https://github.com/definite-d/bee-prepared/releases) page.

---

## Requirements

- **Python 3.7 or later**
- **Dependencies**:
  - `pyttsx3`: Text-to-speech engine for Python
  - `pathlib`: Standard library for file handling
  - `random`: Standard library for generating random selections
  - `httpx`: Web request library for getting definitions from [Wiktionary](https://wiktionary.org) via [their API](https://en.wiktionary.org/api/rest_v1/#/Page%20content/get_page_definition__term_).

Install dependencies using:

```bash
pip install pyttsx3 httpx
```

---

## Installation

1. Clone this repository or download the source code:

   ```bash
   git clone https://github.com/definite-d/bee-prepared.git
   ```

2. Ensure Python and dependencies are installed.

3. Obtain a wordbank file. Each line must contain a word and its definition in the following format:

   ```
   word <pronunciation> [part-of-speech]: definition
   example <eg-zam-ple> [noun]: a sample or model used to explain something
   ```

---

## Usage

1. Run the program:

   ```bash
   python -m bee-prepared
   ```

2. Follow the on-screen instructions:
   - Enter the path to your dictionary file (default: `./wordbanks/easy.txt`).
   - Listen to the word spoken aloud.
   - Type the correct spelling or use commands for assistance.

3. Exit the program anytime with `Ctrl+C` or the `\q` (Quit) command.

---

## Example Session

```
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


Bee Prepared v1.15
A Spelling Bee Practice Tool, by definite_d
(https://github.com/definite-d/bee-prepared)

Ctrl+C at any point to stop.
Logo from Google's Noto Color Emoji 16.0

Enter a path to a wordbank file: .\bee-prepared\wordbanks\scripps_three_bee.txt

WordBank: Scripps National Spelling Bee - Three Bee Difficulty (141 words, 'D:\\Code\\Python\\Bee Prepared\\bee-prepared\\wordbanks\\scripps_three_bee.txt')

Let's begin

Playing word...
Type the word or a command (\h for help): vermicelli
Correct!
Playing word...
Type the word or a command (\h for help): 
```

---

## Contributing

Contributions are welcome! If you have ideas to improve this tool or want to report a bug, feel free to submit an issue or a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Timeline

- **Development Start:** 28/11/2024
- **First Stable Version:** Completed the same evening.
