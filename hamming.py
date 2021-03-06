from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget
import sys

from Hameng import hamming, multi_decoding_hamming
from just_bin import binary_code, to_word
from random_bit import random_error

class Haming_method(QWidget):
    def __init__(self, *args, **kwargs):
        super(Haming_method, self).__init__(*args, **kwargs)
        uic.loadUi('ui/Haming_method.ui', self)

        self.coding_button_pressed = False

        self.coding.clicked.connect(self.coding_button_handler)
        self.no_coding.clicked.connect(self.no_coding_button_handler)
        self.error_button.clicked.connect(self.error_button_handler)
        self.clear_button.clicked.connect(self.clear)

    def coding_button_handler(self):
        self.coding_button_pressed = True
        text = self.user_text.toPlainText()
        self.binary_text.setPlainText(hamming(text.strip()))

    def no_coding_button_handler(self):
        self.coding_button_pressed = False
        text = self.user_text.toPlainText()
        self.binary_text.setPlainText(binary_code(text))
    
    def error_button_handler(self):
        text = self.binary_text.toPlainText()
        error_text = random_error(text)
        self.error_text.setHtml(error_text)
        if self.coding_button_pressed == True:
            self.decoded_text.setHtml(multi_decoding_hamming(error_text))
        else:
            code = self.binary_text.toPlainText()
            self.decoded_text.setHtml(to_word(error_text, code))

    def clear(self):
        self.user_text.clear()
        self.binary_text.clear()
        self.error_text.clear()
        self.decoded_text.clear()

if __name__ == '__main__':
    app = QApplication([])
    wimdow = Haming_method()
    wimdow.show()
    app.exec_()