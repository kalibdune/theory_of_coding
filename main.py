from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QStackedWidget, QWidget, QMainWindow
import sys

from parity_check import Parity_check
from hamming import Haming_method

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('ui/main.ui', self)
        self.window = None
        self.Button_parity.clicked.connect(self.open_parity_window)
        self.Button_haming.clicked.connect(self.open_hamming_window)
    
    def open_parity_window(self):
        if self.window is None or 'Parity_check' or 'Haming_method':
            self.window = Parity_check()
        self.window.show()
    
    def open_hamming_window(self):
        if self.window is None or 'Parity_check' or 'Haming_method':
            self.window = Haming_method()
        self.window.show()

if __name__ == '__main__':
    app = QApplication([])
    wimdow = MainWindow()
    wimdow.show()
    app.exec_()