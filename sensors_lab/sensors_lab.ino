/*
 * Team Pirates Sensor Lab
 */

#include <Wire.h>
#include <SparkFun_MMA8452Q.h>

#define WINDOWSIZE 10

//acclerometer object
MMA8452Q accel;

//ultrasonic range finder variables
const int trigPin = 13;
const int echoPin = 12;
double duration = 0;
double distance = 0;

//flex sensor variables
int flexPin = A1;
int flex = 0;

//potentiometer and system state variables
int potPin = A0;
int state = 0;


/*
 * Initialize the accelerometer
 * Configure the ultrasonic range finder pins
 * Initialize the Serial output
 */
void setup() {
  accel.init();
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
}

/*
 * Main Loop
 * Based on the state of the potentiometer,
 *    read and print the sensor values
 */
void loop() {
  checkState();
  switch(state) {
    case 0:
      accel.read();
      printAccel();
      break;
    case 1:
      findRange_filtered(); 
      printRange();
      break;
    case 2:
      flex = analogRead(flexPin);
      printFlex();
      break;
  }
}

/*
 * Performs median filter over 10 samples of range finder.
 */
void findRange_filtered() {
  //take readings
  int durations[WINDOWSIZE] = {0};
  for(int i = 0; i < WINDOWSIZE; i++) {
    digitalWrite(trigPin, HIGH);
    delay(1);
    digitalWrite(trigPin, LOW);
    durations[i] = pulseIn(echoPin, HIGH);
    delay(60);
  }

  //simple sort
  for(int i = WINDOWSIZE; i > 0; i--){
    for (int j = 1; j < i; j++) {
      if(durations[j-1] > durations[j]) {
        int swap = durations[j-1];
        durations[j-1] = durations[j];
        durations[j] = swap;
      }
    }
    Serial.println(durations[i-1]);
  }

  int duration = durations[WINDOWSIZE/2];
  distance = (duration/2) / 29.1;
}

/*
 * Checks the value of the potentiometer reading an updates the state variable accordingly.
 */
void checkState() {
  int pot = analogRead(potPin);
  
  //divide 1024 by 3, and give each state a 3rd
  if (pot < 342) { state = 0; }
  else if (pot >= 342 && pot < 684 ) { state = 1; }
  else { state = 2; }
}

/*
 * Prints the formated accelerometer reads to the Serial output
 */
void printAccel() {
  Serial.print("X:");
  Serial.print(accel.cx);
  Serial.print(", Y: ");
  Serial.print(accel.cy);
  Serial.print(", Z: ");
  Serial.println(accel.cz);
}

/*
 * Prints the formated range to the Serial output
 */
void printRange(){
  if (distance < 2.5) {  
    Serial.println("Too Close");
  }
  
  if (distance >= 300){
    Serial.println("Too Far");
  }
  else {
    Serial.print(distance);
    Serial.println("cm");
  }
}

/*
 * Converts and prints the flex sensor state.
 */
void printFlex() {
  //based on playing with the sensor, these values roughly differentiate the sensor states
  if(flex < 600) { Serial.println("UP"); }
  else if (flex >= 600 && flex < 700) { Serial.println("NEUTRAL"); }
  else { Serial.println("DOWN"); }
}
