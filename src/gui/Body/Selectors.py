from ctypes import sizeof
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import requests
import json

class Selectors(QWidget):

    language_src=[]
    language_target=[]
    current_src=""
    current_target=""

    def __init__(self,parent,forwardbutton):
        super().__init__(parent)
        self.forwardbutton=forwardbutton
        self.layout=QVBoxLayout()

        self.getData()

        self.setLayout(self.layout)
        self.show()

    def update(self):

        self.select1=QComboBox(self)
        self.select1.setFixedSize(602,27)
        self.select1.setStyleSheet("""QComboBox{
            background:#7974B3;
            color:white;
            border-width:0px;
        }
        QComboBox.drop-down{
            background:#7974B3;
            color:white;
        }""")
        font=QFont("Noto sans",10)
        font.setBold(True)
        self.select1.setFont(font)
        self.select1.addItem("Scegli la lingua da cui vuoi tradurre")
        for language in Selectors.language_src:
            self.select1.addItem(language["language"])
        self.select1.currentIndexChanged.connect(self.onSelectChange)

        self.select2=QComboBox(self)
        self.select2.setFixedSize(602,27)
        self.select2.setStyleSheet("""QComboBox{
            background:#7974B3;
            color:white;
            border-width:0px;
        }""")
        self.select2.setFont(font)
        self.select2.addItem("Scegli la lingua in cui vuoi tradurre")
        for language in Selectors.language_target:
            self.select2.addItem(language["language"])
        self.select2.currentIndexChanged.connect(self.onSelectChange)

        self.layout.addWidget(self.select1,Qt.AlignCenter)
        self.layout.addSpacing(40)
        self.layout.addWidget(self.select2,Qt.AlignCenter)

    def getData(self):
        response=requests.get("http://esmtranslator.altervista.org/api/translator_language/read.php")
        jsonresponse=json.loads(response.text)
        records=jsonresponse["records"]
        for record in records:
            if record["destination"]=='1':
                Selectors.language_target.append(record)
            elif record["destination"]=='0':
                Selectors.language_src.append(record)
        
        #self.removeAll()
        self.update()

    def removeAll(self):
        items = (self.layout.itemAt(i) for i in range(self.layout.count())) 
        for w in items:
            w.widget().deleteLater()

    def onSelectChange(self):
        if self.select1.currentIndex()!=0 and self.select2.currentIndex()!=0:
            self.forwardbutton.show()
            index_src=self.select1.currentIndex()-1
            Selectors.current_src=Selectors.language_src[index_src]["language_tag"]
            index_target=self.select2.currentIndex()-1
            Selectors.current_target=Selectors.language_target[index_target]["language_tag"]
        else:
            self.forwardbutton.hide()