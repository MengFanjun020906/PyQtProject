import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap

class ImageDisplayApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Image Display App')
        self.setGeometry(100, 100, 400, 300)

        self.button = QPushButton('选择图片', self)
        self.button.setGeometry(150, 200, 100, 30)
        self.button.clicked.connect(self.selectImage)

        self.image_label = QLabel(self)
        self.image_label.setGeometry(100, 50, 200, 100)

    def selectImage(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "选择图片", "", "All Files (*)", options=options)
        if file_name:
            pixmap = QPixmap(file_name)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ImageDisplayApp()
    ex.show()
    sys.exit(app.exec_())
