class StringTranslationRecord:

    def __init__(self, type1= "", type2= "", string= "", string_size= 0, translation= "", translation_size= 0, occurrencies= [], num_occurrencies= 0):
        self.id=-1
        self.type1=type1
        self.type2=type2
        self.string=string
        self.string_size=string_size
        self.translation=translation
        self.translation_size=translation_size
        self.occurrencies=occurrencies
        self.num_occurrencies=num_occurrencies

    def __str__(self):
        return "{"+",".join(["'"+str(attr)+"'"+":"+"'"+str(prop)+"'" for attr,prop in self.__dict__.items()])+"}"