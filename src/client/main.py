import requests
import json

def ask(prompt):
    try:
        response = requests.post(
            "http://localhost:8080",
            json={"prompt": prompt}
        )
        print("Gemma3:4b:", response.json()["response"])
    except:
        raise ConnectionRefusedError("Could not connect to MCP server")

if __name__ == "__main__":
    while True:
        user_input = input("> ")
        if user_input.lower() in ["q", "quit"]:
            break
        try:
            ask(user_input)
        except ConnectionRefusedError:
            print("Could not connect to MCP server")
        except:
            print("An error has occured")
