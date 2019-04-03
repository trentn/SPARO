#include <Encoder.h>

#define m1 1
#define m2 2
#define m3 3
#define m4 4

#define CPR1 8400
#define CPR2 8400
#define CPR3 8400
#define CPR4 8400

#define m1in1 4
#define m1in2 24

#define m2in1 5
#define m2in2 25

#define m3in1 6
#define m3in2 26

#define m4in1 7
#define m4in2 27

#define enableAll 13

#define enc1trigA 2
#define enc2trigA 3
#define enc3trigA 18
#define enc4trigA 19

#define enc1trigB 22
#define enc2trigB 23
#define enc3trigB 38
#define enc4trigB 39

Encoder m1_enc = Encoder(enc1trigA, enc1trigB);
Encoder m2_enc = Encoder(enc2trigA, enc2trigB);
Encoder m3_enc = Encoder(enc3trigA, enc3trigB);
Encoder m4_enc = Encoder(enc4trigA, enc4trigB);

double kp[4] = {255.0/600.0, 255/600.0, 255/600.0, 255/600.0};
double kd[4] = {0, 0, 0, 0};

double currentPWM[4];
double send_rate;
volatile double desiredSpeed[4] = {0}; //in RPM

double states[4][3][3]; //[Motor #][Time Step][Absolute Enc Clicks, Velocity (rpm), Time Since Startup (s)]

double error[4][2]; //[Motor #][Time Step]

double last_send_time = 0;

bool initialized = false;
int s_index = 0;
String motor1string;
String motor2string;
String motor3string;
String motor4string;
String* RPM_strings[4] = {&motor1string, &motor2string, &motor3string, &motor4string};
String initialize_code;
String send_rate_string; 
String* initialize_string[2] = {&initialize_code, &send_rate_string};
bool stringComplete = false;  // whether the string is complete

void setup() {
  Serial.flush();
  Serial.end();
  initialized = false;
  s_index = 0;
  stringComplete = false;
  last_send_time = 0;
  send_rate = 0;
  desiredSpeed[0] = 0;
  desiredSpeed[1] = 0;
  desiredSpeed[2] = 0;
  desiredSpeed[3] = 0;
  
  for(int i = 0;i<4;i++){
    for(int j = 0;j<3;j++){
      for(int k = 0;k<3;k++){
        states[i][j][k] = 0;
      }
    }
    desiredSpeed[i]=0;
    currentPWM[i] = 0;
    error[i][0]=0;
    error[i][1]=0;
  }
  motor1string.reserve(50);
  motor2string.reserve(50);
  motor3string.reserve(50);
  motor4string.reserve(50);
  initialize_code.reserve(50);
  send_rate_string.reserve(5);

  initialize_code = "";
  send_rate_string = "";
  
  pinMode(m1in1, OUTPUT);
  pinMode(m1in2, OUTPUT);
  pinMode(m2in1, OUTPUT);
  pinMode(m2in2, OUTPUT);
  pinMode(m3in1, OUTPUT);
  pinMode(m3in2, OUTPUT);
  pinMode(m4in1, OUTPUT);
  pinMode(m4in2, OUTPUT);
  pinMode(m1in1, OUTPUT);

  Serial.begin(9600);
  
  initializeStates();
  updateStates();
  delay(100);
  updateStates();
  delay(100);
  updateStates();
  delay(100);
  //Serial.println("Finished setup");

  Serial.flush();
}



void loop() {
  if(!initialized && stringComplete)
  {
    //Serial.println("Waiting for Rpi");
    waitForRPi();
  }
  else if(initialized)
  {
  if (stringComplete) {
    updateSpeeds();
    stringComplete = false;
  }
  controlLoopAll();
  //Serial.println(currentPWM[0]);
  if(abs(last_send_time-micros()/1000000.0) > send_rate){
    sendToRPi();
    last_send_time = micros()/1000000.0;
  }
  delay(10);
  }
  //allMotorSpeeds();
}

void waitForRPi()
{
     if (stringComplete) {
        //Serial.println("String recieved");
        if(initialize_code == "Are you ready kids?")
        {
          send_rate = send_rate_string.toDouble();
          initialized = true;
          Serial.println("Aye aye captain!");
          Serial.flush();
          delay(2000);
        }
        else
        {
          Serial.println("Authentication failed");
          Serial.flush();
          initialize_code = "";
          send_rate_string = "";
        }
        delay(5);
        stringComplete = false;
    }
}

void sendToRPi()
{
    Serial.print((2*states[0][0][1]+states[0][1][1]+states[0][2][1])/4);
    Serial.print(",");
    Serial.print((2*states[1][0][1]+states[1][1][1]+states[1][2][1])/4);
    Serial.print(",");
    Serial.print((2*states[2][0][1]+states[2][1][1]+states[2][2][1])/4);
    Serial.print(",");
    Serial.print((2*states[3][0][1]+states[3][1][1]+states[3][2][1])/4);
    Serial.print(",");
    Serial.println(states[0][0][2]);
}

void controlLoopAll()
{
  double error[4][2];
  updateStates();

  for (int i = 0; i < 4; i++)
  {
    error[i][1] = error[i][0];
    error[i][0] = desiredSpeed[i] - states[i][0][1];
    currentPWM[i] = currentPWM[i] - (error[i][0] * kp[i] + (error[i][0] - error[i][1]) * kd[i]);
    //Serial.println(currentPWM[i]);
  }
  updatePWM();
}

void updatePWM()
{
  for (int i = 0; i < 4; i++)
  {
    if (currentPWM[i] < -255)
    {
      currentPWM[i] = -254;
      //Serial.print("Warning:: Motor ");
      //Serial.print(i+1);
      //Serial.println(" neg saturating!");
    }
    if (currentPWM[i] > 255)
    {
      currentPWM[i] = 254;
     // Serial.print("Warning:: Motor ");
     // Serial.print(i+1);
      //Serial.println(" pos saturating!");
    }
  }

  //--------------------------------------------- motor1 set

  if (currentPWM[0] < 0)
  {
    digitalWrite(enableAll, HIGH);
    digitalWrite(m1in2, HIGH);
    analogWrite(m1in1, 255 + currentPWM[0]);
  }
  else if (currentPWM[0] > 0)
  {
    digitalWrite(enableAll, HIGH);
    digitalWrite(m1in2, LOW);
    analogWrite(m1in1, currentPWM[0]);
  }
  else
  {
    digitalWrite(enableAll, LOW);
    digitalWrite(m1in2, LOW);
    analogWrite(m1in1, LOW);
  }


  //----------------------------------------------- motor2 set
  if (currentPWM[1] < 0)
  {
    digitalWrite(enableAll, HIGH);
    digitalWrite(m2in2, HIGH);
    analogWrite(m2in1, 255 + currentPWM[1]);
  }
  else if (currentPWM[1] > 0)
  {
    digitalWrite(enableAll, HIGH);
    digitalWrite(m2in2, LOW);
    analogWrite(m2in1, currentPWM[1]);
  }
  else
  {
    digitalWrite(enableAll, LOW);
    digitalWrite(m2in2, LOW);
    analogWrite(m2in1, LOW);
  }
  //------------------------------------------------ motor3 set
  if (currentPWM[2] < 0)
  {
    digitalWrite(enableAll, HIGH);
    digitalWrite(m3in2, HIGH);
    analogWrite(m3in1, 255 + currentPWM[2]);
  }
  else if (currentPWM[2] > 0)
  {
    digitalWrite(enableAll, HIGH);
    digitalWrite(m3in2, LOW);
    analogWrite(m3in1, currentPWM[2]);
  }
  else
  {
    digitalWrite(enableAll, LOW);
    digitalWrite(m3in2, LOW);
    analogWrite(m3in1, LOW);
  }
  //------------------------------------------------- motor4 set
  if (currentPWM[3] < 0)
  {
    digitalWrite(enableAll, HIGH);
    digitalWrite(m4in2, HIGH);
    analogWrite(m4in1, 255 + currentPWM[3]);
  }
  else if (currentPWM[3] > 0)
  {
    digitalWrite(enableAll, HIGH);
    digitalWrite(m4in2, LOW);
    analogWrite(m4in1, currentPWM[3]);
  }
  else
  {
    digitalWrite(enableAll, LOW);
    digitalWrite(m4in2, LOW);
    analogWrite(m4in1, LOW);
  }

  //Serial.println(currentPWM[i]);
}

void allMotorSpeeds()
{
  Serial.print(states[0][0][1]);
  Serial.print(" --- ");
  Serial.print(states[1][0][1]);
  Serial.print(" --- ");
  Serial.print(states[2][0][1]);
  Serial.print(" --- ");
  Serial.println(states[3][0][1]);
  Serial.println();
}

void initializeStates()
{
  for (int i = 0; i < 4; i++)
  {
    desiredSpeed[i] = 0.0;
    currentPWM[i] = 0.0;
    for (int j = 2; j >= 0; j--)
    {
      for (int k = 0; k < 2; k++)
      {

        states[i][j][k] = 0;

      }

      states[i][j][2] = ((millis() + j) / 1000.0); //keeps from dividing by zero
    }
  }
}

void updateStates()
{
  //unsigned long startTime = micros();
  for (int j = 2; j >= 1; j--) //pushback loop
  {
    for (int i = 0; i < 4; i++)
    {
      for (int k = 0; k < 3; k++)
      {
        states[i][j][k] = states[i][j - 1][k];
      }
    }
  }

  states[0][0][0] = m1_enc.read(); //as close to simultaneous as possible but checks times in case its not
  states[0][0][2] = millis() / 1000.0;
  states[1][0][0] = m2_enc.read();
  states[1][0][2] = millis() / 1000.0;
  states[2][0][0] = m3_enc.read();
  states[2][0][2] = millis() / 1000.0;
  states[3][0][0] = m4_enc.read();
  states[3][0][2] = millis() / 1000.0;


  states[0][0][1] = (states[0][0][0] - states[0][1][0]) / (states[0][0][2] - states[0][1][2]) * 60 / CPR1; //updating velocities for all motors
  states[1][0][1] = (states[1][0][0] - states[1][1][0]) / (states[1][0][2] - states[1][1][2]) * 60 / CPR2;
  states[2][0][1] = (states[2][0][0] - states[2][1][0]) / (states[2][0][2] - states[2][1][2]) * 60 / CPR3;
  states[3][0][1] = (states[3][0][0] - states[3][1][0]) / (states[3][0][2] - states[3][1][2]) * 60 / CPR4;

  //Serial.println(states[0][1][1]);
  //Serial.println(micros() - startTime); //checks time it takes to run this component ---> approx 300 micros with no interrupts --->approx 460~70 micros with all motors full speed and no communications
}

void printAllEnc()
{
  Serial.print(m1_enc.read());
  Serial.print("    ");
  Serial.print(m2_enc.read());
  Serial.print("    ");
  Serial.print(m3_enc.read());
  Serial.print("    ");
  Serial.println(m4_enc.read());
  Serial.println();
}

void fullStop()
{
  digitalWrite(enableAll, LOW);
  digitalWrite(m1in2, LOW);
  analogWrite(m1in1, LOW);
  digitalWrite(m2in2, LOW);
  analogWrite(m2in1, LOW);
  digitalWrite(m3in2, LOW);
  analogWrite(m3in1, LOW);
  digitalWrite(m4in2, LOW);
  analogWrite(m4in1, LOW);
}


void updateSpeeds(){
  desiredSpeed[0] = motor1string.toDouble();  
  motor1string = "";
  
  desiredSpeed[1] = motor2string.toDouble();
  motor2string = "";
  
  desiredSpeed[2] = motor3string.toDouble();
  motor3string = "";
  
  desiredSpeed[3] = motor4string.toDouble();
  motor4string = "";

  if(desiredSpeed[0]==-999)
  {
    setup();
  }
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  //Serial.println("Entered serial event");
  while (Serial.available()) {
    // get the new byte:
    //Serial.println("Reading char");
    char inChar = (char)Serial.read();
    if (inChar == ',' || inChar == '\n') {
      if (inChar == '\n') {
        stringComplete = true;
        s_index = 0;
        //Serial.println("newline accepted");
        return;
      }
      s_index++;
      continue;
    }
  if(!initialized){
    //Serial.println("Initialize string");
    *initialize_string[s_index] += inChar;
  }
  else if(initialized){
    //Serial.println("Motor string");
    *RPM_strings[s_index] += inChar;
    
  }
  }
}
