import json
import os
import uuid
from datetime import datetime

CODES_FILE = os.path.join(
    os.path.dirname(__file__),
    '..', 'data', 'access_codes', 'access_codes.json'
)

def load_access_codes():
    with open(CODES_FILE, 'r') as f:
        return json.load(f)

def save_access_codes(codes):
    with open(CODES_FILE, 'w') as f:
        json.dump(codes, f, indent=2)

def is_valid_access_code(submitted_code):
    """
    Check if code exists in JSON.
    Returns True only if code exists — 
    does NOT check used/logged_in here.
    Full validation is in auth_routes.
    """
    codes = load_access_codes()
    code = submitted_code.strip()
    return code in codes

def get_code_status(submitted_code):
    """
    Returns the full status of a code:
    - 'not_found'   : code does not exist
    - 'in_use'      : code is currently logged in elsewhere
    - 'available'   : code exists and is free to use
    """
    codes = load_access_codes()
    code = submitted_code.strip()

    if code not in codes:
        return 'not_found'

    code_data = codes[code]

    if code_data.get('logged_in', False):
        return 'in_use'

    return 'available'

def activate_code(submitted_code, session_id):
    """
    Mark a code as actively in use.
    Called when a student successfully logs in.
    Stores the session_id so we can verify
    the same session is using the code.
    """
    codes = load_access_codes()
    code = submitted_code.strip()

    if code in codes:
        codes[code]['logged_in']      = True
        codes[code]['active_session'] = session_id
        codes[code]['used']           = True
        codes[code]['assigned_date']  = datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S'
        )
        save_access_codes(codes)
        return True
    return False

def release_code(submitted_code):
    """
    Release a code when a student logs out.
    Resets logged_in and active_session
    so the code can be used again.
    """
    codes = load_access_codes()
    code = submitted_code.strip()

    if code in codes:
        codes[code]['logged_in']      = False
        codes[code]['active_session'] = ''
        save_access_codes(codes)
        return True
    return False

def get_active_session_for_code(submitted_code):
    """
    Returns the active session ID stored
    for a given code.
    Used to verify the same person is
    returning (not a different person).
    """
    codes = load_access_codes()
    code = submitted_code.strip()

    if code in codes:
        return codes[code].get('active_session', '')
    return ''

def logout_all_students():
    """
    Emergency function — logs out everyone.
    Resets all codes to logged_in: False.
    Call this when you change all codes
    or want to force everyone to re-login.
    """
    codes = load_access_codes()
    for code in codes:
        codes[code]['logged_in']      = False
        codes[code]['active_session'] = ''
    save_access_codes(codes)
    return True