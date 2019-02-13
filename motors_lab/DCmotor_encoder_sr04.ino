#include <Encoder.h>


//ultrasonic range finder variables
const int trigPin = 13;
const int echoPin = 12;
double duration_sr04 = 0;
double distance = 0;
boolean rangeInitialized = 0;
#define WINDOWSIZE 5
int durations_sr04[WINDOWSIZE] = {0};


//encoder variables
#define a_PINA 2
#define a_PINB 3
int8_t clicks = 0;
char id = 0;

Encoder DC1_enc = Encoder(a_PINA, a_PINB);

//Motor variables
#define DC1_in1 6 //PWM
#define DC1_in2 7 //directional pin


//Motor control variables
int currentAngle = 0; //read from motor state
int desiredAngle = 0; //input from various sources, in this case sr04 data
bool rotationDirection_DC1 = true; //true default forward

int desiredVelocity = 0;
int currentVelocity = 0;

void setup() {
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  Serial.begin(9600);
  Serial.println("Initializing program ");
}

void loop() {
  //findRange_filtered(); 
  //printRange();

  readEncoder();

  //Serial.print("Serial output ");
}

/*
 * Performs median filter over 10 samples of range finder.
 */


void initializeRange(){
  for(int i = 0; i < WINDOWSIZE; i++) {
    digitalWrite(trigPin, HIGH);
    delay(1);
    digitalWrite(trigPin, LOW);
    durations_sr04[i] = pulseIn(echoPin, HIGH);
    delay(60);
  }
}

void findRange_filtered() {
  //take readings
  

  if(rangeInitialized = false)
  {
    initializeRange();
    rangeInitialized = true;
  }

  for(int i = 0; i < WINDOWSIZE-1; i++) { //pushing the values back
    durations_sr04[i] = durations_sr04[i+1];
  }

  
  
  digitalWrite(trigPin, HIGH); //take new sample
  delay(1);
  digitalWrite(trigPin, LOW);
  durations_sr04[WINDOWSIZE-1] = pulseIn(echoPin, HIGH);
  delay(60);

  
  //weighted average filter weighted towards most recent value
  duration_sr04 = 0;
  for(int i = 0; i < WINDOWSIZE-1; i++) { //pushing the values back
    duration_sr04 += durations_sr04[WINDOWSIZE-1-i]/pow(2,i+1);
  }
  duration_sr04 += durations_sr04[WINDOWSIZE-1]/pow(2,WINDOWSIZE-1);

  int duration_sr04 = durations_sr04[WINDOWSIZE/2];
  distance = (duration_sr04/2) / 29.1;
}


void printRange(){
    Serial.print(distance);
    Serial.println("cm");
}

long oldPosition = -999;

void readEncoder(){

    long newPosition = DC1_enc.read();

  if (newPosition != oldPosition) {

    oldPosition = newPosition;

    Serial.println(newPosition);

  }
 // Serial.println(newPosition);
}

void motorProtocol_1(){ //angle control based on sr04 reading
  
}

void motorProtocol_2(){ //velocity control based on sr04 reading
  
}

void motorProtocol_3(){ //Hard brake using sr04 as a proxy sensor
  
}

void motorAnglePID() //Uses desired angle input from other source and current angle reading from encoder to run some PD 
{

  int error = desiredAngle - currentAngle;
  int kd, kp;

  kd = 255/180;

  kp = 0;
  
}



