from sys import argv
from bethesda_structs.plugin import FNVPlugin 
import re
import concurrent.futures
from bs4 import BeautifulSoup
from StringTranslationRecord import StringTranslationRecord
from StringTranslationMap import StringTranslationMap

class Extractor:

    def __init__(self, plugin_path):
        self.plugin_path=plugin_path
        self.plugin=FNVPlugin.parse_file(self.plugin_path)
        self.plugin= self.plugin.parse_file(plugin_path)

        self.StringTranslationMap=StringTranslationMap()
        self.createMap()
        self.populateMap()
        self.pruneMap()


    def getProgressPercentage(self, iteratorindex, recordlenght):
        rawpercentage= (iteratorindex/recordlenght)*100
        percentage=round(rawpercentage,1)
        return percentage

    def createMap(self):
        f=open("../data/mapping.csv","w")
        frewriting=open("../data/rewriting.csv","w")
        progressiveId=1


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
                    print(word)
                    words=word.split("<")
                    print("----------------------------------")
                    print(words)
                    for newword in words:
                        if newword!="" and newword[0:1]!="/" and ">" in newword:
                        #set finalword to the substring of word starting at the index of >
                            finalword=word[word.index(">")+1:]
                            record=StringTranslationRecord(progressiveId,type1,type2,finalword,len(finalword),"",0,[],0)
                            progressiveId+=1
                            f.write(str(self.StringTranslationMap[word])+"\n")

                if word != "" and not re.match("[^\x00-\x7F]+",word) and not hasattr(self.StringTranslationMap, word) and type1 in self.recordsallowedtypes and type2 in self.subrecordsallowedtypes:
                    record=StringTranslationRecord(progressiveId,type1,type2,word,len(word),"",0,[],0)
                    progressiveId+=1
                    f.write(str(self.StringTranslationMap[word])+"\n")
        f.close()

    def populateMap(self):

        #open the file read text
        with open(self.plugin_path, "rb") as file:
            text=file.read()
            text=text.decode("Latin-1")
        #check for each word if it is in the text
        
            for word in self.StringTranslationMap:
        
        #if it is add an occourrence
                if word in text:
                    escaped=re.escape(word)
                    for match in re.finditer(escaped, text):
                        if match.group(0) != "":
                            occurrence=str((match.start(),match.end()))
                            self.StringTranslationMap[word]["occurrencies"].append(occurrence)
                            self.StringTranslationMap[word]["num_occurrencies"]=len(self.StringTranslationMap[word]["occurrencies"])

        #if not pass
                else:
                    pass

            file.close()

    def pruneMap(self):
        orderedMap=sorted(self.StringTranslationMap, key=lambda k: self.StringTranslationMap[k]["size_string"], reverse=False)

    def todo(self, word):
        actualprogress=self.getProgressPercentage(iteratorindex, "recordlenght")
        if actualprogress != progress:
            print("Progress: "+str(actualprogress)+"%")
            progress=actualprogress

        executor=concurrent.futures.ThreadPoolExecutor(max_workers=self.maxthreads)
        # Start the load operations and mark each future with its URL
        futuretodict = {executor.submit(self.extractRecord, dict, "record", subrecord):  subrecord for subrecord in "record".subrecords}
        for future in concurrent.futures.as_completed(futuretodict):
            iteratorindex+=futuretodict[future].data_size


Extractor(argv[1])

