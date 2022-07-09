from PyQt5.QtWidgets import QFrame,QVBoxLayout, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins
from gui.Body.Header import Header
from gui.Body.Translators import Translators

class Body(QFrame):

    def __init__(self,container):
        super().__init__(container)

        self.header=Header(container)#,"back")
        self.selectionlabel=QLabel(self)
        self.translators=Translators(container)

        layout=QVBoxLayout()
        layout.setSpacing(0)
        layout.setContentsMargins(QMargins(0,0,0,0))
        layout.addWidget(self.header,Qt.AlignTop,Qt.AlignCenter)
        layout.addWidget(self.translators,Qt.AlignCenter,Qt.AlignCenter)
        self.setLayout(layout)
        self.show()