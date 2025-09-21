"""Tools for guessing gender from a name."""
import gender_guesser.detector as gender
from google.adk.tools import FunctionTool

def guess_gender_from_name(name: str) -> str:
    """
    Guesses the gender from a given first name.
    Returns 'male', 'female', or 'unknown'.
    """
    detector = gender.Detector()
    first_name = name.split(" ")[0]
    gender_result = detector.get_gender(first_name)
    if "female" in gender_result:
        return "female"
    elif "male" in gender_result:
        return "male"
    else:
        return "unknown"

gender_guesser_tool = FunctionTool(guess_gender_from_name)