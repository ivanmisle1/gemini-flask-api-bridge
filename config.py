import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GEMINI_API_KEY = os.getenv("KEY_API_GEMINI")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL")