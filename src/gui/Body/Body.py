from PyQt5.QtWidgets import QFrame,QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins
from gui.Body.ForwardButton import ForwardButton
from gui.Body.Header import Header
from gui.Body.Translators import Translators

class Body(QFrame):

    def __init__(self,container):
        super().__init__(container)

        self.header=Header(self)#,"back")
        self.selectionlabel=QLabel(self)
        self.forwardbutton=ForwardButton(self)
        self.translators=Translators(self,self.forwardbutton)

        self.layout=QVBoxLayout()
        self.layout.setContentsMargins(QMargins(0,0,0,0))
        self.layout.setStretch(0,0)
        self.layout.setSpacing(0)
        self.layout.addWidget(self.header,Qt.AlignCenter,Qt.AlignCenter)
        self.layout.addWidget(self.translators,Qt.AlignCenter,Qt.AlignCenter)
        self.layout.addWidget(self.forwardbutton,Qt.AlignCenter,Qt.AlignCenter)
        self.setLayout(self.layout)
        self.show()