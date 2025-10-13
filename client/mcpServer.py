import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from ollamaClient import query_ollama
from util import getAltitude, getTemperature, getHumidity

class MCPHandler(BaseHTTPRequestHandler):
    routingMap = {
        "temp": ["temp", "temperature"], "jacket": ["jacket", "coat"], "humidity": ["humidity", "humid"], "altitude": ["alt", "altitude"]
        }

    def handle_jacket(self):
            temp = getTemperature()
            prompt = f" The temperature is {temp}°F. Keep response to one sentence. Give a yes or no, and say what kind of jacket I will need."
            return prompt
    
    def handle_temperature(self):
            temp = getTemperature()
            prompt = f" The temperature is {temp}°F. Keep response to one sentence."
            return prompt
    
    def handle_humidity(self):
            humidity = getHumidity()
            prompt =  f" The humidity is {humidity}. Keep response to one sentence. Give a simple response on how the humidity will feel to a person"
            return prompt

    def handle_altitude(self):
            altitude = getAltitude()
            prompt = f"this altitude in meters is {altitude}. Keep response to one sentence."
            return prompt

    def in_routing(self, prompt, key):
        return any(word in prompt for word in self.routingMap[key])

    def routingLogic(self, prompt):
        match prompt:
            case prompt if self.in_routing(prompt, "jacket"):
                prompt += self.handle_jacket()
            case prompt if self.in_routing(prompt, "temp"):
                prompt += self.handle_temperature()
            case prompt if self.in_routing(prompt, "humidity"):
                prompt += self.handle_humidity()
            case prompt if self.in_routing(prompt, "altitude"):
                prompt += self.handle_altitude()
        return prompt

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        message = json.loads(body)
        prompt = message.get("prompt", "").lower()
        prompt = self.routingLogic(prompt)
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

