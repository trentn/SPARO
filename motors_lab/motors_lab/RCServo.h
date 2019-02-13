#include <Servo.h>

#define SERVO_PIN 7

class RCServo {
  public:
    Servo servo;
    int potpin = A0;  // analog pin used to connect the potentiometer
    volatile int degree = 0;

    RCServo(){
      servo.attach(SERVO_PIN);
    }
    
    void update(){
      servo.write(degree);
    }
    
    void sensorRead(){
      int pot = analogRead(potpin);
      degree = map(pot, 0, 1023, 0, 180);
      double voltage = map(pot, 0, 1023, 0, 5);
      /*Serial.print("P ");
      Serial.println(voltage);*/
    }

    void guiCommand(String command){
      degree = command.toInt();
    }
};
