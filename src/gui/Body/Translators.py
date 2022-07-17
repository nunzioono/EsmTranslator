from PyQt5.QtWidgets import QFrame,QHBoxLayout,QPushButton,QLabel
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins, QDir
from PyQt5.QtGui import QIcon, QPixmap
from gui.Body.Translator import Translator

class Translators(QFrame):

    def __init__(self,parent,forwardbutton):
        super().__init__(parent)
        self.setFixedSize(480,220)

        self.translatoractive=Translator(self,True,forwardbutton)
        self.translatorunactive=Translator(self,False,forwardbutton)


        layout=QHBoxLayout()
        layout.setStretch(0,0)
        layout.setContentsMargins(QMargins(0,0,0,0))
        layout.addWidget(self.translatoractive)
        layout.addWidget(self.translatorunactive)
        self.setLayout(layout)

        self.show()

    def getTranslators(self):
        return self.translatoractive.getTranslators()