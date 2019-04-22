#include <Adafruit_VL53L0X.h>
#include<Stepper.h>

#define TOF1 8
#define TOF2 9
#define TOF3 10
#define TOF4 11

#define STEPPER1 2
#define STEPPER2 3
#define STEPPER3 4
#define STEPPER4 5

String input_string;
bool stringComplete = false;

bool initialized = false;
int s_index = 0;
String initialize_code;
String send_rate_string; 
String* initialize_string[2] = {&initialize_code, &send_rate_string};

const int stepsPerRevolution = 400;
Stepper end_effector(stepsPerRevolution, STEPPER1, STEPPER2, STEPPER3, STEPPER4);
double degree_rotation = 0;
int number_steps = 0;

Adafruit_VL53L0X lox1 = Adafruit_VL53L0X();
Adafruit_VL53L0X lox2 = Adafruit_VL53L0X();
Adafruit_VL53L0X lox3 = Adafruit_VL53L0X();
Adafruit_VL53L0X lox4 = Adafruit_VL53L0X();

#define ROLL_AVG 3

VL53L0X_RangingMeasurementData_t measure1;
VL53L0X_RangingMeasurementData_t measure2;
VL53L0X_RangingMeasurementData_t measure3;
VL53L0X_RangingMeasurementData_t measure4;

int index = 0;
int temp_measurements[4][ROLL_AVG] = {0};
int measurements[4] = {0};

void setup() {
  initialized = false;
  stringComplete = false;
  
  initialize_code.reserve(50);
  send_rate_string.reserve(5);
  input_string.reserve(50);

  initialize_code = "";
  send_rate_string = "";
  input_string = "";

  double degree_rotation = 0;
  int number_steps = 0;
  
  
  Serial.begin(9600);
  while (! Serial) {
    delay(1);
  }

  //Serial.println("Starting initialization");
  pinMode(TOF1, OUTPUT);
  pinMode(TOF2, OUTPUT);
  pinMode(TOF3, OUTPUT);
  pinMode(TOF4, OUTPUT);

  digitalWrite(TOF1, LOW);
  digitalWrite(TOF2, LOW);
  digitalWrite(TOF3, LOW);
  digitalWrite(TOF4, LOW);
  delay(10);

  digitalWrite(TOF1, HIGH);
  if (!lox1.begin(0x31)) {
    //Serial.println("Failed to boot VL53L0X");
    while(1);
  }

  digitalWrite(TOF2, HIGH);
  if (!lox2.begin(0x32)) {
    //Serial.println("Failed to boot VL53L0X");
    while(1);
  }
  
  digitalWrite(TOF3, HIGH);
  if (!lox3.begin(0x33)) {
    //Serial.println("Failed to boot VL53L0X");
    while(1);
  }
  
  digitalWrite(TOF4, HIGH);
  if (!lox4.begin(0x34)) {
    //Serial.println("Failed to boot VL53L0X");
    while(1);
  }
  //Serial.println("Initialized");
}

void loop() {
  if(!initialized && stringComplete) {
    waitForRPi();
    initialize_code = "";
  }
  
  else if(initialized) {
    if (stringComplete) {
      turnStepper();
      stringComplete = false;
    }
    takeMeasurements();
    averageMeasurements();
    sendMeasurements();
  }

  
}

void test() {
  Serial.println("loop");
}

void takeMeasurements() {
  lox1.rangingTest(&measure1, false); // pass in 'true' to get debug data printout!
  lox2.rangingTest(&measure2, false);
  lox3.rangingTest(&measure3, false);
  lox4.rangingTest(&measure4, false);

  if (measure1.RangeStatus != 4) {  // phase failures have incorrect data
    temp_measurements[0][index] = measure1.RangeMilliMeter;
  } else {
    temp_measurements[0][index] = -999;
  }

  if (measure2.RangeStatus != 4) {  // phase failures have incorrect data
    temp_measurements[1][index] = measure2.RangeMilliMeter;
  } else {
    temp_measurements[1][index] = -999;
  }
  
  if (measure3.RangeStatus != 4) {  // phase failures have incorrect data
    temp_measurements[2][index] = measure3.RangeMilliMeter;
  } else {
    temp_measurements[2][index] = -999;
  }

  if (measure4.RangeStatus != 4) {  // phase failures have incorrect data
    temp_measurements[3][index] = measure4.RangeMilliMeter;
  } else {
    temp_measurements[3][index] = -999;
  }

  index = (index + 1)%ROLL_AVG;
}

void averageMeasurements() {
  for(int lox = 0; lox < 4; lox++){
    int sum = 0;
    for(int i = 0; i < ROLL_AVG; i++) {
      sum += temp_measurements[lox][i];
    }
    measurements[lox] = sum/ROLL_AVG;
  }
}

void sendMeasurements() {
  for(int lox = 0; lox < 4; lox++) {
    Serial.print(measurements[lox]);
    Serial.print(",");
  }
  Serial.println(millis()/1000.0);
}

void turnStepper() {
  degree_rotation = input_string.toDouble();
  if(degree_rotation == -999.0) {
    setup();
    return;
  }
  
  input_string = "";
  number_steps = (int) (degree_rotation / 360.0 * stepsPerRevolution);
  for (int i = 1; i <= abs(number_steps); i++)
  {
    if (number_steps > 0)
    {
      end_effector.step(1);
    }
    else
    {
      end_effector.step(-1);
    }
    i++;
    delay(10);
  }
}

void waitForRPi()
{
     if (stringComplete) {
        if(initialize_code == "Are you ready kids?") {
          initialized = true;
          Serial.println("stepper/ToF!");
          Serial.flush();
          delay(2000);
        }
        else {
          Serial.println("Authentication failed");
          Serial.flush();
        }
        stringComplete = false;
    }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n' || inChar == ',') {
      if (inChar == '\n') {
        stringComplete = true;
        s_index = 0;
        return;
      }
      s_index++;
      continue;
    }
    if(!initialized){
      *initialize_string[s_index] += inChar;
    }
    else if(initialized){
      input_string += inChar; 
    }
  }
}
