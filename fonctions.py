import random

def initMatrice(matrice):
    for i in range(0,10):
        ligne = []
        for j in range(0,10):
            ligne.append(random.randint(0,1))
        matrice.append(ligne)
    return matrice

def affichageMatrice(matrice):
    for i in range (0,9):
        print(matrice[i])

def testAutour(matrice):
#test le contenu des cellules voisines
    haut = 0
    bas = 0
    droite = 0
    gauche = 0
    hautDroit = 0
    hautGauche = 0
    basGauche = 0
    basDroite = 0

    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if(i == 0 or j == 0 or i == (len(matrice)-1) or j == (len(matrice))-1):
                if(i == 0 and j == 0):
                    print("En haut à gauche")
                elif(i == (len(matrice)-1) and j == (len(matrice)-1)):
                    print("En bas à droite")
                    print("rang = " + str(i) +" "+ str(j))
                elif(i == (len(matrice)-1) and j==0):
                    print("En haut à droite")
                    print("rang = " + str(i) +" "+ str(j))
                elif(i == 0 and j == (len(matrice)-1)):
                    print("En haut à droite")
                    print("rang = " + str(i) +" "+ str(j))
                elif(i == 0):
                    print("En haut")
                    print("rang = " + str(i) +" "+ str(j))
                elif(j == (len(matrice)-1)):
                    print("En bas")
                    print("rang = " + str(i) +" "+ str(j))
#            else :
#                print("Pas à coté d'un mur")
    
