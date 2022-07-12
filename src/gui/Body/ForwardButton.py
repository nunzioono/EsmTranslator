from PyQt5.QtWidgets import QFrame,QGridLayout,QVBoxLayout,QPushButton
from PyQt5.QtGui import QFont

class ForwardButton(QPushButton):

    def __init__(self,parent,text="AVANTI",font_size=12):
        super().__init__(parent)
        self.setText(text)
        self.setFixedSize(133,41)
        self.setFont(QFont("Noto sans",font_size))
        self.setStyleSheet("""QPushButton{
            background:#2B55FC;
            color:white;
            border-radius: 20px;
        }""")
        sp_retain = self.sizePolicy()
        sp_retain.setRetainSizeWhenHidden(True)
        self.setSizePolicy(sp_retain)