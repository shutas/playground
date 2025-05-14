import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Initialize tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("fdtn-ai/Foundation-Sec-8B")
model = AutoModelForCausalLM.from_pretrained("fdtn-ai/Foundation-Sec-8B")

# Ask for a question
print()
prompt=input("Enter your question here (type 'q' to quit): ")
print()
print("=== Printing warnings here, but no worries ===")

while(prompt != "q"):

    prompt=prompt + " And keep your response short, like around 100 words."

    # Tokenize user prompt
    inputs = tokenizer(prompt, return_tensors="pt", verbose=False)

    # Feed user prompt to Foundations-Sec-8B model
    outputs = model.generate(
        inputs["input_ids"],
        max_new_tokens=150,
        do_sample=True,
        temperature=0.1,
        top_p=0.9,
    )

    # Print model output
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    response = response.replace(prompt, "").strip()
    print("=== Alrighty, no more warnings from here on out ===")
    print()
    print(response)
    print()

    # Ask for another question
    prompt=input("Enter your question here (type 'q' to quit): ")