import os
import sys
sys.path.append('/home/r/root/venv/lib/python3.11/site-packages/')

from app import app as application

if __name__ == '__main__':
    application.run()