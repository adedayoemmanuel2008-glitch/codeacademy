import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_ENV = os.environ.get('FLASK_ENV', 'development')

    # Keep students logged in for 90 days
    PERMANENT_SESSION_LIFETIME = timedelta(days=90)

    # This is the critical line — forces the session cookie
    # to persist even after the browser is fully closed
    SESSION_COOKIE_SAMESITE = 'Lax'
    SESSION_COOKIE_SECURE = False  # Change to True on Render (HTTPS)