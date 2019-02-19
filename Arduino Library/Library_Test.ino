#include "DC_MotorwEnc_Control.h"

DC_Motor motor1 = DC_Motor(6, 7, 8, 2, 3, 1925);

void setup() {
  motor1.initializeStates();
}

void loop() {
  motor1.setPwm(255);

}

