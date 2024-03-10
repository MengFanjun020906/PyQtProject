
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit

app = QApplication([])#底层功能函数，要先写

window = QMainWindow()
window.resize(500, 400)#决定window大小
window.move(300, 310)#控制窗口出现在显示器的位置
window.setWindowTitle('薪资统计')

textEdit = QPlainTextEdit(window)#创建文本输入框
textEdit.setPlaceholderText("请输入薪资表")#创建输入框内提示文本
textEdit.move(10,25)#里面编辑框的位置
textEdit.resize(300,350)

button = QPushButton('统计', window)#设置按钮
button.move(380,80)

window.show()#把窗口展现出来

app.exec_()#死循环，等待用户关闭