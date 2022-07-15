from PyQt5.QtWidgets import QFrame,QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins
from attr import has
from gui.Body.FileDownloader import FileDownloader
from gui.Body.ForwardButton import ForwardButton
from gui.Body.Header import Header
from gui.Body.LoadingBar import LoadingBar
from gui.Body.Translators import Translators
from gui.Body.FileUploader import FileUploader
from gui.Body.Selectors import Selectors
from gui.Body.TranslationLoading import TranslationLoading

class Body(QFrame):

    page=7

    def __init__(self,container):
        super().__init__(container)
        self.setFixedWidth(1280)
        self.layout=QVBoxLayout()
        self.layout.setContentsMargins(QMargins(0,0,0,0))
        self.layout.setStretch(0,0)
        self.layout.setSpacing(0)

        self.update()

        self.setLayout(self.layout)
        self.show()
        

    def update(self):
        selector=True
        if Body.page>1:
            selector=False
        self.header=Header(self,Body.page,self.previous,selector)
        self.layout.addWidget(self.header,Qt.AlignCenter,Qt.AlignCenter)
        self.forwardbutton=ForwardButton(self)
        self.forwardbutton.clicked.connect(self.next)
        self.forwardbutton.hide()

        match Body.page:
            case 1:
                self.translators=Translators(self,self.forwardbutton)
                self.layout.addWidget(self.translators,Qt.AlignCenter,Qt.AlignCenter)
            case 2:
                self.fileuploader=FileUploader(self,self.forwardbutton)
                self.layout.addWidget(self.fileuploader,Qt.AlignCenter,Qt.AlignCenter)
            case 3:
                self.loadingbar=LoadingBar(self,self.forwardbutton,1,True,"Sto estraendo le stringhe dal file...","Estrazione completata.")
                self.layout.addWidget(self.loadingbar,Qt.AlignCenter,Qt.AlignCenter)
            case 4:
                self.selectors=Selectors(self,self.forwardbutton)
                self.layout.addWidget(self.selectors,Qt.AlignCenter,Qt.AlignCenter)
            case 5:
                self.translationloading=TranslationLoading(self,self.forwardbutton,1)
                self.layout.addWidget(self.translationloading,Qt.AlignCenter,Qt.AlignCenter)
            case 6:
                self.filedownloader=FileDownloader(self,self.forwardbutton)
                self.layout.addWidget(self.filedownloader,Qt.AlignCenter,Qt.AlignCenter)
            case 7:
                self.forwardbutton=ForwardButton(self,"TORNA ALLA HOME",10,170,41)
                self.forwardbutton.clicked.connect(self.next)
                self.filedownloader=LoadingBar(self,self.forwardbutton,1,True,"Sto scrivendo la traduzione...","Traduzione completata.")
                self.layout.addWidget(self.filedownloader,Qt.AlignCenter,Qt.AlignCenter)
            # If an exact match is not confirmed, this last case will be used if provided
            case _:
                print("Page navigation error")


        self.layout.addWidget(self.forwardbutton,Qt.AlignCenter,Qt.AlignCenter)

    def next(self):
        if Body.page<7:
            Body.page+=1
        elif Body.page==7:
            Body.page=1
        self.removeAll()
        self.update()

    def previous(self):
        if Body.page>1:
            Body.page-=1
        self.removeAll()
        self.update()

    def removeAll(self):
        items = (self.layout.itemAt(i) for i in range(self.layout.count())) 
        for w in items:
            w.widget().deleteLater()
        