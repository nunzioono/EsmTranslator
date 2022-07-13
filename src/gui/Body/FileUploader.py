from PyQt5.QtWidgets import QFrame, QGridLayout, QLabel, QWidget, QPushButton, QFileDialog
from PyQt5.QtGui import QFont, QIcon, QPixmap, QFont
from PyQt5.QtCore import Qt, QPoint, QSize, QMargins, QDir
from gui.Body.ForwardButton import ForwardButton

class FileUploader(QWidget):

    #default is False
    CARICATO=False
    FILE_PATH=""
    FILE_NAME=""

    def __init__(self,parent,forwardbutton):
        super().__init__(parent)
        self.forwardbutton=forwardbutton
        self.setContentsMargins(150,0,0,0)
        self.layout=QGridLayout()
        self.update()

        self.setLayout(self.layout)
        self.show()
        self.setAcceptDrops(True)
    
    def update(self):

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
            self.selectbutton.clicked.connect(self.selectfile)

            self.layout.addWidget(self.border,0,0,16,16)
            self.layout.addWidget(self.label,4,1,8,10)
            self.layout.addWidget(self.selectbutton,10,5,2,2)

        else:
            self.label=QLabel(self)
            self.label.setText('''"'''+FileUploader.FILE_NAME+'''"
            Caricato.''')
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
            self.button.setStyleSheet("""QPushButton{
                color:#595493;
                border:none;
                }""")
            self.button.clicked.connect(self.invert)

            self.label2=QLabel(self)
            self.label2.setPixmap(QPixmap(QDir.currentPath()+"/gui/assets/FileIcon.png"))

            self.layout.addWidget(self.border,0,0,16,16)
            self.layout.addWidget(self.label,5,7,3,2)
            self.layout.addWidget(self.button,7,7,3,2)
            self.layout.addWidget(self.label2,6,5,3,2)
            self.forwardbutton.show()

    def invert(self):
        FileUploader.CARICATO=not FileUploader.CARICATO
        self.removeAll()
        self.update()

    def removeAll(self):
        items = (self.layout.itemAt(i) for i in range(self.layout.count())) 
        for w in items:
            w.widget().deleteLater()
    
    def selectfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Bethesda files (*.esm *.esp)")
        if fname[0]!="":
            FileUploader.FILE_PATH=fname[0]
            FileUploader.FILE_NAME=fname[0][FileUploader.FILE_PATH.rfind("/")+1:]
            self.invert()

    def dragEnterEvent(self, event):
        print(event)
        print(event.mimeData().text())
        file_path=event.mimeData().text()
        file_extension=file_path[file_path.rfind("."):]
        if file_extension==".esm" or file_extension==".esp":
            FileUploader.FILE_PATH=file_path
            FileUploader.FILE_NAME=FileUploader.FILE_PATH[FileUploader.FILE_PATH.rfind("/")+1:]
            event.accept()
        else:
            event.ignore()
        return super().dragEnterEvent(event)

    def dropEvent(self, event):
        self.invert()
        return super().dropEvent(event)