import sys

from PyQt5.QtWidgets import QPushButton

class Mainwindow(QMainWindow):
	def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 90)
        self.setWindowTitle(':)')

        self.first_value = QLineEdit(self)
        self.first_value.move(100, 90)