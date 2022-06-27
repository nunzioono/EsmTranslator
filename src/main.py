from StringTranslationMap import StringTranslationMap
from Extractor import Extractor
from Translator import Translator
#from Writer import Writer
from sys import argv
import json

map=StringTranslationMap()
path=argv[1]
text=open("../data/translators.json").read()
avaiable_translators=json.loads(text)
choice=0
src_lang="EN"
target_lang="IT"

Extractor(path,map)
Translator(avaiable_translators,map,choice,src_lang,target_lang)
#Writer(path,map)