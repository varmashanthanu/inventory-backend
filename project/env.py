""" Environment variables manager """
import os
from dotenv import load_dotenv

if env_file_path := os.getenv("ENV_FILE_PATH"):
    print(f"[DEBUG]: Found env file variable: {env_file_path}")
    load_dotenv(dotenv_path=env_file_path)
else:
    print(f"[DEBUG] Did not find any env file config")
    load_dotenv()

DEBUG = os.getenv("DEBUG", False)
SECRET_KEY = os.getenv("SECRET_KEY", NotImplemented)

# Databases
POSTGRES_USER = os.getenv("POSTGRES_USER", "")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", ""))
POSTGRES_DB = os.getenv("POSTGRES_DB", "")
POSTGRES_ENDPOINT = os.getenv("POSTGRES_ENDPOINT", "")
PROD_DB_ALIAS = "default"
