#include <Adafruit_MotorShield.h>

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *left_m = AFMS.getMotor(1);
Adafruit_DCMotor *right_m = AFMS.getMotor(2);

int speed_a = 150;
int speed_b = 100;

void forward(int t)
{
  left_m->setSpeed(speed_a);
  right_m->setSpeed(speed_a);
  left_m->run(FORWARD);
  right_m->run(FORWARD);
  delay(t);
}

void backward(int t)
{
  left_m->setSpeed(speed_a);
  right_m->setSpeed(speed_a);
  left_m->run(BACKWARD);
  right_m->run(BACKWARD);
  delay(t);
}

void right(int t)
{
  left_m->setSpeed(speed_b);
  right_m->setSpeed(speed_b);
  left_m->run(FORWARD);
  right_m->run(RELEASE);
  delay(t);
}

void left(int t)
{
  left_m->setSpeed(speed_b);
  right_m->setSpeed(speed_b);
  left_m->run(RELEASE);
  right_m->run(FORWARD);
  delay(t);
}

void brake()
{
  left_m->run(RELEASE);
  right_m->run(RELEASE);
}

void setup() {
  AFMS.begin();
  brake();
}

void loop() {
  switch (Serial.parseInt())
  {
    case 1: //Right
      right(0);
      break;

    case 2: //Left
      left(0);
      break;

    case 3: //Forward
      forward(0);
      break;

    case 4: //Forward
      backward(0);
      break;

    case 10:  //Out of the house
      forward(1000);
      right(700);
      forward(1000);
      right(700);
      forward(1000);
      left(700);
      brake();
      break;

    case 20:  //Dance
      right(500);
      left(500);
      forward(500);
      backward(500);
      brake();
      break;

    case 30:  //Object
      left(700);
      forward(1000);
      right(700);
      forward(2000);
      right(700);
      forward(1000);
      left(700);
      brake();
      break;
  }
}
