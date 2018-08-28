from PyQt5 import QtWidgets
import UI_register
Ui_MainWindow = UI_register.Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        #insert your functions
