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
      Serial.print("R ");
      Serial.print(degree);
      Serial.println(" degrees");
    }
    
    void sensorRead(){
      int pot = analogRead(potpin);
      degree = map(pot, 0, 1023, 0, 180);
      double voltage = (pot*5.0)/1023;
      Serial.print("P ");
      Serial.print(voltage);
      Serial.println("V");
    }

    void guiCommand(String command){
      degree = command.toInt();
    }
};
