from sys import argv
from bethesda_structs.plugin import FNVPlugin
import re

class Extractor:

    def __init__(self, plugin_path):
        self.plugin_path=plugin_path
        self.plugin= FNVPlugin.parse_file(plugin_path)
        self.recordsallowedtypes=["FACT","WYWD","RACE","MGEF","ENCH","SPEL","ACTI","TACT","ARMO","BOOK","CONT","DOOR","LIGH","MISC","STAT","MSTT","FLOR","FURN","WEAP","AMMO","NPC_","KEYM","ALCH","NOTE","PROJ","TERM","CELL","WRLD","REFR","QUST","INFO","WATR","FLST","PERK","LCTN","MESG","OMOD","INNR","ARMO","BOOK","ALCH","COBJ","INFO"]
        self.subrecordsallowedtypes=["FULL","FMRN","DNAM","ATTX","ONAM","SHRT","UNAM","BTXT","ITXT","NAM0","WNAM","RNAM","NNAM","DESC","NAM1"]


    def findOccurrences(self, stringtofind):
        f=open(self.plugin_path, "r", encoding="Latin-1")
        text=f.read()
        occurrences=[]

        for match in re.finditer(stringtofind, text):
            occurrence=str((match.start(),match.end()))
            occurrences.append(occurrence)

        f.close()
        return occurrences

    def extract(self):
        ftotranslate=open("../data/strings.csv","w")
        dict={}

        for record in self.plugin.iter_records():
            for subrecord in record.subrecords:

                if record.type in self.recordsallowedtypes and subrecord.type in self.subrecordsallowedtypes:
                    word=str(subrecord.data)
                    word=word.rstrip('\x00').lstrip('\x00')
                    word=word[2:-1]
                    if word != "":
                        occurrences="["+",".join(self.findOccurrences(word))+"]"
                        print(word)#+","+occurrences)
                        #add traslation
                        translation=word
                        dict[word]=[occurrences,translation]

        for key in dict:
            ftotranslate.write(dict[key][0]+","+",".join(dict[key][1])+"\n")
        ftotranslate.close()


Extractor(argv[1]).extract()
