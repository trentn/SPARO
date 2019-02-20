/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 http://www.arduino.cc/en/Tutorial/Sweep
*/

#include <Servo.h>

Servo myservo;  // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position

void setup() {
  myservo.attach(11);  // attaches the servo on pin 9 to the servo object
}

void loop() {
  for (pos =1500; pos <= 1875; pos += 1) 
  { 
    myservo.writeMicroseconds(pos);             
    delay(1);
  }
  
  for (pos = 1875; pos >= 1500; pos -= 1) 
  { 
    myservo.writeMicroseconds(pos);              
    delay(1);  
    //myservo.writeMicroseconds(1200);
    //delay(1);
    // waits 15ms for the servo to reach the position
  }
  delay(5000);
  for (pos = 1500; pos<=2400; pos++)
  {
    myservo.writeMicroseconds(pos);
    delay(1);
  }
  for (pos = 2400; pos>=1500; pos--)
  {
    myservo.writeMicroseconds(pos);
    delay(1);  
  }
  delay(5000);
  
}
