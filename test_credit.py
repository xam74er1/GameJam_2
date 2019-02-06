import pygame, sys

# ecrire dans un fichier
reponse = input("Votre Nom :") # lit ce que tape le clavier dans le terminal
fichier = open("data.txt", "w") # w ecrase l'ancien fichier, a ecrie a la fin du fichier
fichier.write(reponse)
fichier.close()


# lire dans un fichier
fichier = open("data.txt", "r")
print(fichier.read())
fichier.close()


