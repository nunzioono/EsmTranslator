from PyQt5.QtWidgets import QFrame,QHBoxLayout
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins
from gui.Body.Header import Header

class Body(QFrame):

    def __init__(self,container):
        super().__init__(container)

        self.header=Header(container)#,"back")

        layout=QHBoxLayout()
        layout.setContentsMargins(QMargins(0,0,0,0))
        layout.addWidget(self.header)
        self.setLayout(layout)
        self.show()