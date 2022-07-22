class Writer:

    def __init__(self,path,map):
        self.path=path
        self.map=map

        text=self.readOriginalText()
        text=self.substitute(text)
        print(text)
        self.write(text)

    def readOriginalText(self):
        return open(self.path,"rb").read().decode("Latin-1")

    def substitute(self,text):
        for word in self.map.values:
            record=self.map.get(word)
            if record.translation!="":
                text.replace(record.string,record.translation)
        
        return text.encode("Latin-1")

    def write(self,text):
        path=self.path.replace(".esm","_translated.esm")
        f=open(path,"w",encoding="Latin-1")
        f.write(text)
        f.close()