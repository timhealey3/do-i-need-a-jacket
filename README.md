## Do I Need a Jacket?

A small project that reads sensor data from an Arduino Nano 33 BLE and exposes it via a HTTP server. The client sends natural language prompts to the server, which augments the prompt with live sensor data and queries an Local Ollama LLM (default `gemma3:4b`) to generate a short response.


### Prerequisites
- Python 3.12+
- [Ollama](https://ollama.com) installed and running locally
  - Pull a model (default used here):
    ```
    ollama pull gemma3:4b
    ollama serve
    ```
- Arduino 33 BLE and the Arduino IDE

### Arduino Setup
- Flash the Arduino sketch:
   - Open `src/arduino/sensor_read/sensor_read.ino` in Arduino IDE.
   - Select your board/port and upload.
-. Configure the serial port in `src/mcp/arduino_service.py`:
   - Update the `serial.Serial(port='...')` value to match your system (e.g., `/dev/tty.usbmodemXXXX` on macOS).

### Running
1. Start Ollama locally (if not already):
   ```
   ollama serve
   ```
2. Start the MCP server:
   ```
   python src/mcp/mcpServer.py
   ```
   - Server listens on `http://localhost:8080`.
3. In a second terminal, start the client REPL:
   ```
   python src/client/main.py
   ```