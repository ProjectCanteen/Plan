from PyQt5 import QtWidgets
import sys
#import all UI_actions here,for example:

def start(file_c):
    MainWindow = file_c.MainWindow
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
