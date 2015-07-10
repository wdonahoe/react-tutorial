import os
import json

DEBUG = True

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

THREADS_PER_PAGE = 2

CSRF_ENABLED = True
CSRF_SESSION_KEY = 'i am become death'
SECRET_KEY = 'destroyer of worlds'