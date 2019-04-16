#include <Adafruit_VL53L0X.h>

#define TOF1 8
#define TOF2 9
#define TOF3 10
#define TOF4 11

Adafruit_VL53L0X lox1 = Adafruit_VL53L0X();
Adafruit_VL53L0X lox2 = Adafruit_VL53L0X();
Adafruit_VL53L0X lox3 = Adafruit_VL53L0X();
Adafruit_VL53L0X lox4 = Adafruit_VL53L0X();

void setup() {
  Serial.begin(115200);
  while (! Serial) {
    delay(1);
  }
  
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
    Serial.println(F("Failed to boot VL53L0X"));
    while(1);
  }

  digitalWrite(TOF2, HIGH);
  if (!lox2.begin(0x32)) {
    Serial.println(F("Failed to boot VL53L0X"));
    while(1);
  }
  
  digitalWrite(TOF3, HIGH);
  if (!lox3.begin(0x33)) {
    Serial.println(F("Failed to boot VL53L0X"));
    while(1);
  }
  
  digitalWrite(TOF4, HIGH);
  if (!lox4.begin(0x34)) {
    Serial.println(F("Failed to boot VL53L0X"));
    while(1);
  }

}

void loop() {
  VL53L0X_RangingMeasurementData_t measure1;
  VL53L0X_RangingMeasurementData_t measure2;
  VL53L0X_RangingMeasurementData_t measure3;
  VL53L0X_RangingMeasurementData_t measure4;
    
  lox1.rangingTest(&measure1, false); // pass in 'true' to get debug data printout!
  lox2.rangingTest(&measure2, false);
  lox3.rangingTest(&measure3, false);
  lox4.rangingTest(&measure4, false);

  //Print 1
  if (measure1.RangeStatus != 4) {  // phase failures have incorrect data
    Serial.print(measure1.RangeMilliMeter);
  } else {
    Serial.print(" out of range ");
  }
  Serial.print(","); 


  //Print 2
  if (measure2.RangeStatus != 4) {  // phase failures have incorrect data
    Serial.print(measure2.RangeMilliMeter);
  } else {
    Serial.print(" out of range ");
  }
  Serial.print(","); 


  //Print 3
  if (measure3.RangeStatus != 4) {  // phase failures have incorrect data
    Serial.print(measure3.RangeMilliMeter);
  } else {
    Serial.print(" out of range ");
  }
  Serial.print(","); 

  //Print 4
  if (measure4.RangeStatus != 4) {  // phase failures have incorrect data
    Serial.println(measure4.RangeMilliMeter);
  } else {
    Serial.println(" out of range ");
  }
  
  delay(100);
}
