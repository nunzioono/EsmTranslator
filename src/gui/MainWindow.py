import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMainWindow, QLabel, QDesktopWidget
from gui.Navbar import Navbar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon('assets/Logo.png'))
        self.setWindowTitle('EsmTranslator')
        self.setFixedSize(1280, 668)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.center()

        self.navbar= Navbar(self)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

