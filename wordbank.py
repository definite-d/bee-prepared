"""
Format:
// comment
# title: title
word <pronunciation> [part of speech]: definition
"""

from pathlib import Path
from io import FileIO
from dataclasses import dataclass, field
from regex import findall, DOTALL, search, match
from enum import StrEnum
from httpx import HTTPError, ConnectError, NetworkError
from .wiktionary import get_definition


class PartOfSpeech(StrEnum):
    # Source: Wikipedia
    ADFIX = "adfix"
    ADJECTIVE = "adjective"
    ADNOUN = "adnoun"
    ADVERB = "adverb"
    ARTICLE = "article"
    AUXILIARY_VERB = "auxiliary verb"
    CARDINAL_NUMBER = "cardinal number"
    COLLECTIVE_NUMERAL = "collective numeral"
    CONJUNCTION = "conjunction"
    CONJUNCTIONAL_PHRASE = "conjunctional phrase"
    CONVERB = "converb"
    COVERB = "coverb"
    DEMONSTRATIVE_DETERMINER = "demonstrative determiner"
    DEMONSTRATIVE_PRONOUN = "demonstrative pronoun"
    DETERMINATIVE = "determinative"
    DETERMINER = "determiner"
    FRACTIONAL_NUMBER = "fractional number"
    GERUND = "gerund"
    IDEOPHONE = "ideophone"
    INDEFINITE_PRONOUN = "indefinite pronoun"
    INFINITIVE = "infinitive"
    INTERJECTION = "interjection"
    INTERJECTIONAL_PHRASE = "interjectional phrase"
    INTERROGATIVE_PRONOUN = "interrogative pronoun"
    INTRANSITIVE_VERB = "intransitive verb"
    MULTIPLICATIVE_NUMBER = "multiplicative number"
    MULTIPLICATIVE_NUMERAL = "multiplicative numeral"
    NOUN = "noun"
    NUMBER = "number"
    NUMERAL = "numeral"
    ORDINAL = "ordinal"
    ORDINAL_NUMBER = "ordinal number"
    PARTICIPLE = "participle"
    PARTICLE = "particle"
    PART_OF_SPEECH = "part of speech"
    PERSONAL_PRONOUN = "personal pronoun"
    PHRASAL_PREPOSITION = "phrasal preposition"
    POSSESSIONAL_ADJECTIVE = "possessional adjective"
    POSSESSIVE_ADJECTIVE = "possessive adjective"
    POSSESSIVE_DETERMINER = "possessive determiner"
    POSSESSIVE_PRONOUN = "possessive pronoun"
    POSTPOSITION = "postposition"
    PREDICATIVE = "predicative"
    PREPOSITION = "preposition"
    PREVERB = "preverb"
    PRIVATIVE_ADJECTIVE = "privative adjective"
    PRONOMINAL_PHRASE = "pronominal phrase"
    PRONOUN = "pronoun"
    QUASI_ADJECTIVE = "quasi-adjective"
    RECIPROCAL_PRONOUN = "reciprocal pronoun"
    REFLEXIVE_PRONOUN = "reflexive pronoun"
    RELATIVE_ADJECTIVE = "relative adjective"
    RELATIVE_PRONOUN = "relative pronoun"
    SHADOW_PRONOUN = "shadow pronoun"
    SPEECH_DISFLUENCY = "speech disfluency"
    SUBSTANTIVE = "substantive"
    TRANSITIVE = "transitive"
    TRANSITIVE_VERB = "transitive verb"
    VERBAL_NOUN = "verbal noun"


@dataclass
class Word:
    """A class representing a word from a word bank file."""

    line: int
    word: str
    pronunciation: str | None
    part_of_speech: PartOfSpeech | None
    definition: str | None

    def __post_init__(self):
        self.word = self.word.strip()
        if self.pronunciation is not None:
            self.pronunciation = self.pronunciation.strip()
        if self.definition is not None:
            self.definition = self.definition.strip()
        if self.part_of_speech is not None:
            self.part_of_speech = PartOfSpeech(self.part_of_speech)

    def __str__(self):
        pronounciation = f" <{word.pronunciation}>" if word.pronunciation else ""
        part_of_speech = f" [{word.part_of_speech}]" if word.part_of_speech else ""
        definition = f": {word.definition}" if word.definition else ""
        return f"{self.word}{pronounciation}{part_of_speech}{definition}"


class WordBank:
    """A class representing a word bank file."""

    def __init__(self, filepath: Path):
        """
        Initialize a WordBank object from a file path.

        Args:
            filepath: The path to the word bank file.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        self.filepath = Path(filepath)
        if not self.filepath.exists():
            raise FileNotFoundError(f"The word bank file {filepath} does not exist.")
        self.title = None
        self.words = {}
        self.parse()

    def parse(self):
        """
        Parse the word bank file and populate the `words` attribute.

        Raises:
            FileNotFoundError: If the file does not exist.
        """
        with open(self.filepath, "r") as file:
            self.parse_words(file)

    @staticmethod
    def _parse_line(index: int, line: str):
        """Parses a single line from a word bank file into a Word object.

        Args:
            index: The index of the word in the word bank file.
            line: The line from the word bank file to parse.

        Returns:
            A Word object if the line was successfully parsed, otherwise None.
        """
        m = search(
            (
                r"(?P<word>[.\w\s-]+)\s*(<(?P<pronunciation>[\w-]*)>)?\s*(\[(?P<part_of_speech>[\w\s]*)\])?(:\s*(?P<definition>.*))?"
            ),
            line.strip(),
        )
        if m:
            return Word(line=index, **m.groupdict())

    def parse_words(self, file: FileIO):
        """Parses the words from the given file object into the WordBank.

        Args:
            file: A file object open for reading containing the words to be parsed.
        """
        for index, line in enumerate(file):
            if line.startswith("//"):
                continue
            if line.startswith("#"):
                title = match(r"\s*#\s*title\s*:\s*(?P<title>.*)", line)
                if title:
                    self.title = title.groupdict()["title"]
                continue
            word: Word | None = self._parse_line(index, line)
            if word:
                self.words[word.word] = word

    @property
    def word_count(self):
        """The number of words in the word bank."""
        return len(self.words)

    @property
    def word_list(self):
        """A list of all words in the word bank."""
        return list(self.words.keys())

    def __getitem__(self, word_or_index: str | int):
        """
        Retrieve a Word object by word or index from the word bank.

        Args:
            word_or_index (str | int): The word as a string or its index as an integer.

        Returns:
            Word: The Word object corresponding to the given word or index.

        Raises:
            KeyError: If the word is not found in the word bank when a string is given.
            IndexError: If the index is out of range when an integer is given.
        """
        if isinstance(word_or_index, str):
            return self.words[word_or_index]
        else:
            return self.words[self.word_list[word_or_index]]

    def __str__(self):
        title_piece = f": {self.title}" if self.title else ""
        return f"WordBank{title_piece} ({self.word_count} words, {str(self.filepath.absolute())!r})"

    def update_definition_online(self, word_or_index: str | int | Word):
        """
        Update the part of speech and definition of a word in the word bank by
        fetching the definition from Wiktionary online.

        Args:
            word_or_index: The word or its index in the word bank to update.

        Raises:
            ValueError: If the word's definition cannot be fetched from Wiktionary.
        """
        if isinstance(word_or_index, (str, int)):
            word: Word = self[word_or_index]
        else:
            word: Word = word_or_index
        try:
            part_of_speech, definition = get_definition(word.word)
        except (HTTPError, ConnectError, NetworkError):
            raise ValueError(f"Failed to fetch definition for {word}")
        word.part_of_speech = part_of_speech
        word.definition = definition

    def save_to_file(self, filepath: str | None):
        """
        Save the word bank to the specified file path or the original file path.

        Args:
            filepath: The file path to save to. If None, the original file path is used.

        Raises:
            FileNotFoundError: If the file does not exist or cannot be written to.
        """
        filepath = filepath or self.filepath
        with open(filepath, "w") as file:
            for word in self.words.values():
                file.write(f"{str(word)}\n")
