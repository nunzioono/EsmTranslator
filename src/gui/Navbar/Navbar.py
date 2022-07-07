from PyQt5.QtWidgets import QFrame,QHBoxLayout, QGraphicsDropShadowEffect
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins
from gui.Navbar.Menu import Menu

class Navbar(QFrame):

    def __init__(self,container):
        super().__init__(container)
        self.draggable=True
        self.parent=container
        self.parent.oldPos = self.parent.pos()
        self.setFixedSize(1280,42)
        self.setStyleSheet("background:#4B4591;border:0px;margin:0px;padding:0px")

        self.menu=Menu(container)
        
        layout=QHBoxLayout()
        layout.setContentsMargins(QMargins(0,0,0,0))
        layout.setAlignment(Qt.AlignRight)
        layout.addWidget(self.menu,Qt.AlignRight,Qt.AlignTop)
        self.setLayout(layout)
        self.show()
        
    def mousePressEvent(self, event):
        if(event.x()<=1170):
            self.parent.oldPos = event.globalPos()
        else:
            self.draggable=False

    def mouseMoveEvent(self, event):
        if self.draggable:
            delta = QPoint (event.globalPos() - self.parent.oldPos)
            self.parent.move(self.parent.x() + delta.x(), self.parent.y() + delta.y())
            self.parent.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.draggable=True