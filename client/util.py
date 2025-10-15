from arduino_service import getDataFromArduino

NO_RESPONSE_FROM_ARDUINO = "The arduino board refused to connect. Please make sure the arduino is connected"

def getTemperature():
    try:
        data = getDataFromArduino()
        temp_c, _, _ = parseData(data)
        temp_f = celsiusToFarenheit(temp_c)
        return temp_f
    except ConnectionError:
        return NO_RESPONSE_FROM_ARDUINO

def getHumidity():
    try:
        data = getDataFromArduino()
        _, humidity, _ = parseData(data)
        return humidity
    except ConnectionError:
        return NO_RESPONSE_FROM_ARDUINO

def getAltitude():
    try:
        data = getDataFromArduino()
        _, _, alt = parseData(data)
        return alt
    except ConnectionError:
        return NO_RESPONSE_FROM_ARDUINO

def parseData(data):
    return map(float, data.split(","))

def celsiusToFarenheit(temp_c):
    return (temp_c * 9/5) + 32
