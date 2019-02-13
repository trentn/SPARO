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

    def build_dcmotor_position_command(self, forward, reverse, degrees):
        def dcmotor_position_command():
            if(self.ser.is_open):
                if(forward.isChecked()):
                    self.ser.write(b'D P F %d\n' % degrees.value())
                elif(reverse.isChecked()):
                    self.ser.write(b'D P R %d\n' % degrees.value())
        return dcmotor_position_command

    def build_dcmotor_speed_command(self, forward, reverse, speed):
        def dcmotor_speed_command():
            if(self.ser.is_open):
                if(forward.isChecked()):
                    self.ser.write(b'D S F %d\n' % speed.value())
                elif(reverse.isChecked()):
                    self.ser.write(b'D S R %d\n' % speed.value())
        return dcmotor_speed_command


    def build_controls_changed(self, enabled):
        def controls_changed():
            if(self.ser.is_open):
                if(enabled.isChecked()):
                    self.ser.write(b'C G\n')
                else:
                    self.ser.write(b'C S\n')
        return controls_changed

    def run(self):
        while True:
            out = self.ser.readline()
            self.output.setText(str(out)) #will crash app after too much data
            print(out)