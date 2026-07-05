import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# Load the API key from the .env file into the system environment
load_dotenv()

def main():
    # Initialize the client. It automatically finds GEMINI_API_KEY.
    client = genai.Client()

    print("Sending request to Gemini...")
    
    # Generate content using the recommended standard model
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='can you list the Audi rs3 2026 specs.',
        config=types.GenerateContentConfig(
            temperature=0.5,  # Adjust this value between 0.0 and 2.0 depending on your needs
        )
    )

    print("\n--- Gemini Response ---")
    print(response.text)

if __name__ == "__main__":
    main()
