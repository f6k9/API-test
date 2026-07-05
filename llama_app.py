import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

def main():
    client = Groq()
    
    # This list acts as your context window history
    history = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
    
    print("Llama 3.1 Chat Session Started. Type 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
            
        # 1. Append your new message to the history window
        history.append({"role": "user", "content": user_input})
        
        # 2. Pass the entire updated history window to the API
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=history,
            temperature=0.0
        )
        
        bot_response = completion.choices[0].message.content
        print(f"Llama: {bot_response}\n")
        
        # 3. Append the model's response to the history window so it remembers it next time
        history.append({"role": "assistant", "content": bot_response})

if __name__ == "__main__":
    main()