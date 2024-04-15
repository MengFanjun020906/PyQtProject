import sys
import csv
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QMessageBox

class LoginApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Login App')
        self.setGeometry(100, 100, 300, 150)

        self.username_edit = QLineEdit(self)
        self.username_edit.setPlaceholderText('Username')
        self.password_edit = QLineEdit(self)
        self.password_edit.setPlaceholderText('Password')
        self.password_edit.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton('登录', self)
        self.login_button.clicked.connect(self.login)
        self.register_button = QPushButton('注册', self)
        self.register_button.clicked.connect(self.register)

        layout = QVBoxLayout()
        layout.addWidget(self.username_edit)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)
        self.setLayout(layout)

    def login(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        # 在这里实现登录逻辑，比如检查用户名和密码是否匹配
        # 这里只是一个示例，你需要根据实际情况来编写登录逻辑
        if username == 'admin' and password == 'admin':
            QMessageBox.information(self, '登录成功', '登录成功！')
        else:
            QMessageBox.warning(self, '登录失败', '用户名或密码错误！')

    def register(self):
        username = self.username_edit.text()
        password = self.password_edit.text()

        # 在这里实现注册逻辑，将新用户信息保存到CSV文件中
        # 这里只是一个示例，你需要根据实际情况来编写注册逻辑
        with open('user_info.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([username, password])
        QMessageBox.information(self, '注册成功', '注册成功！')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LoginApp()
    ex.show()
    sys.exit(app.exec_())
