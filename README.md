# Bee Prepared

_A tool to help anyone practice spelling with ease and confidence. 🐝✨_

Bee Prepared is an simple - yet effective - interactive Python-based spelling practice tool designed to help users hone their spelling skills. It provides random words from a dictionary file, reads them aloud, and allows users to type their spelling. The tool also tracks challenging words to help users focus on improving specific areas.

---

## Purpose

This project was created in under 1 hour to help prepare for the Bells University Student Association Spelling Bee, 2024. The words in the `dictionary.txt` file provided are sourced directly from that competition, making it a tailored solution for personal preparation.

---

## Features

- **Interactive Practice**: Practice spelling by typing the words you hear.
- **Voice Assistance**: Words and definitions are read aloud using `pyttsx3`.
- **Custom Dictionary**: Use your own `dictionary.txt` file for personalized practice.
- **Tracking Challenging Words**: Words you struggle with are recorded for later review.
- **Real-Time Feedback**: Immediate feedback for correct or incorrect spelling.
- **Helpful Commands**:
  - `\a`: Repeat the word.
  - `\d`: Get the definition of the word.
  - `\n`: Skip to the next word.
  - `\r`: Reveal the word.

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

Install dependencies using:

```bash
pip install pyttsx3
```

---

## Installation

1. Clone this repository or download the source code:

   ```bash
   git clone https://github.com/your-repo-name/spelling-bee-practice-tool.git
   cd spelling-bee-practice-tool
   ```

2. Ensure Python and dependencies are installed.

3. Add a `dictionary.txt` file in the same directory as the script. Each line must contain a word and its definition in the following format:

   ```
   word: definition
   example: a sample or model used to explain something
   ```

---

## Usage

1. Run the program:

   ```bash
   python spelling_bee.py
   ```

2. Follow the on-screen instructions:
   - Enter the path to your dictionary file (default: `dictionary.txt`).
   - Listen to the word spoken aloud.
   - Type the correct spelling or use commands for assistance.

3. Exit the program anytime with `Ctrl+C`.

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


Bee Prepared v1.13
A Spelling Bee Practice Tool, by definite_d
(https://github.com/definite-d/bee-prepared)

Ctrl+C at any point to exit.
Logo from Google's Noto Color Emoji 16.0

Enter a path to a dictionary.txt file (default "dictionary.txt"):
262 words were found in the given dictionary.

Let's begin.

Playing word *******...
Type the word (\a: say again, \d: define, \n: next, \r: reveal): oratory
Correct!
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