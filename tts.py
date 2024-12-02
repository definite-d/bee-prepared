from pyttsx3 import init

ENGINE = init()
DEFAULT_SPEECH_RATE = 0.934


def speak(text: str, speed_factor: float = DEFAULT_SPEECH_RATE):
    """
    Speaks the given text aloud using the pyttsx3 text-to-speech engine.

    Args:
        text (str): The text to be spoken.
        speed_factor (float, optional): The speed factor for the speech rate. Defaults to 0.96.

    Returns:
        None
    """
    rate = ENGINE.getProperty("rate")
    ENGINE.setProperty("rate", speed_factor * rate)
    ENGINE.say(text)
    ENGINE.setProperty("rate", rate)
    ENGINE.runAndWait()
