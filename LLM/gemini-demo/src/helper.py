def generate_content(model, prompt, config):
    response = model.generate_content(prompt, generation_config=config)
    return response.text