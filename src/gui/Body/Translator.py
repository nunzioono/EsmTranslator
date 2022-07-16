from zoneinfo import available_timezones
from PyQt5.QtWidgets import QFrame,QGridLayout,QVBoxLayout,QPushButton,QLabel,QWidget
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins, QDir, QEvent
from PyQt5.QtGui import QIcon, QPixmap, QFont
import requests, math, json
from gui.Body.RoundedProgressBar import RoundedProgressBar
from datetime import datetime

class Translator(QFrame):

    available_translators=[]
    choice=-1

    def __init__(self,parent,active,button):
        super().__init__(parent)
        self.setFixedSize(220, 220)
        self.forwardButton=button
        self.active=active
        self.selected=False
            
        if self.active:
            self.setStyleSheet("""QFrame{
                padding:10px;
                border: 2px solid #707070;
                border-radius: 25px;
            }""")

            self.getData()
            
            self.selector=QLabel(self)
            self.selector.setFixedSize(50,50)
            self.selector.setPixmap(QPixmap(QDir.currentPath()+'/gui/assets/Check.png'))
            self.selector.setStyleSheet("""QLabel{
                    border-width:0px;
                }""")
            self.selector.hide()
            self.paintedarc=RoundedProgressBar(self,self.consumption,self.limit)
            self.move(15,15)
            self.paintedarc.show()
            self.setFrame1()
            self.setFrame2()

            self.layout=QGridLayout()
            self.layout.setSpacing(0)
            self.layout.setContentsMargins(QMargins(0,0,0,0))
            self.layout.addWidget(self.selector,0,0,1,1)
            self.layout.addWidget(self.frame1,2,2,4,4)
            self.layout.addWidget(self.frame2,6,2,2,4)
            self.layout.addWidget(self.paintedarc,0,0,8,8)
        else:
            self.setToolTip("Prossimamente!")

            label=QLabel(self)
            label.setPixmap(QPixmap(QDir.currentPath()+'/gui/assets/Traduttore vuoto.png'))

            self.layout=QVBoxLayout()
            self.layout.setSpacing(0)
            self.layout.setContentsMargins(QMargins(0,0,0,0))
            self.layout.addWidget(label,Qt.AlignCenter,Qt.AlignCenter)
        #layout.setCurrentIndex(2)
        self.setLayout(self.layout)
        self.show()

    def mousePressEvent(self, event):
        if self.active:
            self.selected=not self.selected
            if(self.selected):
                self.selector.show()
                self.setStyleSheet("""QFrame{
                padding:10px;
                border: 2px solid #707070;
                border-radius: 25px;
                background:white;
            }""")
                self.forwardButton.show()
            else:
                self.selector.hide()
                self.setStyleSheet("""QFrame{
                padding:10px;
                border: 2px solid #707070;
                border-radius: 25px;
                background:transparent;
            }""")
                self.forwardButton.hide()


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
        self.renewdate.setText("Reset il "+self.nextupdate)
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
        Translator.available_translators=jsonresponse["records"]
        Translator.choice=0
        record=self.available_translators[self.choice]
        self.consumption=int(record["consumption"])
        self.limit=int(record["limit"])
        created_at=datetime.strptime(record["created_at"], '%Y-%m-%d %H:%M:%S')
        creation_day=int(created_at.strftime("%d"))
        creation_month=int(created_at.strftime("%m"))
        now=datetime.now()
        now_day=int(now.strftime("%d"))
        now_month=int(now.strftime("%m"))
        now_year=int(now.strftime("%Y"))
        if(now_day<=creation_day):
            update_month=str(now_month)
            update_year=str(now_year)
        else:
            if(now_month==12):
                update_month=str(1)
                update_year=str(now_year+1)
            else:
                update_month=str(now_month+1)
                update_year=str(now_year)
        self.nextupdate=str(creation_day)+"/"+update_month+"/"+update_year

    def getTranslators(self):
        return [Translator.available_translators,Translator.choice]