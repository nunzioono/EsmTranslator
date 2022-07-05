from PyQt5.QtWidgets import QPushButton, QFrame, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore
from PyQt5.QtCore import QDir
#import os

class Menu(QFrame):

    def __init__(self,container):
        super().__init__(container)
        self.parent=container
        self.setFixedSize(110,42)
        self.move(1170,0)
        layout=QHBoxLayout()
        self.setLayout(layout)
        self.b1=QPushButton(self)
        self.b1.setIcon(QIcon(QPixmap(QDir.currentPath()+'/gui/assets/Riduci.png')))
        self.b1.setFixedSize(55,42)
        self.b1.setStyleSheet("border:0px")
        self.b1.show()
        self.b1.clicked.connect(self.reduceWindow)
        self.b2=QPushButton(self)
        self.b2.setIcon(QIcon(QPixmap(QDir.currentPath()+'/gui/assets/Chiudi.png')))
        self.b2.move(55,0)
        self.b2.setFixedSize(55,42)
        self.b2.setStyleSheet("QPushButton{border:0px;}""QPushButton:hover{background:#DC2020;}")
        self.b2.clicked.connect(self.closeWindow)
        self.b2.show()
        layout.addChildWidget(self.b1)
        layout.addChildWidget(self.b2)

    def reduceWindow(self):
        #os.system(cmd)
        self.parent.showMinimized()

    def maximizeWindow(self):
        self.parent.showFullScreen()

    def closeWindow(self):
        #os.system(cmd)
        QtCore.QCoreApplication.instance().quit()

    def mousePressEvent(self, event):
        print(event.x())

    def mouseMoveEvent(self, event):
        return
    def mouseReleaseEvent(self, event):
        return