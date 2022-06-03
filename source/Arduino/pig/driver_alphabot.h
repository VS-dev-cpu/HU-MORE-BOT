#include "AlphaBot.h"
AlphaBot robot = AlphaBot();

int max_speed = 300;

void driver_setup()
{
  // dosomething
}

void run(int left, int right)
{
  left = map(left, -100, 100, -max_speed, max_speed);
  right = map(right, -100, 100, -max_speed, max_speed);
  robot.MotorRun(left, right);
}
