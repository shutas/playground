import google.generativeai as GenAI
from credentials import GOOGLE_API_KEY
from helper import *
from sys import exit

# Global variables
model = None
config = None

def configure():
    # Global variables that will be modified
    global model
    global config

    # Set up API
    GenAI.configure(api_key=GOOGLE_API_KEY)

    # Select Gemini model
    model = GenAI.GenerativeModel("models/gemini-2.0-flash-001")

    # Set generation configuration parameters
    config = GenAI.GenerationConfig(
        max_output_tokens = 2048,
        temperature = 0.5,
    )

def run_chat():
    # Simple chat bot
    print("Hey there! How can I help?\n")

    user_prompt = input("Ask me a question! (type \"exit\" to end chat): ")

    while user_prompt != "exit":
        response = generate_content(model, user_prompt, config)
        print("Gemini: ", response)
        user_prompt = input("Ask me a question! (type \"exit\" to end chat): ")

    print("Gemini: Thanks for chatting!\n")

def end():
    print("The chat has successfully ended.")
    exit(0)

if __name__ == "__main__":
    configure()
    run_chat()
    end()