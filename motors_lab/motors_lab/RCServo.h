#include <Servo.h>

class RCServo {
  public:
    Servo servo;
    int potpin = A0;  // analog pin used to connect the potentiometer
    volatile int degree = 0;

    RCServo(){
      servo.attach(9);
    }
    
    void update(){
      servo.write(degree);
    }
    
    void sensorRead(){
      int pot = analogRead(potpin);
      degree = map(pot, 0, 1023, 0, 180);
    }

    void guiCommand(String command){
      degree = command.toInt();
    }
};
