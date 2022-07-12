from PyQt5.QtWidgets import QFrame, QGridLayout, QLabel, QWidget, QPushButton
from PyQt5.QtGui import QFont, QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins, QDir
from gui.Body.ForwardButton import ForwardButton

class FileUploader(QWidget):

    #default is False
    CARICATO=True

    def __init__(self,parent):
        super().__init__(parent)
        self.update()

        self.setLayout(self.layout)
        self.show()

    
    def update(self):

        self.setContentsMargins(180,0,0,0)
        self.border=QLabel(self)
        self.border.setFixedSize(800,300)
        self.border.setPixmap(QPixmap(QDir.currentPath()+"/gui/assets/Bordo.png"))

        if not FileUploader.CARICATO:
            
            self.label=QLabel(self)
            self.label.setText("""Trascina qui un file con estensione ".esm",".esp" o un altro formato supportato da Bethesda

    oppure

    """)
            font=QFont("Noto sans",11)
            font.setBold(True)
            self.label.setFont(font)
            self.label.setStyleSheet("color:white")
            self.label.setAlignment(Qt.AlignCenter)

            self.selectbutton=ForwardButton(self,"SELEZIONA FILE",10)
            
            self.layout=QGridLayout()
            self.layout.addWidget(self.border,0,0,16,16)
            self.layout.addWidget(self.label,4,1,8,10)
            self.layout.addWidget(self.selectbutton,10,5,2,2)
        else:

            self.label=QLabel(self)
            self.label.setText(""""SS2_XPAC_Chapter2.esm"
Caricato.
""")
            font=QFont("Noto sans",10)
            font.setBold(True)
            self.label.setFont(font)
            self.label.setStyleSheet("color:white")
            self.label.setAlignment(Qt.AlignCenter)

            self.button=QPushButton(self)
            self.button.setText("""Intendevi caricare un'altro file?""")
            font=QFont("Noto sans",10)
            font.setBold(True)
            font.setUnderline(True)
            self.button.setFont(font)
            self.button.setStyleSheet("color:#595493")
            self.button.clicked.connect(self.invert)

            self.label3=QLabel(self)
            self.label3.setPixmap(QPixmap(QDir.currentPath()+"/gui/assets/FileIcon.png"))

            self.layout=QGridLayout()
            self.layout.addWidget(self.border,0,0,16,16)
            self.layout.addWidget(self.label,6,7,3,2)
            self.layout.addWidget(self.button,7,7,3,2)
            self.layout.addWidget(self.label3,6,5,3,2)

    def invert(self):
        FileUploader.CARICATO=not FileUploader.CARICATO
        self.removeAll()
        self.update()

    def removeAll(self):
        items = (self.layout.itemAt(i) for i in range(self.layout.count())) 
        for w in items:
            w.widget().deleteLater()