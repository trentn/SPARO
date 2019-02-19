#include "DC_MotorwEnc_Control.h"



DC_Motor::DC_Motor(int pin1, int pin2, int pin_en, int pinA, int pinB, int clicks)
{
	Encoder temp(pinA, pinB);
	encoder = &temp;
	in1 = pin1;
	in2 = pin2;
	en = pin_en;
	encA = pinA;
	encB = pinB;
	CPR = clicks;
}

void DC_Motor::updateStates()//updates states one iteration
{
	
	for (int i = 2; i > 0; i--)
	{
		for (int j = 0; j < 4; j++)
		{
			states[j][i] = states[j][i-1]; //pushing states back
		}
		
	}

	states[0][0] = encoder->read();
	states[3][0] = millis();

	states[1][0] = (states[0][0] - states[0][1]) / (states[3][0] - states[3][1]); //new velocity
	states[2][0] = (states[1][0] - states[1][1]) / (states[3][0] - states[3][1]); //new acceleration
	


}

void DC_Motor::initializeStates()//runs through and fills initial state matrix, although, could probably just give time row values
{

	states[0][2] = encoder->read();
	states[3][2] = millis();
	delay(10);


	states[0][1] = encoder->read();
	states[3][1] = millis();
	delay(10);

	states[1][1] = (states[0][1] - states[0][2]) / (states[3][1] - states[3][2]); //differentiating velocity, in units of clicks per milli

	states[0][0] = encoder->read();
	states[3][0] = millis();

	states[1][0] = (states[0][0] - states[0][1]) / (states[3][0] - states[3][1]); //differentiating velocity, in units of clicks per milli

	states[2][0] = (states[1][0] - states[1][1]) / (states[3][0] - states[3][1]); //differentiating acceleration, in units of clicks per milli^2

	states[2][2] = 0;
	states[2][1] = 0;

	states[1][2] = 0;

}

void DC_Motor::speedControl(double desSpeed)
{
	updateStates();
	double err[2] = { desSpeed - states[1][0], desSpeed - states[1][1] };
	setPwm(currentPwm + (kp_vel * err[0] + kd_vel*(err[1]-err[0])/(states[3][0]-states[3][1])));
}

void DC_Motor::angleControl(double desAngle)
{
	updateStates();
	double err[2] = { desAngle - states[0][0], desAngle - states[0][1] };
	setPwm(kp_ang * err[0] + kd_ang*(err[1] - err[0]) / (states[3][0] - states[3][1]));

}

void DC_Motor::setPwm(double pwm)
{

	if (pwm > 255)
	{
		pwm = 255.;
	}
	else if (pwm < -255) //saturation conditions. Maybe flash led to indicate saturation?? Later
	{
		pwm = -255;
	}

	if (pwm < 0.)
	{
		digitalWrite(in2, HIGH);
		analogWrite(in1, 255 + pwm);
	}
	else if (pwm == 0)
	{
		digitalWrite(en, LOW);
		digitalWrite(in2, LOW);
		digitalWrite(in1, LOW);
	}
	else
	{
		digitalWrite(in2, LOW);
		analogWrite(in1, pwm);
	}

	currentPwm = pwm;

}

void DC_Motor::setPD_vel(double gains[2])
{
	kp_vel = gains[0];
	kd_vel = gains[1];
}

void DC_Motor::setPD_ang(double gains[2])
{
	kp_ang = gains[0];
	kd_ang = gains[1];
}

