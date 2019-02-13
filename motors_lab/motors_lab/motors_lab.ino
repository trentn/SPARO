#include "RCServo.h"
#include "AStepper.h"
#include "DCMotor.h"

String inputString = "";         // a String to hold incoming data
bool commandComplete = false;  // whether the string is complete

#define INT_PIN 2

enum STATE{GUI,SENSOR};
volatile int state = SENSOR;

RCServo*  rcservo;
AStepper* stepper;
DCMotor*  dcmotor;

void setup() {
  Serial.begin (9600);
  rcservo = new RCServo();
  stepper = new AStepper();
  dcmotor = new DCMotor();
  inputString.reserve(20);

  attachInterrupt(digitalPinToInterrupt(INT_PIN), buttonStateChange, HIGH);
}


void loop() {
  if(commandComplete && inputString.charAt(0) == 'C'){
    updateState(inputString.substring(2));
    inputString = "";
    commandComplete = false;
  }
  if(state == GUI) {
    if(commandComplete) {
      switch(inputString.charAt(0)){
        case 'R': rcservo->guiCommand(inputString.substring(2));
                  rcservo->update();
                  break;
        case 'S': stepper->guiCommand(inputString.substring(2));
                  stepper->update();
                  break;
        case 'D': break;
        default: break;
      }
      inputString = "";
      commandComplete = false;
    }
  }
  if(state == SENSOR) {
    //Handle RC Servo
    rcservo->sensorRead();
    rcservo->update();

    //Handle Stepper
    stepper->sensorRead();
    stepper->update();
  }
  //dcmotor->update();
}

void updateState(String control_state) {
  switch(control_state.charAt(0)) {
    case 'G': state = GUI;
              break;
    case 'S': state = SENSOR;
              break;
  }
}

void buttonStateChange(){
  delay(1);
  if(digitalRead(INT_PIN) == HIGH){
    if(state == SENSOR) {
      state = GUI;
      Serial.println("C G");
    }
    else if(state == GUI) {
      state = SENSOR;
      Serial.println("C S");
    }
  }
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();

    //if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      commandComplete = true;
      return;
    }
    
    // add it to the inputString:
    inputString += inChar;
  }
}
