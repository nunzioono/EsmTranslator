from logic.StringTranslationRecord import StringTranslationRecord

class StringTranslationMap:

    def __init__(self):
        self.values={}
        self.progressiveId=1
        self.recordsallowedtypes=["FACT","KYWD","RACE","MGEF","ENCH","SPEL","ACTI","TACT","ARMO","BOOK","CONT","DOOR","LIGH","MISC","STAT","MSTT","FLOR","FURN","WEAP","AMMO","NPC_","KEYM","ALCH","NOTE","PROJ","TERM","WRLD","REFR","QUST","INFO","WATR","FLST","PERK","LCTN","MESG","OMOD","INNR","ARMO","BOOK","ALCH","COBJ","INFO"]
        self.subrecordsallowedtypes=["FULL","FMRN","ATTX","ONAM","SHRT","UNAM","BTXT","ITXT","WNAM","NNAM","DESC"]

    def put(self,string_translation_record):
        if string_translation_record is not None and isinstance(string_translation_record, StringTranslationRecord):
            word=string_translation_record.string

            if not hasattr(self.values,word) and string_translation_record.type1 in self.recordsallowedtypes and string_translation_record.type2 in self.subrecordsallowedtypes:
                string_translation_record.id=self.progressiveId
                self.progressiveId+=1
                self.values[word]=string_translation_record
                return string_translation_record
        return None

    def get(self,word):
        if word in self.values:
            return self.values[word]
        else:
            return None
    def __str__(self):
        return "{\n"+",\n".join(["'"+prop+"'"+":'"+str(self.values[prop])+"'" for prop in self.values])+"\n}"