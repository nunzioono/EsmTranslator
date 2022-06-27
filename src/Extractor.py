from bethesda_structs.plugin import FNVPlugin 
import re
from bs4 import BeautifulSoup
from StringTranslationRecord import StringTranslationRecord
from StringTranslationMap import StringTranslationMap

class Extractor:

    def __init__(self, plugin_path,string_translation_map):
        self.plugin_path=plugin_path
        self.plugin=FNVPlugin.parse_file(self.plugin_path)
        self.plugin= self.plugin.parse_file(plugin_path)

        self.StringTranslationMap=string_translation_map
        self.createMap()
        self.populateMap()
        self.pruneMap()

    def createMap(self):

        for record in self.plugin.iter_records():
            type1=record.type
            for subrecord in record.subrecords:
                type2=subrecord.type
                extract=subrecord.data.decode("Latin-1").strip("\x00")
                word=str(extract)
                countminus=word.count("<")
                if countminus!=0 and countminus%2==0 :
                    #TODO fix for tag rewriting after translation
                    soup=BeautifulSoup(word,"html.parser")
                    word=soup.get_text()
                    #split the word using < as delimiter
                    words=word.split("<")
                    for newword in words:
                        if newword!="" and newword[0:1]!="/" and ">" in newword:
                        #set finalword to the substring of word starting at the index of >
                            finalword=word[word.index(">")+1:]
                            record=StringTranslationRecord(type1,type2,finalword,len(finalword),"",0,[],0)
                            self.StringTranslationMap.put(record)
                elif "\r" in word:
                    finalwords=word.split("\r\n")
                    for finalword in finalwords:
                        if len(finalword)>1:
                            record=StringTranslationRecord(type1,type2,finalword,len(finalword),"",0,[],0)
                            self.StringTranslationMap.put(record)
                elif word != "" and not re.match("[^\x00-\x7F]+",word) and len(word)>1:
                    record=StringTranslationRecord(type1,type2,word,len(word),"",0,[],0)
                    if record!=None:
                        returned_record=self.StringTranslationMap.put(record)                    

    def populateMap(self):

        #open the file read text
        with open(self.plugin_path, "rb") as file:

            text=file.read()
            text=text.decode("Latin-1")

            #check for each word if it is in the text
        
            for key in self.StringTranslationMap.values.keys():
                #if it is add an occourrence
                if key in text:
                    escaped=re.escape(key)
                    for match in re.finditer(escaped, text):
                        if match.group(0) != "":
                            occurrence=(match.start(),match.end())
                            record=self.StringTranslationMap.get(key)
                            if record != None:
                                record.occurrencies.append(occurrence)
                                record.num_occurrencies=len(self.StringTranslationMap.get(key).occurrencies)
                #if not pass
                else:
                    pass

            file.close()

    def pruneMap(self):
        orderedMap=[]
        max=0
        for val in self.StringTranslationMap.values:
            if self.StringTranslationMap.values[val].string_size>max:
                max=self.StringTranslationMap.values[val].string_size
        
        for lenght in range(1,max):
            for key in self.StringTranslationMap.values:
                record=self.StringTranslationMap.values[key]
                if record.string_size == lenght:
                    orderedMap.append(record)
        
        #Inizio il pruning...")
        for index,value in enumerate(orderedMap):
            key=value.string
            #Cerco di fare pruning di: "+key)
            for index2 in range(0,len(orderedMap)):
                if index!=index2 and value.string in orderedMap[index2].string:
                    #La chiave *"+key+"* è contenuta in *"+orderedMap[index2].string+"*")
                    occtodelete=[]
                    #trovare l'occorrenza di value che è contenuta in una di value2
                    for index3,occ in enumerate(value.occurrencies):
                        for occ2 in orderedMap[index2].occurrencies:
                            if occ[0]>=occ2[0] and occ[1]<=occ2[1]:
                                #Una nuova occorrenza da eliminare "+str(occ))
                                occtodelete.append(index3)
                                break
                    
                    if len(occtodelete)>0:
                        #Procedo con le eliminazioni...")
                        #rimuovere quell'occorrenza
                        for dele in range(len(occtodelete),0,-1):
                            del value.occurrencies[dele]
                    #else: print("Nessuna occ da eliminare")
                    occtodelete=[]
