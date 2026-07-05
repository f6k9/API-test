import os
from dotenv import load_dotenv
from google import genai
from google.genai import types  # Import types to access GenerateContentConfig

load_dotenv()

def main():
    client = genai.Client()
    
    print("Gemini Chat Session Started with custom configuration. Type 'exit' to quit.\n")
    
    # Initialize a continuous chat session and pass the temperature config here
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            temperature=1.2  # Adjust between 0.0 and 2.0 to control creativity
        )
    )
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
            
        # Send message to the ongoing context window
        response = chat.send_message(user_input)
        print(f"Gemini: {response.text}\n")

if __name__ == "__main__":
    main()