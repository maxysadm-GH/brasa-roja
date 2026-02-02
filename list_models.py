# -*- coding: utf-8 -*-
from google import genai

client = genai.Client(api_key="AIzaSyAu9WSLO7DKlCSl_SFdzlw8X7Bx0XQx1PI")

print("Available models:")
for model in client.models.list():
    print(f"  - {model.name}")
    if hasattr(model, 'supported_generation_methods'):
        print(f"    Methods: {model.supported_generation_methods}")
