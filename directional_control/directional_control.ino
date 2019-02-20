typedef void (*op_func)();
op_func operation;

void stop(){Serial.println("STOP");}
void forward(){Serial.println("FORWARD");}
void reverse(){Serial.println("REVERSE");}
void left(){Serial.println("LEFT");}
void right(){Serial.println("RIGHT");}
void spin_left(){Serial.println("SPIN LEFT");}
void spin_right(){Serial.println("SPIN RIGHT");}

void setup() {
  Serial.begin(9600);
  operation = stop;
}

void loop() {
  operation();
}

void serialEvent(){
  while(Serial.available()) {
    char inChar = (char)Serial.read();
    switch(inChar) {
      case 'w': operation = forward;
                break;
      case 's': operation = reverse;
                break;
      case 'a': operation = left;
                break;
      case 'd': operation = right;
                break;
      case 'q': operation = spin_left;
                break;
      case 'e': operation = spin_right;
                break;
      case 'x': operation = stop;
                break;
      default: break;
    }
  }
}
