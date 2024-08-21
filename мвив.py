from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from random import randint

app = QApplication([])

win = QWidget()
win.setWindowTitle('Визначити переможця')
win.move(100, 100)
win.resize(400, 350)

button = QPushButton('Згенерувати')
text = QLabel('Натисніть щоб дізнатися переможця')
num = QLabel('?')

line = QVBoxLayout()
line.addWidget(text, alignment=Qt.AlignCenter)
line.addWidget(num, alignment=Qt.AlignCenter)
line.addWidget(button, alignment=Qt.AlignCenter)
win.setLayout(line)

def rand_num():
    number = randint(0, 99)
    num.setText (str(number))
    text.setText('Переможець:')

button.clicked.connect(rand_num)

win.show()
app.exec_()

