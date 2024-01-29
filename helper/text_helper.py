
# Global variables
unit = 'GB'

# Constants
RED = "\033[1;31m"
YELLOW = "\033[1;33m"
GREEN = "\033[1;32m"
DEFAULT = "\033[0m"  # Reset
EXPONENTS_MAP = {'BYTES': 0, 'KB': 1, 'MB': 2, 'GB': 3, 'TB': 4}

def size_format(size):
    global unit
    if unit not in EXPONENTS_MAP:
        raise ValueError("Must select from   ['BYTES', 'KB', 'MB', 'GB', 'TB']")
    else:
        res = size / 1024 ** EXPONENTS_MAP[unit]
        return str(round(res, 3)) + unit

def get_font_color(percentage):
    if percentage <= 25:
        return GREEN
    elif percentage <= 50:
        return YELLOW
    else:
        return RED
