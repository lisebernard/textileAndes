import os

#script pour récupérer les noms des images du répertoire dans un document txt

def noms_images_txt(repertoire, nom_document):
    contenu = ""

    if not os.path.isdir(repertoire):
        print("Le répertoire spécifié n'existe pas.")
        return

    fichiers = sorted(os.listdir(repertoire))
    for fichier in fichiers:
        chemin_fichier = os.path.join(repertoire, fichier)
        if os.path.isfile(chemin_fichier):
            contenu += f"{fichier}\n"

    try:
        with open(nom_document, "w") as fichier_txt:
            fichier_txt.write(contenu)
        print(f"Le document '{nom_document}' a été créé avec succès.")
    except IOError:
        print("Une erreur s'est produite lors de l'écriture du document.")