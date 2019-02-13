#include "RCServo.h"
#include "Stepper.h"
#include "DCMotor.h"

String inputString = "";         // a String to hold incoming data
bool commandComplete = false;  // whether the string is complete

enum STATE{GUI,SENSOR};
int state = GUI;

RCServo* rcservo;
Stepper* stepper;
DCMotor* dcmotor;

void setup() {
  Serial.begin (9600);
  rcservo = new RCServo();
  stepper = new Stepper();
  dcmotor = new DCMotor();
  inputString.reserve(20);
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
                  break;
        case 'S': break;
        case 'D': break;
        default: break;
      }
      inputString = "";
      commandComplete = false;
    }
  }
  if(state == SENSOR) {
    rcservo->sensorRead();
  }
  
  rcservo->update();
  stepper->update();
  dcmotor->update();
}

void updateState(String control_state) {
  switch(control_state.charAt(0)) {
    case 'G': state = GUI;
              break;
    case 'S': state = SENSOR;
              break;
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
