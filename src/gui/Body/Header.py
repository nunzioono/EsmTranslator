from PyQt5.QtWidgets import QFrame,QHBoxLayout,QVBoxLayout,QPushButton,QLabel
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins, QDir
from PyQt5.QtGui import QIcon, QPixmap, QFont

class Header(QFrame):

    def __init__(self,parent,mode=""):
        super().__init__(parent)

        self.frame2=QFrame(self)

        if mode=="back":
            self.arrowback=QPushButton(self.frame2)
            self.arrowback.setFixedSize(11, 30)
            self.arrowback.setStyleSheet("border:0px;")
            self.arrowback.setIcon(QIcon(QPixmap(QDir.currentPath()+'/gui/assets/Arrow Back.png')))
        self.logotype=QLabel(self.frame2)
        self.logotype.setFixedSize(380, 30)
        self.logotype.setPixmap(QPixmap(QDir.currentPath()+'/gui/assets/Logotype.png'))
        
        layout=QHBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(QMargins(0,0,0,0))
        if mode=="back":
            layout.addWidget(self.arrowback)
        layout.addWidget(self.logotype)
        if mode=="back":
            layout.insertSpacing(2, 220)
        self.frame2.setLayout(layout)

        self.selectionlabel=QLabel()
        font=QFont("Noto Sans",12)
        font.setBold(True)
        self.selectionlabel.setFont(font)
        self.selectionlabel.setText("Seleziona un traduttore per continuare:")
        self.selectionlabel.setStyleSheet("color:white")

        layout2=QVBoxLayout()
        layout2.setSpacing(20)
        layout2.setContentsMargins(0,0,0,0)
        layout2.addWidget(self.frame2,Qt.AlignTop,Qt.AlignCenter)
        layout2.addWidget(self.selectionlabel,Qt.AlignTop,Qt.AlignCenter)
        self.setLayout(layout2)
        self.show()