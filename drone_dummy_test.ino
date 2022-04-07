String pwm = "0";
int rpm;
float currentVal;
float voltageVal;

String loadCell_1 = "2121.4";
String loadCell_2 = "212.4";
String loadCell_3 = "-212.4";

int extraTime = 0;
int extratime_;

void setup() {
  Serial.begin(57600);
  extratime_ = millis();
}

void loop() {
  rpm_main();
  Serial.print(millis() - extratime_);
  Serial.print(",");
  Serial.print(pwm.toInt());
  Serial.print(",");
  Serial.print(voltageMeasurement());
  Serial.print(",");
  Serial.print(currentMeasurement());
  Serial.print(",");
  Serial.print(rpm);
  Serial.print(",");
  Serial.print(loadCell_1);
  Serial.print(",");
  Serial.print(loadCell_2);
  Serial.print(",");
  Serial.println(loadCell_3);
}


void rpm_main()
{
  rpm = 5214;
}

float currentMeasurement()
{
  currentVal = 1.23;
  return currentVal;
}

float voltageMeasurement()
{
  voltageVal = 24.2;
  return voltageVal;
}
