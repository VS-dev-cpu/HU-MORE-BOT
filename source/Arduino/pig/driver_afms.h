#include <Adafruit_MotorShield.h>

Adafruit_DCMotor *m_left = AFMS.getMotor(2);
Adafruit_DCMotor *m_right = AFMS.getMotor(1);

int ms = 100;

void init(int max_speed)
{
  ms = max_speed;
  AFMS.begin();
}

void run(int left, int right)
{
  if (left > 0)
  {
    m_left->setSpeed(map(left, 0, 100, 0, ms));
    m_left->run(FORWARD);
  }
  else if (left < 0)
  {
    m_left->setSpeed(map(-left, 0, 100, 0, ms));
    m_left->run(BACKWARD);
  }
  else
  {
    m_left->run(RELEASE);
  }

  if (right > 0)
  {
    m_right->setSpeed(map(right, 0, 100, 0, ms));
    m_right->run(FORWARD);
  }
  else if (right < 0)
  {
    m_right->setSpeed(map(-right, 0, 100, 0, ms));
    m_right->run(BACKWARD);
  }
  else
  {
    m_right->run(RELEASE);
  }
}
