from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import math

class RoundedProgressBar(QWidget):

    def __init__(self,parent,consume=0,limit=500000):
        super().__init__(parent)
        self.consume=consume
        self.limit=limit
        self.setFixedSize(220,220)
        self.show()

    def paintEvent(self, event):
        print("I got invoked!")
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        color=QColor(121,116,179)
        pen=QPen(color, 15, cap=Qt.RoundCap)
        qp.setPen(pen)
        brush=QBrush()
        brush.setColor(color)
        brush.setStyle(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawArc(8,20,180,180,16*-30,16*240)
        color2=QColor(43,85,252)
        pen2=QPen(color2, 15, cap=Qt.RoundCap)
        qp.setPen(pen2)
        alenght=math.floor(self.consume/self.limit*240)
        print(alenght)
        astart=210-alenght
        qp.drawArc(8,20,180,180,16*astart,16*alenght)
        qp.end()