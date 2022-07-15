from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from gui.Body.LoadingBar import LoadingBar

class TranslationLoading(QWidget):

    perc=0

    def __init__(self,parent,forwardbutton,perc=0,estimatedtime="0:00"):
        super().__init__(parent)
        TranslationLoading.perc=perc
        self.estimatedtime=estimatedtime
        self.forwardbutton=forwardbutton
        self.layout=QVBoxLayout()
                
        self.update()

        self.setLayout(self.layout)

    def update(self):
        self.removeAll()
        self.label=QLabel(self)
        if TranslationLoading.perc<1:
            self.label.setText("Traduzione in corso... (Tempo Stimato "+self.estimatedtime+")")
        else:
            self.label.setText("Traduzione completata.")
        self.label.setStyleSheet("""QLabel{
            color:white;
        }""")
        font=QFont("Noto sans",10)
        font.setBold(True)
        self.label.setFont(font)

        self.loadingbar=LoadingBar(self,self.forwardbutton,TranslationLoading.perc)

        self.translationbody=QLabel(self)
        self.translationbody.setStyleSheet("""QLabel{
            background:#393473;
            color:white;
            border:2px solid #707070;
            border-radius:9px;
        }""")
        self.translationbody.setFixedSize(854,300)

        self.layout.addWidget(self.label,Qt.AlignLeft)
        self.layout.addWidget(self.loadingbar,Qt.AlignLeft)
        self.layout.addWidget(self.translationbody,Qt.AlignLeft)
        if TranslationLoading.perc==1:
            self.forwardbutton.show()

    def addTranslatedString(self,translatedstring):
        text=self.translationbody.text
        self.translationbody.setText(text+translatedstring)

    def removeAll(self):
        items = (self.layout.itemAt(i) for i in range(self.layout.count())) 
        for w in items:
            w.widget().deleteLater()