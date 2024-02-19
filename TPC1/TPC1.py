#10

filename = '../../data/CHI Bilingual Medical Glossary R«English-Spanish.txt'

file = open(filename)
text = file.read()

text = text.replace('.', ' ').replace(',', ' ').replace('-', ' ')

tokens = [word.lower() for word in text.split()]

def areAnagrams(str1, str2):
    
    return sorted(str1) == sorted(str2)

def findAnagrams(tokens):
    return [(tokens[i], tokens[j]) for i in range(len(tokens)) for j in range(i + 1, len(tokens)) if areAnagrams(tokens[i], tokens[j])]

anagramPairs = findAnagrams(tokens)
print(anagramPairs)


