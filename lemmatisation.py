import spacy_udpipe
import fonctions
import re
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
    lem = list()
    for token in doc:
        toks.append([token.text, token.lemma_, token.pos_, token.dep_])
        lem.append(token.lemma_)
        
    res = pd.DataFrame(toks, columns=['Forme', 'Lemme','POS', 'dep'])
    res.to_csv("resultat.csv", sep=";") 
    res_lem = " ".join(lem)
    res_lem = re.sub(r"\*\s+\*\s+\*\s\*\s", r"\n**** ", res_lem)    
    
    outnom = fichier.split(".")[0] + "_lem.txt"
    output = open(outnom, "w")
    output.write(res_lem)
    output.close()
    
except FileNotFoundError:
    print('Sorry the file we\'re looking for doesn\' exist')
    exit()

