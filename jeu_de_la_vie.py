# coding: UTF-8 
""" 
Script: jeu_de_la_vie/main
Création: le 20/02/2023
"""
# Imports 
import random
# Fonctions 
import fonctions
# Programme principal 
def main():
    
    matrice = []
    TAILLE = 10

#INITIALISATION Matrice

    matrice = fonctions.initMatrice(matrice)
    fonctions.affichageMatrice(matrice)

    fonctions.testAutour(matrice)


if __name__ == '__main__':
    main()
    # Fin

