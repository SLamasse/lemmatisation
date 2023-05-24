import spacy_udpipe
import fonctions
import pandas as pd


lang = input("Quel model de langue souhaitez vous utiliser ? \n")


for k,v in fonctions.langues.items():
    b = True
    if lang == v:
        print("Vous avez séléctionné "+ k)
        break
    else:
        b = False

if b == False:
    print(fonctions.langues)



spacy_udpipe.download(lang) # download model
nlp = spacy_udpipe.load(lang)

fichier = input("Donner le nom du texte avec l'extension que vous souhaitez lemmatiser : ")

try :
    f = open(fichier, "r")
    texte = f.read() 
    doc = nlp(texte)
    toks = list()
    for token in doc:
        toks.append([token.text, token.lemma_, token.pos_, token.dep_])
    res = pd.DataFrame(toks, columns=['Forme', 'Lemme','POS', 'dep'])
    res.to_csv("resultat.csv", sep=";") 
except FileNotFoundError:
    print('Sorry the file we\'re looking for doesn\' exist')
    exit()

