# app/llm.py

from huggingface_hub import InferenceApi

def generate_text(prompt):
    api = InferenceApi(repo_id="gpt2")
    result = api(inputs=prompt)
    return result
