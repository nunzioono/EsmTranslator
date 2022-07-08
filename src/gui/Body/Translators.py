from PyQt5.QtWidgets import QFrame,QHBoxLayout,QPushButton,QLabel
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins, QDir
from PyQt5.QtGui import QIcon, QPixmap
from gui.Body.Translator import Translator

class Translators(QFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.setStyleSheet("background:red")
        self.translatoractive=Translator(self)
        self.translatorunactive=Translator(self)

        layout=QHBoxLayout()
        layout.setContentsMargins(QMargins(0,0,0,0))
        layout.setSpacing(30)
        layout.addWidget(self.translatoractive)
        layout.addWidget(self.translatorunactive)
        self.setLayout(layout)

        self.show()