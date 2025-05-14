from dotenv import load_dotenv
import os

# Loading the .env file
load_dotenv()

# accessing the API key
api_key = os.getenv('OPENAI_API_KEY')

print(api_key)