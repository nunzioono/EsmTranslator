from StringTranslationMap import StringTranslationMap
from Extractor import Extractor
from Translator import Translator
from Writer import Writer
from sys import argv

map=StringTranslationMap()
path=argv[1]
avaiable_translators=[]
url=""
api_key=""
translator=()
avaiable_translators.append(translator)

Extractor(path,map)
Translator(avaiable_translators,map)
Writer(path,map)