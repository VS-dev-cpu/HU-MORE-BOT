#include "AlphaBot.h"

AlphaBot rZ = AlphaBot();

int sensor = 8;

void house()
{
  rZ.MotorRun(-130, -150);
  delay(200);
  rZ.LeftCircle(375);
  rZ.MotorRun(130, 150);
  delay(1000);
  rZ.RightCircle(337);
  rZ.MotorRun(130, 150);
  delay(2000);
  rZ.RightCircle(337);
  rZ.MotorRun(130, 150);
  delay(1000);
  rZ.LeftCircle(375);
}

void dance(int a)
{
  for (int i = 0; i < a; i++)
  {
    delay(400);
  rZ.MotorRun(130, 150);     //1 másodpercig előremegy
  rZ.Brake();

  delay(400);
  rZ.Backward(1200);  //1 másodpercig hátramegy
  rZ.Brake();

  delay(400);
  rZ.LeftCircle(1200);  //1 másodpercig balra tesz egy kört
  rZ.Brake();

  delay(400);
  rZ.Backward(1200);  //1 másodpercig hátramegy
  rZ.Brake();

  delay(400);
  rZ.MotorRun(0, 250);  //Balra tesz egy kört; bal motor sebessége: 0, jobb motor sebessége: 250
  delay(1200);
  rZ.Brake();

  delay(1600);

  
delay(400);
  rZ.MotorRun(130, 150);     //1 másodpercig előremegy
  rZ.Brake();

  delay(400);
  rZ.Backward(1200);  //1 másodpercig hátramegy
  rZ.Brake();

  delay(400);
  rZ.LeftCircle(1200);  //1 másodpercig balra tesz egy kört
  rZ.Brake();

  delay(400);
  rZ.Backward(1200);  //1 másodpercig hátramegy
  rZ.Brake();

  delay(400);
  rZ.MotorRun(250, 0);  //Jobbra tesz egy kört; bal motor sebessége: 250, jobb motor sebessége: 0
  delay(1200);
  rZ.Brake();

  delay(1600);
  }
  brake();
}

void avoid()
{
  rZ.Backward(175);
    rZ.LeftCircle(425);
    rZ.MotorRun(130, 150);
    delay(1750);
    rZ.RightCircle(345);
    rZ.MotorRun(130, 150);
    delay(1750);
    rZ.RightCircle(345);
    rZ.MotorRun(130, 150);
    delay(1750);
    rZ.LeftCircle(425);
    rZ.MotorRun(130, 150);
}

void setup() {
  Serial.begin(9600);
  pinMode(sensor, INPUT);
  rZ.SetSpeed(150);
}

int state = 0;

void loop() {
  while (Serial.available() > 0)
  {
    switch (Serial.parseInt())
    {
      case 1:
        house();
        state = 1;
        break;

      case 2:
        state = 2;
        break;

      default:
        break;
    }
  }

  switch (state)
  {
    case 0:
      // Wait
      break;

    case 1:
      if (!digitalRead(sensor))
      {
        avoid();
      }
      else
      {
         rZ.MotorRun(130, 150);
      }
      break;

    case 2:
      dance(5);
      state = 0;
      break;
  }
}
