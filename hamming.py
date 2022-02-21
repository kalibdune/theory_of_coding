from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget
import sys

from Hameng import hamming
from just_bin import binary_code

class Haming_method(QWidget):
    def __init__(self, *args, **kwargs):
        super(Haming_method, self).__init__(*args, **kwargs)
        uic.loadUi('ui/Haming_method.ui', self)

        self.coding.clicked.connect(self.coding_button_handler)
        self.no_coding.clicked.connect(self.no_coding_button_handler)

    def coding_button_handler(self):
        text = self.user_text.toPlainText()
        self.binary_text.setPlainText(hamming(text))

    def no_coding_button_handler(self):
        text = self.user_text.toPlainText()
        self.binary_text.setPlainText(binary_code(text))

if __name__ == '__main__':
    app = QApplication([])
    wimdow = Haming_method()
    wimdow.show()
    app.exec_()