#include <Adafruit_MotorShield.h>

Adafruit_MotorShield AFMS = Adafruit_MotorShield();

Adafruit_DCMotor *m_left = AFMS.getMotor(2);
Adafruit_DCMotor *m_right = AFMS.getMotor(1);

int max_speed = 100;

void driver_setup()
{
  AFMS.begin();
}

void run(int left, int right)
{
  if (left > 0)
  {
    m_left->setSpeed(map(left, 0, 100, 0, max_speed));
    m_left->run(FORWARD);
  }
  else if (left < 0)
  {
    m_left->setSpeed(map(-left, 0, 100, 0, max_speed));
    m_left->run(BACKWARD);
  }
  else
  {
    m_left->run(RELEASE);
  }

  if (right > 0)
  {
    m_right->setSpeed(map(right, 0, 100, 0, max_speed));
    m_right->run(FORWARD);
  }
  else if (right < 0)
  {
    m_right->setSpeed(map(-right, 0, 100, 0, max_speed));
    m_right->run(BACKWARD);
  }
  else
  {
    m_right->run(RELEASE);
  }
}
