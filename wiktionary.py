from regex import sub
from lxml.html import fromstring
from httpx import get, head

URL = "https://en.wiktionary.org/api/rest_v1/page/definition/"
RANDOM_WORD_URL = (
    "https://en.wiktionary.org/wiki/"
    "Special:RandomInCategory/"
    "English_lemmas#English"
)


def _clean_text(text: str) -> str:
    """
    Remove unnecessary HTML tags and whitespace from a string.

    Args:
        text (str): The string to clean.

    Returns:
        str: The cleaned string.
    """
    return fromstring(text).text_content().strip().replace("\n", "")


def get_definition(word: str) -> str:
    """
    Get the definition of a given word from Wiktionary.

    Args:
        word (str): The word to look up.

    Returns:
        tuple[str, str]: A tuple containing the part of speech and the definition of the word.
            If the word is not found, returns (None, None).
    """
    response = get(URL + word)
    if response.status_code == 200:
        data = response.json()["en"][0]
        part_of_speech = data["partOfSpeech"].lower()
        definition = _clean_text(data["definitions"][0]["definition"])
        return part_of_speech, definition
    else:
        print(f"Failed to fetch definition ({response.status_code}).")
        return None, None


def get_random_word() -> str:
    """
    Retrieve a random English lemma word from Wiktionary and fetch its definition.

    Returns:
        tuple[str, tuple[str, str] | None]: The random word and a tuple containing its part of speech and definition.
            If the word cannot be fetched, returns None.
    """
    response = head(RANDOM_WORD_URL, follow_redirects=False)
    if response.status_code == 302:
        word = response.headers["Location"].split("/")[-1]
        return word, get_definition(word)
