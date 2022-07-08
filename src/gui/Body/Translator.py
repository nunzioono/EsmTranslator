from PyQt5.QtWidgets import QFrame,QVBoxLayout,QPushButton,QLabel
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins, QDir
from PyQt5.QtGui import QIcon, QPixmap, QFont

class Translator(QFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.setFixedSize(220, 220)
        self.setStyleSheet("""QFrame{
            border: 1px solid #707070;
            border-radius: 25px;
        }""")

        self.icon=QLabel(self)
        self.icon.setFixedSize(49,49)
        self.icon.setPixmap(QPixmap(QDir.currentPath()+'/gui/assets/DeepL logo.png'))
        self.icon.setStyleSheet("""QLabel{
                                    border-width: 0px;
                                    border-radius: 25px;
                                    min-height: 49px;
                                    min-width: 49px;
                                    }""")
        self.name=QLabel(self)
        font1=QFont("Noto Sans",16)
        font1.setBold(True)
        self.name.setFont(font1)
        self.name.setText("DeepL Free")
        self.name.setStyleSheet("""QLabel{
                                    border-width: 0px;
                                    color:#707070;
                                    }""")
        self.consume=QLabel(self)
        self.consume.setFont(QFont("Noto Sans",12))
        self.consume.setText("83K/500K")
        self.consume.setStyleSheet("""QLabel{
                                    border-width: 0px;
                                    color:#707070;
                                    }""")
        self.renewdate=QLabel(self)
        self.renewdate.setFont(QFont("Noto Sans",10))
        self.renewdate.setText("Reset il 27/08/2022")
        self.renewdate.setStyleSheet("""QLabel{
                                    border-width: 0px;
                                    color:#707070;
                                    background:red;
                                    }""")
        self.layout=QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(QMargins(0,0,0,0))
        self.layout.addWidget(self.icon,Qt.AlignCenter,Qt.AlignCenter)
        self.layout.addWidget(self.name,Qt.AlignCenter,Qt.AlignCenter)
        self.layout.addWidget(self.consume,Qt.AlignCenter,Qt.AlignCenter)
        self.layout.addWidget(self.renewdate,Qt.AlignCenter,Qt.AlignCenter)
        self.setLayout(self.layout)
        self.show()

    def mousePressEvent(self, event):
        print("!")