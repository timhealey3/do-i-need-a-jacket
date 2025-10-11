from arduino_service import getDataFromArduino

def getTemperature():
    data = getDataFromArduino()
    temp_c, _ = parseData(data)
    temp_f = celsiusToFarenheit(temp_c)
    return temp_f

def getHumidity():
    data = getDataFromArduino()
    _, humidity = parseData(data)
    return humidity

def parseData(data):
    return map(float, data.split(","))

def celsiusToFarenheit(temp_c):
    return (temp_c * 9/5) + 32