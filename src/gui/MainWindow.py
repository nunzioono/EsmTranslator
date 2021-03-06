import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QPoint, QDir
from PyQt5.QtWidgets import QMainWindow, QLabel, QDesktopWidget, QVBoxLayout
from gui.MainContainer import MainContainer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon(QPixmap(QDir.currentPath()+'/gui/assets/Logo.png')))
        self.setWindowTitle('EsmTranslator')
        self.setFixedSize(1280, 668)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.center()

        self.container=MainContainer(self)
        self.setCentralWidget(self.container)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

