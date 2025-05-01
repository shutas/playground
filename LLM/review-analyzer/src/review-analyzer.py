import google.generativeai as GenAI
from credentials import GOOGLE_API_KEY
from helper import *
from sys import exit

# Global variables
model = None
config = None

def configure_llm():
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

def run_analyzer():
    # TODO: Enter analyzer logic here
    return

def end_app():
    print("The analyzer has successfully ended.")
    exit(0)

if __name__ == "__main__":
    configure_llm()
    run_analyzer()
    end_app()