from sys import argv
from bethesda_structs.plugin import FNVPlugin
import re
import time

class Extractor:

    def __init__(self, plugin_path):
        self.plugin_path=plugin_path
        self.plugin= FNVPlugin.parse_file(plugin_path)
        self.recordsallowedtypes=["FACT","WYWD","RACE","MGEF","ENCH","SPEL","ACTI","TACT","ARMO","BOOK","CONT","DOOR","LIGH","MISC","STAT","MSTT","FLOR","FURN","WEAP","AMMO","NPC_","KEYM","ALCH","NOTE","PROJ","TERM","CELL","WRLD","REFR","QUST","INFO","WATR","FLST","PERK","LCTN","MESG","OMOD","INNR","ARMO","BOOK","ALCH","COBJ","INFO"]
        self.subrecordsallowedtypes=["FULL","FMRN","DNAM","ATTX","ONAM","SHRT","UNAM","BTXT","ITXT","NAM0","WNAM","RNAM","NNAM","DESC","NAM1"]

    def getProgressPercentage(self, iteratorindex, recordlenght):
        rawpercentage= (iteratorindex/recordlenght)*100
        percentage=round(rawpercentage,2)
        return percentage

    def joinToString(self, list):
        stringtoreturn="["
        for item in list:
            stringtoreturn+=item+","
        
        stringtoreturn=stringtoreturn[:-1]
        stringtoreturn+="]"
        return stringtoreturn

    def findOccurrences(self, stringtofind):
        f=open(self.plugin_path, "r", encoding="Latin-1")
        text=f.read()
        escaped=re.escape(stringtofind)
        occurrences=[]

        for match in re.finditer(escaped, text):
            if match.group(0) != "":
                occurrence=str((match.start(),match.end()))
                occurrences.append(occurrence)

        f.close()
        return occurrences

    def extract(self):
        ftotranslate=open("../data/strings.csv","w")
        dict={}
        recordlenght=0

        for record in self.plugin.iter_records():
            recordlenght+=record.data_size

        iteratorindex=0
        progress=0
        starttime=time.time()

        for record in self.plugin.iter_records():

            progress=self.getProgressPercentage(iteratorindex, recordlenght)
            moment=time.time()
            elapsedtime=moment-starttime
            elapsedtime=round(elapsedtime,1)
            if(elapsedtime%0.5==0):
                print("Progress: "+str(progress)+"%")

            for subrecord in record.iter_subrecords():

                if record.type in self.recordsallowedtypes and subrecord.type in self.subrecordsallowedtypes:
                    extract=subrecord.data.decode("Latin-1")
                    word=str(extract)
                    word=word.strip("\x00")
                    if word != "" and dict[word] == None:
                        occurrences=self.findOccurrences(word)
                        occurencesstring=self.joinToString(occurrences)
                        #TODO: translate the word
                        translation=word
                        dict[word]=[translation,record.type+"->"+subrecord.type,occurencesstring]

            iteratorindex+=record.data_size

        for key in dict:
            ftotranslate.write(dict[key][0]+","+self.joinToString(dict[key][1])+"\n")
        ftotranslate.close()


Extractor(argv[1]).extract()
