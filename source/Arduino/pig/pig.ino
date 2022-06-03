#define IS_PIGS false

#if IS_PIGS
#include "driver_afms.h"
#else
#include "driver_alphabot.h"
#endif

void dance()
{
  for (int i = 0; i < 2; i++)
  {
    // Dance Phase 1

    //Left 1200
    run(0, 100);
    delay(1200);
    run(0, 0);

    delay(400);

    //Right 1200
    run(100, 0);
    delay(1200);
    run(0, 0);

    delay(400);

    //Left 1200
    run(0, 100);
    delay(1200);
    run(0, 0);

    delay(400);

    //Right 1200
    run(100, 0);
    delay(1200);
    run(0, 0);

    delay(400);

    //Left 1600
    run(0, 100);
    delay(1600);
    run(0, 0);

    delay(1600);

    // Dance Phase 2

    //Right 1200
    run(100, 0);
    delay(1200);
    run(0, 0);

    delay(400);

    //Left 1200
    run(0, 100);
    delay(1200);
    run(0, 0);

    delay(400);

    //Right 1200
    run(100, 0);
    delay(1200);
    run(0, 0);

    delay(400);

    //Left 1200
    run(0, 100);
    delay(1200);
    run(0, 0);

    delay(400);

    //Right 1600
    run(100, 0);
    delay(1600);
    run(0, 0);

    delay(1600);
  }
}

void house()
{
  int turn = 800;

  run(50, 50);
  delay(1000);
  run(50, 0);
  delay(turn);

  run(50, 50);
  delay(1000);
  run(50, 0);
  delay(turn);

  run(50, 50);
  delay(1000);
  run(0, 50);
  delay(turn);

  run(0, 0);
}

void setup()
{
  Serial.begin(9600);
  driver_setup();
  run(0, 0);
}

int l, r;
int state = -1;
bool is_housed = true;
int x = 160;

void loop()
{
  if (Serial.available() > 0)
  {
    int msg = Serial.parseInt();

    if (msg == 1000)
    {
      if (is_housed)
      {
        is_housed = false;
        house();
      }
      state = 0;
    }
    else if (msg == 2000)
    {
      state = 1;
    }
    else
    {
      x = map(msg, 0, 320, 100, -100);
    }
  }

  switch (state)
  {
    case 0:
      l = map(x, -100, 100, 0, 60);
      r = map(x, -100, 100, 60, 0);
      run(l, r);
      break;

    case 1:
      dance();
      state = 2;
      break;

    default:
      break;
  }
}
