from PyQt5.QtWidgets import QFrame,QVBoxLayout
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins
from gui.Body.Header import Header
from gui.Body.Translators import Translators

class Body(QFrame):

    def __init__(self,container):
        super().__init__(container)

        self.header=Header(container)#,"back")
        self.translators=Translators(container)

        layout=QVBoxLayout()
        layout.setSpacing(30)
        layout.setContentsMargins(QMargins(0,0,0,0))
        layout.addWidget(self.header)
        layout.addWidget(self.translators)
        self.setLayout(layout)
        self.show()