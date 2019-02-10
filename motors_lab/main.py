from GUI import *
from Serial import *
from PyQt5 import QtWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    serial_thread = ProcessSerial()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow, serial_thread)
    MainWindow.show()
    sys.exit(app.exec_())