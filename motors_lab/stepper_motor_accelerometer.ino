#include <Stepper.h>
#include <Wire.h>
#include <SparkFun_MMA8452Q.h>

//const int groundpin = 18;             // analog input pin 4 -- ground
//const int powerpin = 19;              // analog input pin 5 -- voltage
//const int xpin = A3;                  // x-axis of the accelerometer
//const int ypin = A2;                  // y-axis
//const int zpin = A1;                  // z-axis (only on 3-axis models)
const int StepsPerRevolution=200;
int stepcount=0;
Stepper myStepper (StepsPerRevolution, 8,9,10,11);
MMA8452Q accel;

void setup() {
  // initialize the serial communications:
  myStepper.setSpeed(60);
  accel.init();
  

  Serial.begin(9600);

  // Provide ground and power by using the analog inputs as normal digital pins.
  // This makes it possible to directly connect the breakout board to the
  // Arduino. If you use the normal 5V and GND pins on the Arduino,
  // you can remove these lines.
  //pinMode(groundpin, OUTPUT);
  //pinMode(powerpin, OUTPUT);
  //digitalWrite(groundpin, LOW);
  //digitalWrite(powerpin, HIGH);
}



void loop() {
  accel.read();
  Serial.print("X:");
  Serial.print(accel.cx);
  Serial.print(", Y: ");
  Serial.print(accel.cy);
  Serial.print(", Z: ");
  Serial.println(accel.cz);

  if (accel.cx>accel.cy and accel.cx>accel.cz)
  {
    Serial.println("clockwise, X axis has higher acceleration");
    myStepper.step(StepsPerRevolution);
    //delay(500); 
   }

  if (accel.cy>accel.cz and accel.cy>accel.cx)
  {
    Serial.println("anticlockwise, y axis has higher acceleration");
    myStepper.step(-StepsPerRevolution);
    //delay(500); 
  }
  if (accel.cz>accel.cx and accel.cz>accel.cy)
  {
    myStepper.step(StepsPerRevolution);
    delay(500);
    Serial.println("Z axis has higher acceleration");
    myStepper.step(-StepsPerRevolution);
    delay(500);
    
  }
  else
  {
    myStepper.step(StepsPerRevolution);
    delay(1000);
  }
}
