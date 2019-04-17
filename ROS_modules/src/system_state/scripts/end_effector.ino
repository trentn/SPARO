#include<Stepper.h>

const int stepsPerRevolution = 400;
Stepper end_effector(stepsPerRevolution, 8, 9, 10, 11);
String input_string;
//int stepCount = 0;
double degree_rotation = 0;
int number_steps = 0;

void setup() {
  // put your setup code here, to run once:
  input_string.reserve(50);
  //end_effector.setSpeed(30);
  Serial.begin(9600);
}

void loop() {
  while (true)
  {
    input_string = Serial.readStringUntil('\n');
    degree_rotation = input_string.toDouble();
    number_steps = (int) (degree_rotation / 360.0 * stepsPerRevolution);
    //end_effector.step(number_steps);

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
}
