from arduino_service import getDataFromArduino

def getTemperature():
    data = getDataFromArduino()
    temp_c, _, _ = parseData(data)
    temp_f = celsiusToFarenheit(temp_c)
    return temp_f

def getHumidity():
    data = getDataFromArduino()
    _, humidity, _ = parseData(data)
    return humidity

def getAltitude():
    data = getDataFromArduino()
    _, _, alt = parseData(data)
    return alt

def parseData(data):
    return map(float, data.split(","))

def celsiusToFarenheit(temp_c):
    return (temp_c * 9/5) + 32
