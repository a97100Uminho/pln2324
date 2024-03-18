import json
import re
from deep_translator import GoogleTranslator


translate = GoogleTranslator(source='pt', target='en')
filein = open('conceitos.json', 'r', encoding='utf-8')
dict = json.load(filein)


novodict = {}

for designacao, description in dict.items():
    en_translate = translate.translate(designacao)
    print(en_translate)
    novodict[designacao] = {
                        "des": description,
                        "en": en_translate
                        }

fileout = open('result_ficheiro.json', 'w')
json.dump(novodict, fileout, ensure_ascii=False, indent=4)

filein.close()
fileout.close()