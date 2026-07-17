import json
import os
from datetime import datetime

# Path to the access codes JSON file
ACCESS_CODES_PATH = os.path.join('data', 'access_codes', 'access_codes.json')


def load_access_codes():
    """Reads and returns the full access codes dictionary from the JSON file."""
    with open(ACCESS_CODES_PATH, 'r') as file:
        return json.load(file)


def save_access_codes(codes_data):
    """Writes the updated access codes dictionary back to the JSON file."""
    with open(ACCESS_CODES_PATH, 'w') as file:
        json.dump(codes_data, file, indent=2)


def is_valid_access_code(submitted_code):
    """
    Checks if a submitted access code exists in the JSON database.
    Returns True if valid, False if invalid.
    """
    codes_data = load_access_codes()

    # Normalize the submitted code (remove extra spaces, make uppercase)
    submitted_code = submitted_code.strip().upper()

    if submitted_code not in codes_data:
        return False

    code_info = codes_data[submitted_code]

    # Mark this code as used and record the date, only the first time it's used
    if not code_info.get('used'):
        code_info['used'] = True
        code_info['assigned_date'] = datetime.now().strftime('%Y-%m-%d')
        save_access_codes(codes_data)

    return True