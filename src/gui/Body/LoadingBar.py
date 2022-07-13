from PyQt5.QtWidgets import QLabel, QWidget, QGridLayout
from PyQt5.QtGui import QFont
import math

class LoadingBar(QWidget):

    TOTAL_SIZE=854

    def __init__(self,parent,forwardbutton,perc):
        super().__init__(parent)
        self.layout=QGridLayout()
        self.layout.setContentsMargins(0,0,0,0)
        
        self.update()

        self.setLayout(self.layout)
        self.show()

    def update(self):
        self.label=QLabel(self)
        self.label.setFixedSize(LoadingBar.TOTAL_SIZE,28)
        self.label.setStyleSheet("""QLabel{
            background:#7974B3;
            border:2px solid #707070;
            border-radius:9px;
        }""")

        self.label2=QLabel(self)
        self.label2.setMaximumWidth(LoadingBar.TOTAL_SIZE)
        self.label2.setFixedHeight(24)
        self.label2.setStyleSheet("""QLabel{
            background:#393473;
            border-radius:9px;
        }""")

        
        ncols=math.floor((LoadingBar.TOTAL_SIZE-4)*perc)

        self.label3=QLabel(self)
        font=QFont("Noto sans",12)
        font.setBold(True)
        self.label3.setFont(font)
        self.label3.setText(str(math.floor(perc*100))+"%")
        self.label3.setStyleSheet("""QLabel{
            color:white;
            background:transparent;
        }""")

        self.layout.addWidget(self.label,0,0,28,LoadingBar.TOTAL_SIZE)
        self.layout.addWidget(self.label2,1,2,26,ncols)
        self.layout.addWidget(self.label3,1,416,26,40)

    def removeAll(self):
        items = (self.layout.itemAt(i) for i in range(self.layout.count())) 
        for w in items:
            w.widget().deleteLater()