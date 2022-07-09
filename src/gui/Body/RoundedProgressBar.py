from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class RoundedProgressBar(QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setFixedSize(220,220)
        self.show()

    def paintEvent(self, event):
        print("I got invoked!")
        qp = QPainter()
        qp.begin(self)
        color=QColor(121,116,179)
        qp.setPen(color)
        brush=QBrush()
        brush.setColor(color)
        brush.setStyle(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawArc(0,0,200,200,16*-30,16*240)
        qp.drawArc(20,20,160,160,16*-30,16*240)
        qp.drawArc(12,135,20,20,16*-135,16*180)
        qp.drawArc(168,135,20,20,16*135,16*180)
        qp.end()