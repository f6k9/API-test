import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def main():
    client = Groq()
    print("Sending request to Llama 3.1 via Groq...")
    
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant", 
        messages=[{"role": "user"
        , "content": "can you explain the meaning of API"}],
        temperature=0.7
    )
    print("\n--- Llama Response ---")
    print(completion.choices[0].message.content)

if __name__ == "__main__":
    main()