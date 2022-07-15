from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from gui.Body.ForwardButton import ForwardButton

class FileDownloader(QWidget):

    CARICATO=False
    FILE_PATH=""

    def __init__(self,parent,forwardbutton):
        super().__init__(parent)
        self.forwardbutton=forwardbutton
        self.layout=QGridLayout()

        self.update()
        
        self.setLayout(self.layout)
        self.show()

    def update(self):

        if not FileDownloader.CARICATO:
            self.setContentsMargins(70,0,0,0)
            
            self.border=QLabel(self)
            self.border.setPixmap(QPixmap(QDir.currentPath()+"/gui/assets/Bordo.png"))

            self.label=QLabel(self)
            font=QFont("Noto sans",12)
            font.setBold(True)
            self.label.setFont(font)
            self.label.setText("""Seleziona una cartella nella quale trasferire
la traduzione del file:""")
            self.label.setAlignment(Qt.AlignCenter)
            
            self.label.setStyleSheet("""QLabel{
                color:white;
            }""")

            self.selectbutton=ForwardButton(self,"SELEZIONA CARTELLA",10,170,41)
            self.selectbutton.clicked.connect(self.selectfolder)

            self.layout.addWidget(self.border,0,0,64,64)
            self.layout.addWidget(self.label,20,15,10,30)
            self.layout.addWidget(self.selectbutton,35,25,10,10)

            self.forwardbutton.hide()
        else:
            self.setContentsMargins(180,0,0,0)
            
            self.border=QLabel(self)
            self.border.setPixmap(QPixmap(QDir.currentPath()+"/gui/assets/Bordo.png"))

            self.folder=QLabel(self)
            self.folder.setPixmap(QPixmap(QDir.currentPath()+"/gui/assets/Folder.png"))

            self.label=QLabel(self)            
            font=QFont("Noto sans",12)
            font.setBold(True)
            self.label.setFont(font)
            self.label.setText("""Il file verra trascritto con la traduzione nella cartella:
'"""+FileDownloader.FILE_PATH+"""'""")
            self.label.setAlignment(Qt.AlignCenter)
            self.label.setStyleSheet("""QLabel{
                color:white;
            }""")

            self.returnbutton=QPushButton(self)
            font.setUnderline(True)            
            self.returnbutton.setFont(font)
            self.returnbutton.setText("""Intendevi trascrivere in un'altra cartella?
""")
            self.returnbutton.setStyleSheet("""QPushButton{
                color:#7974B3;
                border:none;
            }""")
            self.returnbutton.clicked.connect(self.invert)

            self.layout.addWidget(self.border,0,0,64,64)
            self.layout.addWidget(self.folder,15,23,10,10)
            self.layout.addWidget(self.label,30,13,10,23)
            self.layout.addWidget(self.returnbutton,45,12,10,25)

            self.forwardbutton.show()

    def invert(self):
        FileDownloader.CARICATO=not FileDownloader.CARICATO
        self.removeAll()
        self.update()

    def removeAll(self):
        items = (self.layout.itemAt(i) for i in range(self.layout.count())) 
        for w in items:
            w.widget().deleteLater()

    def selectfolder(self):
        fname = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if fname!="":
            FileDownloader.FILE_PATH=fname
            self.invert()