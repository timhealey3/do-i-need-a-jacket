import requests
import json

GENERIC_ERROR_OCCURRED = "An error has occured"
COULD_NOT_CONNECT_MCP_SERVER = "Could not connect to MCP server"

def ask(prompt):
    try:
        response = requests.post(
            "http://localhost:8080",
            json={"prompt": prompt}
        )
        displayResponse(response)
    except:
        raise ConnectionRefusedError(COULD_NOT_CONNECT_MCP_SERVER)

def displayResponse(response):
    print("Gemma3:4b:", response.json()["response"])

def coreLoop():
    while True:
        user_input = input("> ")
        if user_input.lower() in ["q", "quit"]:
            return False
        try:
            ask(user_input)
        except ConnectionRefusedError:
            print(COULD_NOT_CONNECT_MCP_SERVER)
        except:
            print(COULD_NOT_CONNECT_MCP_SERVER)


if __name__ == "__main__":
    coreLoop()
        