from PyQt5.QtWidgets import QFrame,QVBoxLayout,QPushButton,QLabel
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins, QDir
from PyQt5.QtGui import QIcon, QPixmap, QFont

class Translator(QFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.setFixedSize(220, 220)
        self.setStyleSheet("background:blue")

        self.icon=QLabel(self)
        self.icon.setFixedSize(49,49)
        self.icon.setPixmap(QPixmap(QDir.currentPath()+'/gui/assets/DeepL logo.png'))
        self.icon.setStyleSheet("""QLabel{border-radius: 25px;
                                    min-height: 49px;
                                    min-width: 49px;
                                    border: 1px solid #707070;}""")
        self.name=QLabel(self)
        font1=QFont("Noto Sans",16)
        font1.setBold(True)
        self.name.setFont(font1)
        self.name.setText("DeepL Free")
        self.name.setStyleSheet("background:green;color:#707070")
        self.consume=QLabel(self)
        self.consume.setFont(QFont("Noto Sans",12))
        self.consume.setStyleSheet("background:green;color:#707070")
        self.consume.setText("83K/500K")
        self.renewdate=QLabel(self)
        self.renewdate.setFont(QFont("Noto Sans",10))
        self.renewdate.setStyleSheet("background:green;color:#707070")
        self.renewdate.setText("Reset il 27/08/2022")

        layout=QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(QMargins(0,0,0,0))
        layout.addWidget(self.icon,Qt.AlignCenter,Qt.AlignCenter)
        layout.addWidget(self.name,Qt.AlignCenter,Qt.AlignCenter)
        layout.addWidget(self.consume,Qt.AlignCenter,Qt.AlignCenter)
        layout.addWidget(self.renewdate,Qt.AlignCenter,Qt.AlignCenter)
        self.setLayout(layout)
        self.show()

    def mousePressEvent(self, event):
        print("!")