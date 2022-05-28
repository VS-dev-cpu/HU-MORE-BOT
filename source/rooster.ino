#include <Servo.h>

Servo s;

void mouth(bool en)
{
  if (en)
  {
    s.write(75);
  }
  else
  {
    s.write(90);
  }
}

void setup() {
  s.attach(9);
  Serial.begin(9600);
  mouth(false);
}

void loop() {
  mouth(false);
  while (Serial.available() > 0)
  {
    switch (Serial.parseInt())
    {   
      case 1:
        mouth(true);
        delay(2000);
        break;

      default:
        mouth(false);
        break;
    }
  }
}
