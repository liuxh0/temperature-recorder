// TMP36 used
const int SENSOR_PIN = A0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int input = analogRead(SENSOR_PIN);
  float voltage = (input / 1024.0) * 5.0;
  float temperature = (voltage - 0.5) * 100;

  Serial.println(temperature);
  delay(1000);
}
