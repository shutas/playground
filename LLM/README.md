# llm-playground
This is where I save all of my LLM-related code that I write for fun and to learn.  
Each folder under ```llm-playground``` is a separate mini-project that runs on its own docker container.

## gemini-demo

### Description
It's a small chat application that calls Gemini.

### How to Run
1. Generate and paste your Gemini API key in ```credentials.py```
2. Run following commands from repo directory:
```sh
cd gemini-demo
docker build -t gemini-demo .
docker run -it gemini-demo
```