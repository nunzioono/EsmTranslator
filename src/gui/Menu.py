from tkinter import HORIZONTAL
from PyQt5.QtWidgets import QPushButton, QFrame, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore
#import os

class Menu(QFrame):

    def __init__(self,container):
        super().__init__(container)
        self.setFixedSize(165,42)
        self.move(1115,0)
        layout=QHBoxLayout()
        self.setLayout(layout)
        self.b1=QPushButton(self)
        self.b1.setIcon(QIcon(QPixmap('C:/Users/nunzi/Desktop/fallout_mods/EsmTranslator/src/gui/assets/Riduci.png')))
        self.b1.setFixedSize(55,42)
        self.b1.setStyleSheet("border:0px")
        self.b1.show()
        self.b1.clicked.connect(self.reduceWindow)
        self.b2=QPushButton(self)
        self.b2.setIcon(QIcon(QPixmap('C:/Users/nunzi/Desktop/fallout_mods/EsmTranslator/src/gui/assets/Espandi.png')))
        self.b2.move(55,0)
        self.b2.setFixedSize(55,42)
        self.b2.setStyleSheet("border:0px")
        self.b2.show()
        self.b3=QPushButton(self)
        self.b3.setIcon(QIcon(QPixmap('C:/Users/nunzi/Desktop/fallout_mods/EsmTranslator/src/gui/assets/Chiudi.png')))
        self.b3.move(110,0)
        self.b3.setFixedSize(55,42)
        self.b3.setStyleSheet("QPushButton{border:0px;}""QPushButton:hover{background:#DC2020;}")
        self.b3.clicked.connect(self.closeWindow)
        self.b3.show()
        layout.addChildWidget(self.b1)
        layout.addChildWidget(self.b2)
        layout.addChildWidget(self.b3)

    def reduceWindow(self):
        #os.system(cmd)
        self.showMinimized()

    def closeWindow(self):
        #os.system(cmd)
        QtCore.QCoreApplication.instance().quit()

    def mousePressEvent(self, event):
        print(event.x())

    def mouseMoveEvent(self, event):
        return
    def mouseReleaseEvent(self, event):
        return