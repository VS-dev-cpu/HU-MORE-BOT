#include <Adafruit_MotorShield.h>

Adafruit_MotorShield AFMS = Adafruit_MotorShield();
Adafruit_DCMotor *left_m = AFMS.getMotor(1);
Adafruit_DCMotor *right_m = AFMS.getMotor(2);

int speed_a = 100;
int speed_b = 100;
int turn = 800;

int sensor = 12;

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

void house()
{
  forward(1000);
  right(turn);
  forward(1000);
  right(turn);
  forward(1000);
  left(turn);
}

void dance(int a)
{
  for (int i = 0; i < a; i++)
  {
    right(500);
    left(500);
    forward(500);
    backward(500);

    left(500);
    right(500);
    backward(500);
    forward(500);

  }
  brake();
}

void avoid()
{
  left(turn);
  forward(1000);
  right(turn);
  forward(1000);
  right(turn);
  forward(1000);
  left(turn);
}

void setup() {
  Serial.begin(9600);
  AFMS.begin();
  pinMode(sensor, INPUT);
  brake();
}

int state = 0;

void loop() {
  switch (Serial.parseInt())
  {
    case 1:
      forward(0);
      break;

    case 2:
      backward(0);
      break;

    case 3:
      right(0);
      break;

    case 4:
      left(0);
      break;

    case 10:
      house();
      break;

    case 20:
      avoid();
      break;

    case 30:
      dance(5);
      break;

    default:
      break;
  }
}
