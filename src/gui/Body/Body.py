from PyQt5.QtWidgets import QFrame,QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins
from attr import has
from gui.Body.ForwardButton import ForwardButton
from gui.Body.Header import Header
from gui.Body.Translators import Translators

class Body(QFrame):

    page=1

    def __init__(self,container):
        super().__init__(container)
        self.layout=QVBoxLayout()
        self.layout.setContentsMargins(QMargins(0,0,0,0))
        self.layout.setStretch(0,0)
        self.layout.setSpacing(0)

        self.update()

        self.setLayout(self.layout)
        self.show()
        

    def update(self):
        print(Body.page)
        print(self.layout)
        self.header=Header(self,Body.page,self.previous)
        self.layout.addWidget(self.header,Qt.AlignCenter,Qt.AlignCenter)
        self.forwardbutton=ForwardButton(self)
        self.forwardbutton.clicked.connect(self.next)

        match Body.page:
            case 1:
                self.translators=Translators(self,self.forwardbutton)
                self.layout.addWidget(self.translators,Qt.AlignCenter,Qt.AlignCenter)
            case 2:
                self.translators=Translators(self,self.forwardbutton)
                self.layout.addWidget(self.translators,Qt.AlignCenter,Qt.AlignCenter)
            # If an exact match is not confirmed, this last case will be used if provided
            case _:
                print("Page navigation error")


        self.layout.addWidget(self.forwardbutton,Qt.AlignCenter,Qt.AlignCenter)

    def next(self):
        print(self.page)
        if Body.page<6:
            Body.page+=1
        self.removeAll()
        self.update()

    def previous(self):
        print(self.page)
        if Body.page>1:
            Body.page-=1
        self.removeAll()
        self.update()

    def removeAll(self):
        items = (self.layout.itemAt(i) for i in range(self.layout.count())) 
        for w in items:
            w.widget().deleteLater()
        