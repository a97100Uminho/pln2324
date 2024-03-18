import re 
import json 
from deep_translator import GoogleTranslator

file = open("c:/Users/liama/OneDrive/Ambiente de Trabalho/dicionario_medico.txt")
texto = file.read()

#limpar documento
texto = re.sub(r'<text.+?>', r'', texto)
texto = re.sub(r'</text>', r'', texto)

#texto = re.sub(r'</?text.*>', r'', texto)

texto = re.sub(r'</?page.*?>', r'', texto)
texto = re.sub(r'</?pdf2xml.*?>', r'', texto)

#extrair conceitos 
#conceitos = re.findall(r'<b>(.+)</b>', texto)
#conceitos = re.findall(r'</b>(.+)<b>', texto)
#conceitos = re.findall(r'<?b>(.*)</b>\n([\s\S]+?)\n+<', texto)
conceitos = re.findall(r'<b>(.+)</b>\n([^<]+)', texto)

print(texto)



novos_conceitos = []
for designacao, descricao in conceitos:
    nova_designacao = designacao.strip()
    nova_descricao = descricao.strip()
    novos_conceitos.append((nova_designacao, nova_descricao))


conceitos_dicti = dict(conceitos)

conceitos_dicti = {designacao.strip() : descricao.strip() for designacao, descricao in conceitos}


#aula5

file_livro = open("../../data/livrinho.txt")
texto = file_livro.read()

file_conceitos = open("conceitos.json")
texto = file_conceitos.read()
conceitos = json.loads(texto)
conceitosmin = {chave.lower(): conceitos[chave] for chave in conceitos}

blacklist = ["e", "de", "para", "pelo", ]

conceitos_min = {chave.lower(): conceitos[chave] for chave in conceitos} #SAI NO TESTE
    
translate = GoogleTranslator(source='pt', target='en')

def translateword(word):
    return translate.translate(word)

def etiquetador(matched):
    palavra = matched[0] 
    original = palavra.lower()
    

    if palavra in conceitos and palavra not in blacklist: 
        descricao = conceitos[palavra]
        translate = translateword(palavra)
        descricao = re.sub(r"<br>\s*",r"", descricao)

        etiqueta = f"<a href='' title='{descricao}'>{designacao}</a>"
        return etiqueta
    else: 
        return original



expressao = r'[\wáéçâóõéíêâú]'
texto = re.sub(expressao, etiquetador, texto)
texto = re.sub(r'\n,', r'<br>', texto)
texto = re.sub(r'\f', r'<hr>', texto)



file_out = open('conceitos.json', 'w')
json.dump(conceitos_dicti, file_out, indent = 4)
file_out.close()


