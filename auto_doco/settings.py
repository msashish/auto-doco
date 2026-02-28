import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

GITHUB_API_URL = os.environ.get("GITHUB_API_URL")
GITHUB_API_TOKEN = os.environ.get("GITHUB_API_TOKEN")
