from PyQt5.QtWidgets import QFrame, QVBoxLayout
from PyQt5.QtCore import Qt, QMargins
from gui.Navbar.Navbar import Navbar
from gui.Body.Body import Body

class MainContainer(QFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.setStyleSheet("background:#090433")

        self.navbar= Navbar(parent)
        self.body= Body(parent)

        layout= QVBoxLayout()
        layout.setContentsMargins(QMargins(0,0,0,0))
        layout.setSpacing(50)
        layout.setAlignment(Qt.AlignTop)
        layout.addWidget(self.navbar)
        layout.addWidget(self.body)
        self.setLayout(layout)

        self.show()
