import requests
import json

def ask(prompt):
    response = requests.post(
        "http://localhost:8080",
        json={"prompt": prompt}
    )
    print("Gemma3:4b:", response.json()["response"])

if __name__ == "__main__":
    while True:
        user_input = input("> ")
        if user_input.lower() in ["q", "quit"]:
            break
        ask(user_input)

