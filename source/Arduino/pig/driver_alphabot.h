#include "AlphaBot.h"
AlphaBot r = AlphaBot();

int ms = 300;

void init()
{
  // dosomething
}

void run(int left, int right)
{
  int l = map(left, -100, 100, -max_speed, max_speed);
  int r = map(right, -100, 100, -max_speed, max_speed)
  r.MotorRun(l, r);
}
