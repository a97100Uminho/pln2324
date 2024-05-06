import re
from gensim.models import Word2Vec 
from gensim.utils import tokenize
import os 

print("Diretório atual:", os.getcwd())

with open("Harry_Potter_Camara_Secreta-br.txt", "r", encoding="utf-8") as f1:
    harry_text_1 = f1.read()

with open("Harry_Potter_e_A_Pedra_Filosofal.txt", "r", encoding="utf-8") as f2:
    harry_text_2 = f2.read()


harry_text = harry_text_1 + "\n" + harry_text_2

linhas = harry_text.split("\n")

tokens = []
for linha in linhas:
    #linha = re.sub(r'[-!?.,]',"", linha)
    linha = list(tokenize(linha, lower=True))
    tokens.append(linha)

model = Word2Vec(tokens, vector_size= 300, window= 5, min_count= 1, epochs= 20)

print(model.wv.most_similar("harry"))

"""
[['this', 'is', 'the', 'first', 'sentence', 'for', 'word2vec'],
			['this', 'is', 'the', 'second', 'sentence'],
			['yet', 'another', 'sentence'],
			['one', 'more', 'sentence'],
			['and', 'the', 'final', 'sentence']]
"""




