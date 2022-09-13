import argparse

parser = argparse.ArgumentParser()

FichierParDefaut = "default.txt"

parser.add_argument("filename",default="default.txt",help="nom du fichier a utiliser",type=str,const=FichierParDefaut,nargs="?")#a verifier
parser.add_argument("--add","-a",help="ajouter une tache a la liste",type=str)
parser.add_argument("--modify","-m",help="modifier la tache",nargs=2, type=str) ##ajouter l'ordre des arg dans le rd
parser.add_argument("--show","-s",help="montrer la liste des taches",action="store_true")

args = parser.parse_args()

def add(filename,add):
    with open (filename,"a") as fichier:
        fichier.write(add+"\n")
    with open (filename, "r") as fichier:
        var = len(fichier.readlines())
    print(var)

def modify(filename,id,text):
    with open (filename, "r") as fichier:
        lignes = fichier.readlines()
    if id <= len(lignes) and id > 0:
        lignes[id-1] = text + "\n"
        with open (filename, "w") as fichier:
            fichier.writelines(lignes)
    else:
        print("id non valide")

def TexteId(id,x):#pour eviter la répétition dans la fonction show
    texte = " " + id + " "
    while len(texte) < x:
        texte += " "    
    return texte 

def TexteDescription(description,y):#pour eviter la répétition dans la fonction show
    text = " " + description + " "
    while len(text) < y:
        text += " "   
    return text 

def show(filename):
    with open (filename,"r") as fichier:
        lignes = fichier.readlines()
        x = 2 + len(str(len(lignes)))
        y = 2
        for i in range(len(lignes)):
            if len(lignes[i]) + 2 > y:
                y = len(lignes[i]) + 2
    LigneBlanche = "+" + ("-" * x) + "+" + ("-" * y) + "+" + "\n"
    TexteAAfficher = LigneBlanche
    TexteAAfficher += ("|" + TexteId("id",x) + "|" + TexteDescription("description",y) + "|"+"\n" + LigneBlanche)
    for i in range(len(lignes)):
        TexteAAfficher += ("|" + TexteId(str(i+1),x) + "|" + TexteDescription(lignes[i][:-1],y) + "|"+"\n" + LigneBlanche)
    print(TexteAAfficher)

if args.add != None:
    try:
        add(args.filename,args.add)
    except:
        print("AddError")
if args.modify != None:
    try:
        id,text = args.modify
        id = int(id) ##car id est de type str comme text
        modify(args.filename,id,text)
    except ValueError:
        print("id non valide, veuillez indiquer id + nouvelle description de la tache")
    except:
        print("ModifyError")
if args.show:
    try:
        show(args.filename)
    except:
        print("ShowError")
