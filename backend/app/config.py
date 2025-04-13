import os
from dotenv import load_dotenv

load_dotenv()

# api becomes global var of project
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")