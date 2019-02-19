#ifndef DC_MotorwEnc_Control
#define DC_MotorwEnc_Control

#include <Encoder.h>

class DC_Motor{
public:
	int in1;
	int in2;
	int en;
	int encA;
	int encB;
	int led_pin = -1;

	int CPR;
	DC_Motor();
	DC_Motor(int pin1, int pin2, int pin_en, int pinA, int pinB, int clicks);
	

	Encoder* encoder; //pointer to encoder object location

	double states[5][3]; // [state type][iteration #] state order (position(clicks), velocity(clicks/ms), acceleration(clicks/ms^2), time(ms))

	double currentPwm = 0;

	double kp_vel, kd_vel = 0;

	double kp_ang, kd_ang = 0;

	void updateStates(); //updates states one iteration

	void initializeStates(); //runs through and fills initial state matrix

	void speedControl(double desSpeed); //speed controller

	void angleControl(double desAngle); //angle controller (absolute)

	void setPwm(double pwm); //set motor speed and direction (-255 to 255) but can accept values outside this

	void setPD_vel(double gains[2]); //quick gain set command velocity control

	void setPD_ang(double gains[2]); //quick gain set command angle control


};

#endif

