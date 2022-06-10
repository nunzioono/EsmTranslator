from sys import argv
from bethesda_structs.plugin import FNVPlugin

class Extractor:

    def __init__(self, plugin_path):
        self.plugin= FNVPlugin.parse_file(plugin_path)

    def extract(self):
        fdatradurre=open("../data/strings.csv","w")

        for record in self.plugin.iter_records():
            for subrecord in record.subrecords:
                
                typeformat=record.type+"->"+subrecord.type
                righttype=False

                for listedtype in self.lines:
                    if typeformat in listedtype:
                        righttype=True
                        break

                if righttype:
                    fdatradurre.write(str(record.type)+"->"+str(subrecord.type)+","+str(subrecord.data)+"\n")


        fdatradurre.close()


Extractor(argv[1]).extract()
