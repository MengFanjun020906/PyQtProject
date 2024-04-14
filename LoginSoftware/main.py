from LoginUi import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_LoginWindow()
        self.ui.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setOffset(5,5)
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QtCore.Qt.gray)
        self.ui.frame.setGraphicsEffect(self.shadow)
        self.ui.pushButton_Login.clicked.connect(lambda :self.ui.stackedWidget_2.setCurrentIndex(1))
        self.ui.pushButton_Register.clicked.connect(lambda: self.ui.stackedWidget_2.setCurrentIndex(0))
        self.show()


if __name__ == '__main__':
    app= QApplication(sys.argv)
    win = LoginWindow()
    sys.exit(app.exec_())

