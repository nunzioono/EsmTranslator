import requests
import json

class Translator:

    def __init__(self,avaiable_translators,map,choice,source_lan,dest_lan):
        self.source_lan=source_lan
        self.dest_lan=dest_lan
        self.choosentranslator=avaiable_translators[choice]
        self.map=map

        for key in self.map.values:
            record=self.map.values[key]
            record.translation=self.translate(record.string)

        f=open("../data/translations.csv","w")
        for key in self.map.values:
            f.write(str(self.map.get(key))+"\n")
        f.close()

    def translate(self,text):
        headers={
            "Content-Type": "application/json",
            "Host": "api-free.deepl.com",
            "Accept": "*/*"
        }
        response=requests.post(self.choosentranslator['url']+"/v2/translate?auth_key="+self.choosentranslator['api_key']
        +"&text="+text
        +"&source_lang="+self.source_lan
        +"&target_lang="+self.dest_lan
        +"&tag_handling=html",headers=headers)
        text=response.text
        jsonresponse=json.loads(text)
        translation=""
        if "translations" in jsonresponse:
            translation=jsonresponse['translations'][0]['text']
        print(jsonresponse)
        return translation