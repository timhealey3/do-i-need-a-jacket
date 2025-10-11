/*
  HS300x - Read Sensors

  Reads from the Temperature, Humidity
*/

#include <Arduino_HS300x.h>

void setup() {
  Serial.begin(9600);
  while (!Serial);

  if (!HS300x.begin()) {
    Serial.println("Failed to initialize humidity temperature sensor!");
    while (1);
  }
}

void loop() {
  // read all the sensor values
  float temperature = HS300x.readTemperature();
  float humidity    = HS300x.readHumidity();
  // output values, comma seperatad
  Serial.print(temperature);
  Serial.print(",");
  Serial.println(humidity);

  delay(1000);
}