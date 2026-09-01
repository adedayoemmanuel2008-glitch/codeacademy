import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_ENV  = os.environ.get('FLASK_ENV', 'development')

    # Session settings
    PERMANENT_SESSION_LIFETIME = timedelta(days=90)
    SESSION_COOKIE_SAMESITE    = 'Lax'
    SESSION_COOKIE_SECURE      = False  # Change to True on Render

    # ── SESSION VERSION ──
    # Change this number to force ALL students to log out
    # Example: change 1 to 2 and push to GitHub
    # Everyone gets logged out automatically
    SESSION_VERSION = 1