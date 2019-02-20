#define m1in1 11
#define m1in2 12
#define m2in1 6
#define m2in2 7
#define m3in1 5
#define m3in2 4
#define m4in1 10
#define m4in2 9
#define enableAll 13

typedef void (*op_func)();
op_func operation;

void setup() {
  pinMode(m1in1, OUTPUT);
  pinMode(m1in2, OUTPUT);
  pinMode(m2in1, OUTPUT);
  pinMode(m2in2, OUTPUT);
  pinMode(m3in1, OUTPUT);
  pinMode(m3in2, OUTPUT);
  pinMode(m4in1, OUTPUT);
  pinMode(m4in2, OUTPUT);
  pinMode(m1in1, OUTPUT);

  operation = fullStop;
  Serial.begin(9600);
}

void loop() {
  operation();
}

void allMovementTest()
{
  goForward();
  delay(2000);
  fullStop();
  delay(1000);
  goBackward();
  delay(2000);
  fullStop();
  delay(1000);

  goLeft();
  delay(2000);
  fullStop();
  delay(1000);

  goRight();
  delay(2000);
  fullStop();
  delay(1000);

  goRight();
  delay(2000);
  fullStop();
  delay(1000);


  rotateCCW();
  delay(2000);
  fullStop();
  delay(1000);

  rotateCW();
  delay(2000);
  fullStop();
  delay(1000);
}

void rotateCCW()
{
  digitalWrite(enableAll, HIGH);
  digitalWrite(m1in2, LOW);
  analogWrite(m1in1, 255);
  digitalWrite(m2in2, HIGH);
  analogWrite(m2in1, LOW);
  digitalWrite(m3in2, HIGH);
  analogWrite(m3in1, LOW);
  digitalWrite(m4in2, HIGH);
  analogWrite(m4in1, LOW);
}

void rotateCW()
{
  digitalWrite(enableAll, HIGH);
  digitalWrite(m1in2, HIGH);
  analogWrite(m1in1, 0);
  digitalWrite(m2in2, LOW);
  analogWrite(m2in1, 255);
  digitalWrite(m3in2, LOW);
  analogWrite(m3in1, 255);
  digitalWrite(m4in2, LOW);
  analogWrite(m4in1, 255);
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
void goForward()
{

  digitalWrite(enableAll, HIGH);

  digitalWrite(m3in2, HIGH);
  analogWrite(m3in1, 0);

  digitalWrite(m2in2, LOW);
  analogWrite(m2in1, 255);
}

void goBackward()
{
  digitalWrite(enableAll, HIGH);

  digitalWrite(m3in2, LOW);
  analogWrite(m3in1, 255);

  digitalWrite(m2in2, HIGH);
  analogWrite(m2in1, 0);
}

void goLeft()
{
  digitalWrite(enableAll, HIGH);

  digitalWrite(m4in2, HIGH);
  analogWrite(m4in1, 0);

  digitalWrite(m1in2, HIGH);
  analogWrite(m1in1, 0);
}

void goRight()
{
  digitalWrite(enableAll, HIGH);

  digitalWrite(m4in2, LOW);
  analogWrite(m4in1, 255);

  digitalWrite(m1in2, LOW);
  analogWrite(m1in1, 255);
}

void motorTestProtocol()
{
  digitalWrite(enableAll, HIGH);
  digitalWrite(4, HIGH);
  digitalWrite(5, LOW);
  delay(2000);

  delay(500);
  digitalWrite(enableAll, HIGH);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  delay(500);

  digitalWrite(enableAll, HIGH);
  digitalWrite(4, LOW);
  digitalWrite(5, HIGH);
  delay(2000);

  delay(500);
  digitalWrite(enableAll, HIGH);
  digitalWrite(4, LOW);
  digitalWrite(5, LOW);
  delay(1000);

  digitalWrite(enableAll, HIGH);
  digitalWrite(6, HIGH);
  digitalWrite(7, LOW);
  delay(2000);

  delay(500);
  digitalWrite(enableAll, HIGH);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  delay(500);

  digitalWrite(enableAll, HIGH);
  digitalWrite(6, LOW);
  digitalWrite(7, HIGH);
  delay(2000);

  delay(500);
  digitalWrite(enableAll, HIGH);
  digitalWrite(6, LOW);
  digitalWrite(7, LOW);
  delay(1000);

  digitalWrite(enableAll, HIGH);
  digitalWrite(9, HIGH);
  digitalWrite(10, LOW);
  delay(2000);

  delay(500);
  digitalWrite(enableAll, HIGH);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  delay(500);

  digitalWrite(enableAll, HIGH);
  digitalWrite(9, LOW);
  digitalWrite(10, HIGH);
  delay(2000);

  delay(500);
  digitalWrite(enableAll, HIGH);
  digitalWrite(9, LOW);
  digitalWrite(10, LOW);
  delay(1000);

  digitalWrite(enableAll, HIGH);
  digitalWrite(11, HIGH);
  digitalWrite(12, LOW);
  delay(2000);

  delay(500);
  digitalWrite(enableAll, HIGH);
  digitalWrite(11, LOW);
  digitalWrite(12, LOW);
  delay(500);

  digitalWrite(enableAll, HIGH);
  digitalWrite(11, LOW);
  digitalWrite(12, HIGH);
  delay(2000);

  delay(500);
  digitalWrite(enableAll, HIGH);
  digitalWrite(11, LOW);
  digitalWrite(12, LOW);
  delay(1000);
}

void serialEvent(){
  while(Serial.available()) {
    char inChar = (char)Serial.read();
    switch(inChar) {
      case 'w': operation = goForward;
                break;
      case 's': operation = goBackward;
                break;
      case 'a': operation = goLeft;
                break;
      case 'd': operation = goRight;
                break;
      case 'q': operation = rotateCCW;
                break;
      case 'e': operation = rotateCW;
                break;
      case 'x': operation = fullStop;
                break;
      default: break;
    }
    fullStop();
  }
}

