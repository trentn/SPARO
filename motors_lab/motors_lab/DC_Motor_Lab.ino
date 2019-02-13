#include <Encoder.h>

//------------------------------------------------------------------------------------------------------------

//ultrasonic range finder variables
const int trigPin = 13;
const int echoPin = 12;
double duration_sr04 = 0;
double distance = 0;
boolean rangeInitialized = 0;
#define WINDOWSIZE 6 //must be even
int durations_sr04[WINDOWSIZE] = {0};
int waitTime = 70;

//------------------------------------------------------------------------------------------------------------

//encoder variables
#define a_PINA 2
#define a_PINB 3
double ticksPerRotation = 1925.0;
long encPosition[2] = {0,0};
double encSpeed[2] = {0, 0};
double vel_error[2] = {0, 0};
Encoder DC1_enc = Encoder(a_PINA, a_PINB);

//------------------------------------------------------------------------------------------------------------

//Motor variables
#define DC1_in1 6 //PWM
#define DC1_in2 7 //directional pin
#define DC1_en  8 // enable  pin
double currentPwm = 0;

//------------------------------------------------------------------------------------------------------------

void setup() {
  
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  
  pinMode(DC1_in1, OUTPUT);
  pinMode(DC1_in2, OUTPUT);
  pinMode(DC1_en, OUTPUT);

  Serial.begin(9600);
}

//------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------

void loop() {
  
   speed_Control(360);
   Serial.println(encSpeed[0]);
   
}

//------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------

void readSpeed()
{
  readEnc();
  delay(20);
  readEnc();
  double stepinc = (20)/1000.0;
  encSpeed[1] = encSpeed[0];
  encSpeed[0] = (encPosition[0]-encPosition[1])/stepinc*360/ticksPerRotation;
}

//------------------------------------------------------------------------------------------------------------

void speed_PID(double vel_error[2],double timestep)
{
  double kd, kp;
 
  kp = 255.0/1850.0;
  kd = 7.5;
 
  currentPwm = currentPwm+( kp*vel_error[0] + (vel_error[0]-vel_error[1])/timestep * kd);

  if(currentPwm > 255)
  {
    currentPwm = 255;
  }
  else if(currentPwm < -255)
  {
    currentPwm = -255;
  }
}

//------------------------------------------------------------------------------------------------------------

void speed_Control(double desSpeed)
{
    
  digitalWrite(DC1_en, HIGH);

  
  vel_error[1] = vel_error[0];
  readSpeed();
  vel_error[0] = desSpeed - encSpeed[0];
  
  speed_PID(vel_error,20);
  if(currentPwm < 0.0) //Directionality check
    {
      digitalWrite(DC1_in2, HIGH);
      analogWrite(DC1_in1, 255+currentPwm);
    }
    else
    {
      digitalWrite(DC1_in2, LOW);
      analogWrite(DC1_in1, currentPwm);
    }
}

//------------------------------------------------------------------------------------------------------------

void sr04_Angle_Control()
{
  double sr04delay = .06;
  findRange_filtered();

  readEnc();
  double currentAngle = getAngle();
  double desAngle = (distance-5)/30.0*180.0;

  if(desAngle > 720){
    desAngle = 720;
  }

  //Serial.println(desAngle);
  //Serial.println(currentAngle);
  
  double error[2];
  error[1] = desAngle-currentAngle;
  findRange_filtered();

  readEnc();
  currentAngle = getAngle();
//  error[0] = desAngle-currentAngle;
  error[0] = error[1];
  
  //Serial.println(error[0]);
  
  double pwm = motorAnglePID_sr04(error, sr04delay);

  //Serial.println(pwm);
  
  digitalWrite(DC1_en, HIGH);

  if(pwm < 0.0) //Directionality check
    {
      digitalWrite(DC1_in2, HIGH);
      analogWrite(DC1_in1, 255+pwm);
    }
    else
    {
      digitalWrite(DC1_in2, LOW);
      analogWrite(DC1_in1, pwm);
    }
}

//------------------------------------------------------------------------------------------------------------

double motorAnglePID_sr04(double error[2],double timestep) //Uses desired angle input from other source and current angle reading from encoder to run some PD 
{
  
  double kd, kp;
 
  kp = 255.0/180*.3;
  kd = .023;
  int undersat = 20; //turn on PWM parameter
  
  double pwm = kp*error[1] + (error[1]-error[0])/timestep * kd;
//  Serial.print("pwm ");
//  Serial.println(pwm);
  if(pwm > 255) //oversaturation and underactuation compensation
  {
    pwm = 255.0;
    
  }
  else if(pwm < -255)
  {
    pwm = -255.0;
    
  }
  
  if(pwm < undersat && pwm > 0)
  {
    pwm = undersat;
    
  }
  
  if(pwm > -undersat && pwm < 0)
  {
    pwm = -undersat;
      
  }

  return pwm; //returns negative for sign agreement
}

//------------------------------------------------------------------------------------------------------------

void motorFullForward(int duration)
{
  Serial.println("Motor Full Forward Start");
  digitalWrite(DC1_in1, HIGH);
  digitalWrite(DC1_in2, LOW);
  digitalWrite(DC1_en, HIGH);

  delay(duration);
  digitalWrite(DC1_in1, LOW);

  Serial.println("Motor Full Forward End");
}

//------------------------------------------------------------------------------------------------------------

void motorFullBackward(int duration)
{
  Serial.println("Motor Full Backward Start");
  digitalWrite(DC1_in1, LOW);
  digitalWrite(DC1_in2, HIGH);
  digitalWrite(DC1_en,  HIGH);

  delay(duration);
  Serial.println("Motor Full Backward End");
  digitalWrite(DC1_en,LOW); 
}

//------------------------------------------------------------------------------------------------------------

void pwmRun(int pwm, int duration){
  digitalWrite(DC1_en, HIGH);
  digitalWrite(DC1_in2, LOW);
  analogWrite(DC1_in1, pwm);
  delay(duration);
}
//------------------------------------------------------------------------------------------------------------

void pwmRunEncoder(int pwm,int encoder_cap)
{
  Serial.println("Motor Encoder Read Start");
  digitalWrite(DC1_en, HIGH);
  digitalWrite(DC1_in2, LOW);
  analogWrite(DC1_in1, pwm);

  while( abs(encPosition[0]) < encoder_cap)
  {
    Serial.println(encPosition[0]);
  }

  digitalWrite(DC1_in1, LOW);
  Serial.println("Motor Encoder Read End");
}

//------------------------------------------------------------------------------------------------------------

void motorRamp(int tdelay){ //test function to ramp motor up over a period of time
  Serial.println("Motor Ramp Start");
  digitalWrite(DC1_en, HIGH);
  digitalWrite(DC1_in2, LOW);
  digitalWrite(DC1_in1, HIGH);
  for(int i = 25; i <= 255.0; i++)
  {
    analogWrite(DC1_in1, i);
    Serial.println(i);
    readSpeed();
    Serial.println(encSpeed[0]);
    delay(tdelay);
  }
  digitalWrite(DC1_in1,LOW);
  Serial.println("Motor Ramp End");
}

//------------------------------------------------------------------------------------------------------------

void initializeRange(){
  for(int i = 0; i < WINDOWSIZE; i++) {
    digitalWrite(trigPin, HIGH);
    delay(1);
    digitalWrite(trigPin, LOW);
    durations_sr04[i] = pulseIn(echoPin, HIGH);
    delay(waitTime); //Investigate shortening
  }
}

//------------------------------------------------------------------------------------------------------------

void findRange_filtered() {  
  int temp[WINDOWSIZE];
  if(rangeInitialized = false)
  {
    initializeRange();
    rangeInitialized = true;
  }

  for(int i = 0; i < WINDOWSIZE-1; i++) { //pushing the values back
    durations_sr04[i] = durations_sr04[i+1];
    temp[i] = durations_sr04[i];
  }
  
  digitalWrite(trigPin, HIGH); //take new sample
  delay(1);
  digitalWrite(trigPin, LOW);
  durations_sr04[WINDOWSIZE-1] = pulseIn(echoPin, HIGH);
  temp[WINDOWSIZE-1] = durations_sr04[WINDOWSIZE-1];
//  Serial.println(durations_sr04[WINDOWSIZE-1]);
  delay(waitTime); //##investigate decreasing
  
  //weighted average filter weighted towards most recent value
  for(int i = WINDOWSIZE; i > 0; i--){
    for (int j = 1; j < i; j++) {
      if(temp[j-1] > temp[j]) {
        int swap = temp[j-1];
        temp[j-1] = temp[j];
        temp[j] = swap;
      }
    }

  int duration_sr04 = temp[WINDOWSIZE/2];
  distance = (duration_sr04/2) / 29.1;
}
}

//------------------------------------------------------------------------------------------------------------

void printRange(){
    Serial.print(distance);
    Serial.println(" cm");
}

//------------------------------------------------------------------------------------------------------------

void setAngle(double angle){ //angle control

  double timeStep = .001; //changes the control delay
  double error[2];

  readEnc();
  error[1] = angle - getAngle(); //REPLACE
  error[0] = error[1];
  int pwm = 0;
  
  while(abs(error[1]-error[0])/timeStep > 1 || abs(error[1]+error[0])/2 > .5)
  {
    digitalWrite(DC1_en, HIGH);

    readEnc();
    error[0] = error[1];
    error[1] = angle - getAngle();
    Serial.println(error[1]); //optional error tracking
    pwm = (int)motorAnglePID(error, timeStep);

    if(pwm < 0.0) //Directionality check
    {
      digitalWrite(DC1_in2, HIGH);
      analogWrite(DC1_in1, 255+pwm);
    }
    else
    {
      digitalWrite(DC1_in2, LOW);
      analogWrite(DC1_in1, pwm);
    }
    delay(timeStep*1000.0);
  }
  digitalWrite(DC1_in2, LOW);
  digitalWrite(DC1_in1,LOW);
  digitalWrite(DC1_en,LOW);
  
//  Serial.print("Ending angle control protocol final error approx ");
//  Serial.print(error[1]);
//  Serial.println(" degrees"); //reporting final error
//  
}

//------------------------------------------------------------------------------------------------------------

void motorProtocol_2(){ //velocity control based on sr04 reading
  
}

//------------------------------------------------------------------------------------------------------------

double motorAnglePID(double error[2],double timestep) //Uses desired angle input from other source and current angle reading from encoder to run some PD 
{
  
  double kd, kp;
 
  kp = 255.0/180*2;
  kd = .023;
  int undersat = 30; //turn on PWM parameter
  
  double pwm = kp*error[1] + (error[1]-error[0])/timestep * kd;
//  Serial.print("pwm ");
//  Serial.println(pwm);
  if(pwm > 255) //oversaturation and underactuation compensation
  {
    pwm = 255.0;
    
  }
  else if(pwm < -255)
  {
    pwm = -255.0;
    
  }
  
  if(pwm < undersat && pwm > 0)
  {
    pwm = undersat;
    
  }
  
  if(pwm > -undersat && pwm < 0)
  {
    pwm = -undersat;
      
  }

  return pwm; //returns negative for sign agreement
}

void readEnc(){

    encPosition[1] = encPosition[0];
    encPosition[0] = DC1_enc.read();
//    Serial.print("encPosition[0] ");
//    Serial.println(encPosition[0]);
}

double getAngle(){
  return encPosition[0]/ticksPerRotation*360.00;
}


//------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------
//------------------------------------------------------------------------------------------------------------
