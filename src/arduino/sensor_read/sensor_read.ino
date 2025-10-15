/*
  HS300x - Read Sensors

  Reads from the Temperature, Humidity
*/

#include <Arduino_HS300x.h>
#include <Arduino_LPS22HB.h>

float getAltitude(float pressure){
  return 44330 * ( 1 - pow(pressure/101.325, 1/5.255));
}

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!HS300x.begin()) {
    Serial.println("Failed to initialize humidity temperature sensor!");
    while (1);
  }
  if (!BARO.begin()) {
    Serial.println("Failed to initialize pressure sensor!");
    while (1);
  }
}

void loop() {
  // read all the sensor values
  float temperature = HS300x.readTemperature();
  float humidity = HS300x.readHumidity();
  float pressure = BARO.readPressure();
  // calculate values
  float altitude = getAltitude(pressure);
  // output values, comma seperatad
  Serial.print(temperature);
  Serial.print(",");
  Serial.print(humidity);
  Serial.print(",");
  Serial.println(altitude);

  delay(1000);
}