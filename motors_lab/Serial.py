import serial, time
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread


class ProcessSerial(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.ser = serial.Serial()

    def __del__(self):
        self.wait()

    
    def set_output(self, output):
        self.output = output

    def build_serial_config(self, port_name, baud_rate, accept):
        def configure_serial():
            self.ser.port = port_name.text()
            self.ser.baudrate = int(baud_rate.text())
            self.ser.open()
            self.start()
            accept()
        return configure_serial

    def build_stepper_command(self, forward, reverse, degrees):
        def stepper_command():
            if(self.ser.is_open):
                if(forward.isChecked()):
                    self.ser.write(b'S F %d\n' % degrees.value())
                elif(reverse.isChecked()):
                    self.ser.write(b'S R %d\n' % degrees.value())
        return stepper_command

    def build_rcservo_command(self, angle):
        def rcservo_command():
            if(self.ser.is_open):
                self.ser.write(b'R %d\n' % angle.value())
        return rcservo_command

    def build_dcmotor_command(self, forward, reverse, degrees, speed):
        def dcmotor_command():
            if(self.ser.is_open):
                if(forward.isChecked()):
                    self.ser.write(b'D F %d %d\n' % (degrees.value(), speed.value()))
                elif(reverse.isChecked()):
                    self.ser.write(b'D R %d %d\n' % (degrees.value(), speed.value()))
        return dcmotor_command

    def run(self):
        while True:
            out = self.ser.readline()
            self.output.setText(str(out)) #will crash app after too much data
            print(out)