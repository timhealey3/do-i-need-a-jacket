import serial
import time

def getDataFromArduino():
    # Change to your actual port
    arduino = serial.Serial(port='/dev/tty.usbmodem1101', baudrate=9600, timeout=1)
    time.sleep(2)
        
    data = arduino.readline().decode('utf-8').strip()
    arduino.close()
    
    return data
