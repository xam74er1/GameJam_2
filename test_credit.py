import pygame

def triNoms():
    fichier = open("noms.txt", "r")

    NumberOfLine = 0
    for line in fichier:
        NumberOfLine += 1

    fichier.close()

    fichier = open("noms.txt", "r")
    tableau = []

    i = 0
    while i < NumberOfLine:
        tableau.append(fichier.readline().split("|"))
        i += 1
    fichier.close()

    tableau.sort()
    return tableau


def ecrireNoms(tab):
    i = 0
    while i < len(tab):
        print(tab[i][0] + " dans le rôle du " + tab[i][1])
        i += 1

tableau = triNoms()
ecrireNoms(tableau)