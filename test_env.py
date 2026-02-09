import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv("OPENROUTER_API_KEY")
print(f"Key loaded: '{key}'")
if key and key.startswith("'") and key.endswith("'"):
    print("WARNING: Key has surrounding quotes!")
