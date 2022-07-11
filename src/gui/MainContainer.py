from PyQt5.QtWidgets import QFrame, QVBoxLayout
from PyQt5.QtCore import Qt, QMargins
from gui.Navbar.Navbar import Navbar
from gui.Body.Body import Body
from gui.Footer import Footer
class MainContainer(QFrame):

    def __init__(self,parent):
        super().__init__(parent)
        self.setStyleSheet("background:#090433")

        self.navbar= Navbar(parent)
        self.body= Body(parent)
        self.footer=Footer(self)

        layout= QVBoxLayout()
        layout.setContentsMargins(QMargins(0,0,0,0))
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignTop)
        layout.addWidget(self.navbar,Qt.AlignTop)
        layout.addWidget(self.body,Qt.AlignCenter)
        layout.addWidget(self.footer,Qt.AlignBottom)
        self.setLayout(layout)

        self.show()
