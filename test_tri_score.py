import pygame

def triScore():
    fichier = open("test-score.txt", "r")
    tableau = []

    NumberOfLine = 0
    for line in fichier:
        NumberOfLine += 1

    i = 0
    while i < NumberOfLine:
        tableau.append(fichier.readline().split('|'))
        print(fichier.readline().split('|'))
        #print(tableau.append(fichier.readline().split('|')))
        i += 1
    fichier.close()

    tableau.sort(reverse=True)
    return tableau

def afficheScore(tab, val):
    i = 0
    nom = False
    if int(tab[9][0]) > val:
        while i < len(tab):
            if i < 10:
                print(str(i + 1) + " - " + tab[i][0] + "  -  " + tab[i][1])
                i += 1
            elif val >= int(tab[i][0]) and nom == False:
                print("")
                print(str(i + 1) + " - " + str(val) + "  -  " + "taper votre nom ...")
                nom = True
                i += 1
            else:
                i += 1
                print(i)
    else:
        while i < 9:
            if val >= int(tab[i][0]) and nom == False:
                print(str(i + 1) + " - " + str(val) + "  -  " + "taper votre nom ...")
                nom = True
                i -= 1
            else:
                if nom == True:
                    print(str(i + 2) + " - " + tab[i][0] + "  -  " + tab[i][1])
                else:
                    print(str(i + 1) + " - " + tab[i][0] + "  -  " + tab[i][1])
            i += 1


#tableau = triScore()
#afficheScore(tableau, 2)
