from PyQt5.QtWidgets import QPushButton, QFrame, QHBoxLayout, QSizePolicy
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5 import QtCore
from PyQt5.QtCore import QDir, Qt, QMargins
#import os

class Menu(QFrame):

    def __init__(self,container):
        super().__init__(container)
        self.parent=container
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)

        self.b1=QPushButton(self)
        self.b1.setIcon(QIcon(QPixmap(QDir.currentPath()+'/gui/assets/Riduci.png')))
        self.b1.setFixedSize(55,35)
        self.b1.setStyleSheet("QPushButton{border:0px;}""QPushButton:hover{background:#393473;}")
        self.b1.clicked.connect(self.reduceWindow)
        self.b1.show()
        self.b2=QPushButton(self)
        self.b2.setIcon(QIcon(QPixmap(QDir.currentPath()+'/gui/assets/Chiudi.png')))
        self.b2.setFixedSize(55,35)
        self.b2.setStyleSheet("QPushButton{border:0px;}""QPushButton:hover{background:#DC2020;}")
        self.b2.clicked.connect(self.closeWindow)
        self.b2.show()
        
        layout=QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(QMargins(0,0,0,0))
        layout.addWidget(self.b1)
        layout.addWidget(self.b2)
        self.setLayout(layout)

    def reduceWindow(self):
        #os.system(cmd)
        self.parent.showMinimized()

    def closeWindow(self):
        #os.system(cmd)
        QtCore.QCoreApplication.instance().quit()

    def mousePressEvent(self, event):
        return
    def mouseMoveEvent(self, event):
        return
    def mouseReleaseEvent(self, event):
        return