# coding: UTF-8 
""" 
Script: jeu_de_la_vie/main
Création: le 20/02/2023
"""
# Imports 
import random
# Fonctions 

# Programme principal 
def main():
    i = 0
    j = 0
    TAILLE = 10
    tab = [[0]*TAILLE] * TAILLE
    for i in range(0,9):
        print(tab[i])
    print("\n")

if __name__ == '__main__':
    main()
    # Fin

