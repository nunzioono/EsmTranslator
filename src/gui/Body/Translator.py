from PyQt5.QtWidgets import QFrame,QVBoxLayout,QPushButton,QLabel
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins, QDir
from PyQt5.QtGui import QIcon, QPixmap, QFont
from gui.Body.RoundedProgressBar import RoundedProgressBar

class Translator(QFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.setFixedSize(220, 220)
        self.setStyleSheet("""QFrame{
            padding:10px;
            border: 2px solid #707070;
            border-radius: 25px;
        }""")


        self.paintedarc=RoundedProgressBar(self)
        self.paintedarc.show()

        self.frame1=QFrame(self)
        self.frame1.setStyleSheet('''QFrame{
            border-width: 0px;
        }''')
        self.icon=QLabel(self.frame1)
        self.icon.setFixedSize(49,49)
        self.icon.setPixmap(QPixmap(QDir.currentPath()+'/gui/assets/DeepL logo.png'))
        self.icon.setStyleSheet('''QLabel{
                                    padding:0px;
                                    border-width: 0px;
                                    border-radius: 25px;
                                    min-height: 49px;
                                    min-width: 49px;
                                    }''')
        self.name=QLabel(self.frame1)
        font1=QFont('Noto Sans',16)
        font1.setBold(True)
        self.name.setFont(font1)
        self.name.setText("DeepL Free")
        self.name.setStyleSheet('''QLabel{
                                    padding:0px;
                                    border-width: 0px;
                                    color:#707070;
                                    }''')
        layout1=QVBoxLayout()
        layout1.setSpacing(0)
        layout1.setContentsMargins(QMargins(0,0,0,0))
        layout1.addWidget(self.icon,Qt.AlignTop,Qt.AlignCenter)
        layout1.addWidget(self.name,Qt.AlignTop,Qt.AlignCenter)
        self.frame1.setLayout(layout1)

        self.frame2=QFrame(self)
        self.frame2.setStyleSheet('''QFrame{
            border-width: 0px;
        }''')
        self.consume=QLabel(self.frame2)
        self.consume.setFont(QFont("Noto Sans",12))
        self.consume.setText("83K/500K")
        self.consume.setStyleSheet('''QLabel{
                                    padding:0px;
                                    border-width: 0px;
                                    color:#707070;
                                    }''')
        self.renewdate=QLabel(self.frame2)
        self.renewdate.setFont(QFont("Noto Sans",10))
        self.renewdate.setText("Reset il 27/08/2022")
        self.renewdate.setStyleSheet('''QLabel{
                                    padding:0px;
                                    border-width: 0px;
                                    color:#707070;
                                    }''')
        layout2=QVBoxLayout()
        layout2.setSpacing(0)
        layout2.setContentsMargins(QMargins(0,0,0,0))
        layout2.addWidget(self.consume,Qt.AlignTop,Qt.AlignCenter)        
        layout2.addWidget(self.renewdate,Qt.AlignTop,Qt.AlignCenter)        
        self.frame2.setLayout(layout2)

        layout=QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(QMargins(0,0,0,0))
        layout.addWidget(self.paintedarc,Qt.AlignTop,Qt.AlignCenter)
        layout.addWidget(self.frame1,Qt.AlignTop,Qt.AlignCenter)
        layout.addWidget(self.frame2,Qt.AlignTop,Qt.AlignCenter)
        self.setLayout(layout)
        self.show()

    def mousePressEvent(self, event):
        print("!")