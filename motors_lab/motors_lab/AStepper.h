#include <SparkFun_MMA8452Q.h>
#include <Stepper.h>

#define STEPPER_PIN1 8
#define STEPPER_PIN2 9
#define STEPPER_PIN3 10
#define STEPPER_PIN4 11

class AStepper {
  public:
  const int stepsPerRevolution = 200;
  Stepper* myStepper;
  MMA8452Q accel;
  volatile int steps = 0;

  AStepper(){
    myStepper = new Stepper(stepsPerRevolution,
                              STEPPER_PIN1,
                              STEPPER_PIN2,
                              STEPPER_PIN3,
                              STEPPER_PIN4);
    accel.init();
    myStepper->setSpeed(60);
  }

  update(){  
    myStepper->step(steps);
    steps = 0;
  }

  void sensorRead(){
    accel.read();

    if (accel.cx>accel.cy and accel.cx>accel.cz)
    {;
      steps = stepsPerRevolution;
     }
  
    if (accel.cy>accel.cz and accel.cy>accel.cx)
    {
      steps = -stepsPerRevolution;
    }
    if (accel.cz>accel.cx and accel.cz>accel.cy)
    {
      steps = 0;
    }
    else
    {
      steps = stepsPerRevolution;
    }

    /*Serial.print("A X:");
    Serial.print(accel.cx);
    Serial.print(", Y: ");
    Serial.print(accel.cy);
    Serial.print(", Z: ");
    Serial.println(accel.cz);*/
  }

  void guiCommand(String command) {
    steps = command.toInt();
    steps = (int)(steps/1.8);
  }
};
