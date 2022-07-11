import math
from PyQt5.QtWidgets import QFrame,QGridLayout,QVBoxLayout,QPushButton,QLabel
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins, QDir
from PyQt5.QtGui import QIcon, QPixmap, QFont
from requests import request
import requests
from gui.Body.RoundedProgressBar import RoundedProgressBar
import json
from datetime import datetime

class Translator(QFrame):

    def __init__(self,parent,active):
        super().__init__(parent)
        self.setFixedSize(220, 220)
        self.active=active
        if self.active:
            self.setStyleSheet("""QFrame{
                padding:10px;
                border: 2px solid #707070;
                border-radius: 25px;
            }""")

            self.getData()

            self.paintedarc=RoundedProgressBar(self,self.consumption,self.limit)
            self.move(15,15)
            self.paintedarc.show()
            self.setFrame1()
            self.setFrame2()

            layout=QGridLayout()
            layout.setSpacing(0)
            layout.setContentsMargins(QMargins(0,0,0,0))
            layout.addWidget(self.frame1,2,2,4,4)
            layout.addWidget(self.frame2,6,2,2,4)
            layout.addWidget(self.paintedarc,0,0,8,8)
        else:
            self.setStyleSheet("""QFrame{
                padding:10px;
                border: 2px dashed #707070;
                border-radius: 25px;
            }""")

            label=QLabel(self)
            print(QDir.currentPath())
            label.setPixmap(QPixmap(QDir.currentPath()+'/gui/assets/Piu.png'))
            label.setFixedSize(70,70)
            label.setStyleSheet("""QLabel{
                    padding:10px;
                    border-width:2px;
                    border-style:dashed;
                    border-color:#707070;
                    border-radius: 35px;
                }""")

            layout=QVBoxLayout()
            layout.setSpacing(0)
            layout.setContentsMargins(QMargins(0,0,0,0))
            layout.addWidget(label,Qt.AlignCenter,Qt.AlignCenter)
        #layout.setCurrentIndex(2)
        self.setLayout(layout)
        self.show()

    def mousePressEvent(self, event):
        print("!")

    def round1k(self,number):
        div=number/1000
        return str(math.floor(div))

    def setFrame1(self):
        self.frame1=QFrame(self)
        self.frame1.setStyleSheet('''QFrame{
            border-width: 0px;
            border-radius: 0px;
        }''')
        self.frame1.move(0,0)
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
        font1=QFont('Noto Sans',14)
        font1.setBold(True)
        self.name.setFont(font1)
        self.name.setText("DeepL")
        self.name.setStyleSheet('''QLabel{
                                    padding:0px;
                                    border-width: 0px;
                                    border-radius: 0px;
                                    color:#707070;
                                    }''')
        layout1=QVBoxLayout()
        layout1.setSpacing(0)
        layout1.setContentsMargins(QMargins(0,0,0,0))
        layout1.addWidget(self.icon,Qt.AlignTop,Qt.AlignCenter)
        layout1.addWidget(self.name,Qt.AlignTop,Qt.AlignCenter)
        self.frame1.setLayout(layout1)

    def setFrame2(self):
        self.frame2=QFrame(self)
        self.frame2.setStyleSheet('''QFrame{
            border-width: 0px;
            border-radius: 0px;
        }''')
        self.frame2.move(100,100)
        self.consume=QLabel(self.frame2)
        self.consume.setFont(QFont("Noto Sans",10))
        self.consume.setText(self.round1k(self.consumption)+"K/"+self.round1k(self.limit)+"K")
        self.consume.setStyleSheet('''QLabel{
                                    padding:0px;
                                    border-width: 0px;
                                    border-radius: 0px;
                                    color:#707070;
                                    }''')
        self.renewdate=QLabel(self.frame2)
        self.renewdate.setFont(QFont("Noto Sans",6))
        self.renewdate.setText("Reset il "+self.lastupdate)
        self.renewdate.setStyleSheet('''QLabel{
                                    padding:0px;
                                    border-width: 0px;
                                    border-radius: 0px;
                                    color:#707070;
                                    }''')
        layout2=QVBoxLayout()
        layout2.setSpacing(0)
        layout2.setContentsMargins(QMargins(0,0,0,0))
        layout2.addWidget(self.consume,Qt.AlignTop,Qt.AlignCenter)        
        layout2.addWidget(self.renewdate,Qt.AlignTop,Qt.AlignCenter)        
        self.frame2.setLayout(layout2)

    def getData(self):
        response=requests.get("http://esmtranslator.altervista.org/api/translator/read.php")
        jsonresponse=json.loads(response.text)
        record=jsonresponse["records"][0]
        print(record)
        self.consumption=int(record["consumption"])
        self.limit=int(record["limit"])
        created_at=datetime.strptime(record["created_at"], '%y-%m-%d %H:%M:%S')
        print(created_at.strftime("%m/%d/%Y"))
        self.nextupdate=created_at.strftime("%m/%d/%Y")
