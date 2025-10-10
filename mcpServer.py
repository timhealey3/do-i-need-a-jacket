import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from ollamaClient import query_ollama
from util import getTemperature

class MCPHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        message = json.loads(body)
        prompt = message.get("prompt", "")
        # TODO change this
        # Simple routing logic
        if "jacket" in prompt.lower():
            temp = getTemperature()
            tempPrompt = f" The temperature is {temp}°F. Keep response to one sentence. Give a yes or no."
            response_text = query_ollama(prompt + tempPrompt)
        else:
            # Let the model decide how to answer
            response_text = query_ollama(prompt)

        response = {
            "type": "mcp_response",
            "response": response_text
        }

        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

def run_server():
    server = HTTPServer(("localhost", 8080), MCPHandler)
    server.serve_forever()

if __name__ == "__main__":
    run_server()

