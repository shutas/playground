# llm-playground
This is where I save all of my LLM-related code that I write for fun and to learn.  
Each folder under ```llm-playground``` is a separate mini-project that runs independently.

## gemini-demo

### Description
It's a small chat application that calls Gemini. This runs on its own docker container.

### How to Run
1. Generate and paste your Gemini API key in ```credentials.py```
2. Run following commands from repo directory:
```sh
cd gemini-demo
docker build -t gemini-demo .
docker run -it gemini-demo
```

## foundation-sec-8b-chatbot

### Description
It's a small chat application that queries Cisco's new security AI model Foundations-Sec-8B.

### Prerequisites
This chatbot is powered by a local LLM, so I didn't put it inside a container. You'd need a few things for this application to run.

1. Good hardware
   - Storage: 50GB (Although 30GB worked for me)
   - RAM: 16GB  
  (So you definitely need to run something more than a t2.micro LOL... I used a g4dn.4xlarge)
2. Python dependencies (Install them with pip - commands below)
```
pip install torch
pip install git+https://github.com/huggingface/transformers
pip install git+https://github.com/huggingface/accelerate
pip install huggingface_hub
```

### How to Run
1. Run `python main.py` 
