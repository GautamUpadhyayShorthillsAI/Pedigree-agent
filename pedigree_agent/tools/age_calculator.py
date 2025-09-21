"""Tools for calculating age from date of birth."""
from datetime import datetime
from google.adk.tools import FunctionTool

def calculate_age_from_dob(dob: str) -> int:
    """
    Calculates age from a date of birth string provided in dd/mm/yyyy format.
    Returns the calculated age as an integer.
    """
    try:
        birth_date = datetime.strptime(dob, "%d/%m/%Y")
        today = datetime.today()
        age = (
            today.year
            - birth_date.year
            - ((today.month, today.day) < (birth_date.month, birth_date.day))
        )
        return age
    except ValueError:
        return -1  # Indicates an error in date format

age_calculator_tool = FunctionTool(calculate_age_from_dob)