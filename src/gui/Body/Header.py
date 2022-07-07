from PyQt5.QtWidgets import QFrame,QHBoxLayout,QPushButton,QLabel
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins, QDir
from PyQt5.QtGui import QIcon, QPixmap

class Header(QFrame):

    def __init__(self,parent,mode=""):
        super().__init__(parent)

        if mode=="back":
            self.arrowback=QPushButton(self)
            self.arrowback.setFixedSize(11, 30)
            self.arrowback.setStyleSheet("border:0px;")
            self.arrowback.setIcon(QIcon(QPixmap(QDir.currentPath()+'/gui/assets/Arrow Back.png')))
        self.logotype=QLabel(self)
        self.logotype.setFixedSize(365, 30)
        self.logotype.setPixmap(QPixmap(QDir.currentPath()+'/gui/assets/Logotype.png'))
        
        layout=QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(QMargins(0,0,0,0))
        if mode=="back":
            layout.addWidget(self.arrowback)
        layout.addWidget(self.logotype)
        if mode=="back":
            layout.insertSpacing(2, 220)
        self.setLayout(layout)
        self.show()