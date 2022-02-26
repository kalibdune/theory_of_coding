from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget

from Check_mat import chet_mat, decode_mat
from just_bin import binary_code, to_word
from random_bit import random_error

class Parity_check(QWidget):
    def __init__(self, *args, **kwargs):
        super(Parity_check, self).__init__(*args, **kwargs)
        uic.loadUi('ui/Parity_method.ui', self)
        
        self.coding_button_pressed = False

        self.coding.clicked.connect(self.coding_button_handler)
        self.no_coding.clicked.connect(self.no_coding_button_handler)
        self.error_button.clicked.connect(self.error_button_handler)
        self.clear_button.clicked.connect(self.clear)

    def coding_button_handler(self):
        self.coding_button_pressed = True
        text = self.user_text.toPlainText()
        self.binary_text.setPlainText(chet_mat(text.strip()))

    def no_coding_button_handler(self):
        self.coding_button_pressed = False
        text = self.user_text.toPlainText()
        self.binary_text.setPlainText(binary_code(text.strip()))
    
    def error_button_handler(self):
        text = self.binary_text.toPlainText()
        error_text = random_error(text)
        self.error_text.setHtml(error_text)
        if self.coding_button_pressed == True:
            self.decoded_text.setHtml(decode_mat(error_text))
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
    wimdow = Parity_check()
    wimdow.show()
    app.exec_()