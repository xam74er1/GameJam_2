import pygame

val = 6

def triScore():
    fichier = open("test-score.txt", "r")
    tableau = []
    i = 0
    while i < 14:
        tableau.append(fichier.readline().split('|'))
        i+=1
    fichier.close()

    tableau.sort(reverse=True)
    return tableau


tab = triScore()

#j = 0
#while j < 10:
    #print(str(j+1)+" - "+tab[j][0]+"  -  "+tab[j][1])
    #j +=1


#test
i=0
while i in tab:
    if val > tab[i][0]:
        print("oui")
    else:
        print("non")
    i+=1
    print(i)