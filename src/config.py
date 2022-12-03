import os

from dotenv import load_dotenv


current_directory = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(current_directory, "..", ".env"))
except FileNotFoundError:
    print("No .env file found!")

DATA_FOLDER_PATH = os.path.join(current_directory, "..", "data")

DATABASE_FILE_NAME = os.getenv("DATABASE_FILENAME") or "database.db"
DATABASE_FILE_PATH = os.path.join(DATA_FOLDER_PATH, DATABASE_FILE_NAME)
