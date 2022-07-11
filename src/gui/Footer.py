from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt

class Footer(QLabel):

    def __init__(self,parent):
        super().__init__(parent)
        self.setFixedSize(1280,21)
        self.setText("v1.0.0")
        self.setAlignment(Qt.AlignRight)
        self.setFont(QFont("Noto sans",10))
        self.setStyleSheet("""QLabel{
            color:white;
        }""")