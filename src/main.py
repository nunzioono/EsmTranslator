from logic.StringTranslationMap import StringTranslationMap
from logic.Extractor import Extractor
from logic.Translator import Translator
from logic.Writer import Writer
from sys import argv
import json
from gui.MainWindow import MainWindow
from PyQt5.QtWidgets import QApplication

app = QApplication([])
window = MainWindow()
app.exec()
#map=StringTranslationMap()
#path=argv[1]
#text=open("../data/translators.json").read()
#avaiable_translators=json.loads(text)
#choice=0
#src_lang="EN"
#target_lang="IT"

#Extractor(path,map)
#Translator(avaiable_translators,map,choice,src_lang,target_lang)
#Writer(path,map)