import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

# UPDATE: Use 'gemini-2.5-flash' (Current stable workhorse) 
# OR 'gemini-3-flash' (Newest high-performance model)
model = genai.GenerativeModel('gemini-2.5-flash')

def get_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"I ran into an issue: {e}"