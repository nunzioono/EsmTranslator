from PyQt5.QtWidgets import QLabel, QWidget, QGridLayout, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.Qt import Qt
import math

class LoadingBar(QWidget):

    TOTAL_SIZE=854

    def __init__(self,parent,forwardbutton,perc,extractor,textenabled=False,loadingtext="",completetext=""):
        super().__init__(parent)
        self.extractor=extractor
        self.loadingtext=loadingtext
        self.completetext=completetext
        self.perc=perc
        self.textenabled=textenabled
        self.forwardbutton=forwardbutton
        self.layout=QGridLayout()
        self.layout.setContentsMargins(0,0,0,0)
        
        self.update()

        self.setLayout(self.layout)
        self.show()

    def update(self):

        layout=QGridLayout()

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

        
        ncols=math.floor((LoadingBar.TOTAL_SIZE-4)*self.perc)

        self.label3=QLabel(self)
        font=QFont("Noto sans",12)
        font.setBold(True)
        self.label3.setFont(font)
        self.label3.setText(str(math.floor(self.perc*100))+"%")
        self.label3.setStyleSheet("""QLabel{
            color:white;
            background:transparent;
        }""")

        layout.addWidget(self.label,0,0,28,LoadingBar.TOTAL_SIZE)
        layout.addWidget(self.label2,1,2,26,ncols)
        layout.addWidget(self.label3,1,406,26,40)

        if(self.textenabled):
            self.label4=QLabel(self)
            font=QFont("Noto sans",12)
            font.setBold(True)
            self.label4.setFont(font)
            if self.perc<1:
                self.label4.setText(self.loadingtext)
            else:
                self.label4.setText(self.completetext)
            self.label4.setStyleSheet("""QLabel{
                color:white;
                background:transparent;
            }""")

        self.layout=QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addLayout(layout)
        if(self.textenabled):
            self.layout.addSpacing(50)
            self.layout.addWidget(self.label4,Qt.AlignCenter,Qt.AlignCenter)
        if self.perc==1:
            self.forwardbutton.show()

    def removeAll(self):
        items = (self.layout.itemAt(i) for i in range(self.layout.count())) 
        for w in items:
            w.widget().deleteLater()