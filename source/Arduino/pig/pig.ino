#define IS_PIGS false

#if IS_PIGS
#include "driver_afms.h"
#else
#include "driver_alphabot.h"
#endif

void setup()
{
  init();
}

void loop()
{
}
