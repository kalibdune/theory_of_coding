from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QWidget

from Check_mat import chet_mat
from just_bin import binary_code

class Parity_check(QWidget):
    def __init__(self, *args, **kwargs):
        super(Parity_check, self).__init__(*args, **kwargs)
        uic.loadUi('ui/Parity_method.ui', self)
        
        self.coding.clicked.connect(self.coding_button_handler)
        self.no_coding.clicked.connect(self.no_coding_button_handler)

    def coding_button_handler(self):
        text = self.user_text.toPlainText()
        self.binary_text.setPlainText(chet_mat(text.strip()))

    def no_coding_button_handler(self):
        text = self.user_text.toPlainText()
        self.binary_text.setPlainText(binary_code(text.strip()))

if __name__ == '__main__':
    app = QApplication([])
    wimdow = Parity_check()
    wimdow.show()
    app.exec_()