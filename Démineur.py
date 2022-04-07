
#-------------------------------------------------------------------------------
# Name:        Démineur Py
# Purpose:
#
# Author:      Nicolas Becharat-Salacroup
#
# Created:     10/02/2022
# Copyright:   (c) NBS 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import *
import time
from datetime import datetime

# the function returns a dictionary with for key: a tuple which contains the coordinates
# and to value the content of the box

nomJoueur = input ("Quel est votre pseudo ? ")



def créa_dico (n, i, Bomb):
    #the function créa_dico returns a dictionary with for key : a tuple which contains the coordinates and for value the content of the cell. This dictionary returns the game array with values n
    liste = []
    for abscisse in range (1,n+1):
        for ordonnée in range (1,n+1):
            liste.append((abscisse, ordonnée))

    dico = {}
    for valeur in liste :
        dico[valeur] = [0,-3, 0, 0]
    coordonnéesUtilisées =[]
    if i == 1 :
      for test in range(Bomb) :
        abscisse = randint(1,9)
        ordonnée = randint(1,9)
        while (abscisse,ordonnée) in coordonnéesUtilisées:
            abscisse = randint(1,9)
            ordonnée = randint(1,9)
        coordonnéesUtilisées.append((abscisse,ordonnée))
        dico[abscisse,ordonnée]=[-1, -3, 0, 0]
    elif i == 0 :
          for valeur in liste :
                dico[valeur] = -3
    return (dico)


# VeCaseChoisi function checks if the coordinates of the chosen case are in the table
def VeCaseChoisi(abscisse,ordonnée):
  if ((abscisse <= 10) and (abscisse >= 1)) and ((ordonnée <= 10) and (ordonnée >= 1)):
    pass
  else:
    print("LA CASE", abscisse,",",ordonnée, "N'EXISTE PAS")





def jeu (tableau):
    finish = 0
    while finish != 1:
            print("--------------------------")
            abscisse = int(input("Entrer l'abscisse de la case "))
            ordonnée = int(input("Entrer l'ordonnée de la case "))
            print("--------------------------")
            action = input("Entrer d  pour dévoilez la case, taper  f  pour poser un drapeau, ou l'enlever ")

            valeurs = tableau[abscisse, ordonnée]
            if action == "d" and valeurs[1] == -3:
                valeurs[1] = -4
                if (abscisse <= 9) and (abscisse >= 2) and (ordonnée <= 9) and (ordonnée >= 2): # Calcul pour enlever les 0 dans une zone de 9 cases
                    if tableau[abscisse + 1, ordonnée][0] ==0:
                        tableau[abscisse + 1, ordonnée][1] = -4
                    if tableau[abscisse - 1, ordonnée][0] == 0:
                        tableau[abscisse - 1, ordonnée][1] = -4
                    if tableau[abscisse - 1, ordonnée - 1][0] == 0:
                        tableau[abscisse - 1, ordonnée - 1][1] = -4
                    if tableau[abscisse + 1, ordonnée + 1][0] ==0:
                        tableau[abscisse + 1, ordonnée + 1][1] = -4
                    if tableau[abscisse, ordonnée - 1][0] == 0:
                        tableau[abscisse, ordonnée - 1][1] = -4
                    if tableau[abscisse, ordonnée + 1][0] == 0:
                        tableau[abscisse, ordonnée + 1][1] = -4
                    if tableau[abscisse - 1, ordonnée + 1][0] == 0:
                        tableau[abscisse - 1, ordonnée + 1][1] = -4
                    if tableau[abscisse + 1, ordonnée - 1][0] == 0:
                        tableau[abscisse + 1, ordonnée - 1][1] = -4
                elif ordonnée == 1 and abscisse == 1:
                    if tableau[abscisse + 1, ordonnée][0] == 0:
                        tableau[abscisse + 1, ordonnée][1] = -4
                    if tableau[abscisse , ordonnée +1][0] == 0:
                        tableau[abscisse , ordonnée +1][1] = -4
                    if tableau[abscisse+1, ordonnée +1][0] == 0:
                        tableau[abscisse+1, ordonnée +1][1] = -4
                elif ordonnée == 1 and abscisse > 1 and abscisse < 10:
                    if tableau[abscisse + 1, ordonnée][0] == 0:
                        tableau[abscisse + 1, ordonnée][1] = -4
                    if tableau[abscisse - 1 , ordonnée ][0] ==0:
                        tableau[abscisse - 1 , ordonnée ][1] = -4
                    if tableau[abscisse + 1, ordonnée + 1][0] == 0:
                        tableau[abscisse + 1, ordonnée + 1][1] = -4
                    if tableau[abscisse, ordonnée + 1][0] == 0:
                        tableau[abscisse, ordonnée + 1][1] = -4
                    if tableau[abscisse - 1, ordonnée + 1][0] ==0:
                        tableau[abscisse - 1, ordonnée + 1][1] = -4
                elif ordonnée == 10 and abscisse > 1 and abscisse < 10:
                    if tableau[abscisse + 1, ordonnée][0] == 0:
                        tableau[abscisse + 1, ordonnée][1] = -4
                    if tableau[abscisse - 1 , ordonnée ][0] == 0:
                        tableau[abscisse - 1 , ordonnée ][1] = -4
                    if tableau[abscisse + 1, ordonnée - 1][0] == 0:
                        tableau[abscisse + 1, ordonnée - 1][1] = -4
                    if tableau[abscisse, ordonnée - 1][0] ==0:
                        tableau[abscisse, ordonnée - 1][1] = -4
                    if tableau[abscisse - 1, ordonnée - 1][0] == 0:
                        tableau[abscisse - 1, ordonnée - 1][1] = -4
                elif abscisse == 10 and ordonnée > 1 and ordonnée < 10:
                    if tableau[abscisse, ordonnée + 1][0] == 0:
                        tableau[abscisse, ordonnée + 1][1] = -4
                    if tableau[abscisse, ordonnée - 1 ][0] == 0:
                        tableau[abscisse, ordonnée - 1 ][1] = -4
                    if tableau[abscisse - 1, ordonnée + 1][0] == 0:
                        tableau[abscisse - 1, ordonnée + 1][1] = -4
                    if tableau[abscisse - 1, ordonnée][0] == 0:
                        tableau[abscisse - 1, ordonnée][1] = -4
                    if tableau[abscisse - 1, ordonnée - 1][0] == 0:
                        tableau[abscisse - 1, ordonnée - 1][1] = -4
                elif abscisse == 1 and ordonnée > 1 and ordonnée < 10:
                    if tableau[abscisse, ordonnée + 1][0] == 0:
                        tableau[abscisse, ordonnée + 1][1] = -4
                    if tableau[abscisse, ordonnée - 1 ][0] == 0:
                        tableau[abscisse, ordonnée - 1 ][1] = -4
                    if tableau[abscisse + 1, ordonnée + 1][0] == 0:
                        tableau[abscisse + 1, ordonnée + 1][1] = -4
                    if tableau[abscisse + 1, ordonnée][0] == 0:
                        tableau[abscisse + 1, ordonnée][1] = -4
                    if tableau[abscisse + 1, ordonnée - 1][0] == 0:
                        tableau[abscisse + 1, ordonnée - 1][1] = -4
                elif abscisse == 10 and ordonnée==1:
                    if tableau[abscisse, ordonnée + 1][0] == 0:
                        tableau[abscisse, ordonnée + 1][1] = -4
                    if tableau[abscisse - 1, ordonnée][0] == 0:
                        tableau[abscisse - 1, ordonnée][1] = -4
                    if tableau[abscisse - 1, ordonnée + 1][0] == 0:
                        tableau[abscisse - 1, ordonnée + 1][1] = -4
                elif abscisse == 10 and ordonnée==10:
                    if tableau[abscisse, ordonnée - 1][0] == 0:
                        tableau[abscisse, ordonnée - 1][1] = -4
                    if tableau[abscisse - 1, ordonnée-1][0] == 0:
                        tableau[abscisse - 1, ordonnée-1][1] = -4
                    if tableau[abscisse - 1, ordonnée - 1][0] == 0:
                        tableau[abscisse - 1, ordonnée - 1][1] = -4

                elif abscisse == 1 and ordonnée==10:
                    if tableau[abscisse, ordonnée - 1][0] == 0:
                        tableau[abscisse, ordonnée - 1][1] = -4
                    if tableau[abscisse + 1, ordonnée-1][0] == 0:
                        tableau[abscisse + 1, ordonnée-1][1] = -4
                    if  tableau[abscisse + 1, ordonnée][0] == 0:
                        tableau[abscisse + 1, ordonnée][1] = -4


                break


            elif action == "d" and valeurs[1] == -4:
                print ("La case selectionné a déja été dévoilée")
                finish = 1

            if action == "f" and valeurs[2] == 0:
                valeurs[2] = 1
                break

            if action == "f" and valeurs[2] == 1:
                valeurs[2] = 0
                break


def CalculMine(abscisse,ordonnée):
    if tableau[abscisse, ordonnée] != -1:
        if (abscisse <= 9) and (abscisse >= 2) and (ordonnée <= 9) and (ordonnée >= 2):
            MineAutour = tableau[abscisse + 1, ordonnée][0] + tableau[abscisse - 1, ordonnée][0] + tableau[abscisse - 1, ordonnée - 1][0] + tableau[abscisse + 1, ordonnée + 1][0] + tableau[abscisse, ordonnée - 1][0] + tableau[abscisse, ordonnée + 1][0] + tableau[abscisse - 1, ordonnée + 1][0] + tableau[abscisse + 1, ordonnée - 1][0]
            return(abs(MineAutour))  # Displays the absolute value of the number of mines around the selected Case
        elif ordonnée == 1 and abscisse == 1:
            MineAutour =  tableau[abscisse + 1, ordonnée][0] + tableau[abscisse , ordonnée +1][0] + tableau[abscisse+1, ordonnée +1][0]
            return(abs(MineAutour))
        elif ordonnée == 1 and abscisse > 1 and abscisse < 10:
            MineAutour =  tableau[abscisse + 1, ordonnée][0] + tableau[abscisse - 1 , ordonnée ][0] + tableau[abscisse + 1, ordonnée + 1][0] + tableau[abscisse, ordonnée + 1][0]  + tableau[abscisse - 1, ordonnée + 1][0]
            return(abs(MineAutour))
        elif ordonnée == 10 and abscisse > 1 and abscisse < 10:
            MineAutour =  tableau[abscisse + 1, ordonnée][0] + tableau[abscisse - 1 , ordonnée ][0] + tableau[abscisse + 1, ordonnée - 1][0] + tableau[abscisse, ordonnée - 1][0]  + tableau[abscisse - 1, ordonnée - 1][0]
            return(abs(MineAutour))
        elif abscisse == 10 and ordonnée > 1 and ordonnée < 10:
            MineAutour =  tableau[abscisse, ordonnée + 1][0] + tableau[abscisse, ordonnée - 1 ][0] + tableau[abscisse - 1, ordonnée + 1][0] + tableau[abscisse - 1, ordonnée][0]  + tableau[abscisse - 1, ordonnée - 1][0]
            return(abs(MineAutour))
        elif abscisse == 1 and ordonnée > 1 and ordonnée < 10:
            MineAutour =  tableau[abscisse, ordonnée + 1][0] + tableau[abscisse, ordonnée - 1 ][0] + tableau[abscisse + 1, ordonnée + 1][0] + tableau[abscisse + 1, ordonnée][0]  + tableau[abscisse + 1, ordonnée - 1][0]
            return(abs(MineAutour))
        elif abscisse == 10 and ordonnée==1:
            MineAutour =  tableau[abscisse, ordonnée + 1][0] + tableau[abscisse - 1, ordonnée][0] + tableau[abscisse - 1, ordonnée + 1][0]
            return(abs(MineAutour))
        elif abscisse == 10 and ordonnée==10:
            MineAutour =  tableau[abscisse, ordonnée - 1][0] + tableau[abscisse - 1, ordonnée-1][0] + tableau[abscisse - 1, ordonnée - 1][0]
            return(abs(MineAutour))
        elif abscisse == 1 and ordonnée==10:
            MineAutour =  tableau[abscisse, ordonnée - 1][0] + tableau[abscisse + 1, ordonnée-1][0] + tableau[abscisse + 1, ordonnée][0]
            return(abs(MineAutour))
    else:  # if Case chosen is -1 in the table
        return (-1)
    return


def tableau_finale (tableau, n):
    stop = "p"
    while n == 0 :
        a = 0
        while stop == "p":
            n = win(tableau)
            jeu (tableau)
            print ("------------------grille démineur ----------------")
            print ("|  - - - - - - - - - - - - - - - - - - - - - - - | \n| -    | 1   2   3   4   5   6   7   8   9   10  |")

            for i in range (1, 11):
                ordonnée = i
                print ("|",end=' ')
                if i< 10:
                    print (i,""," ", "|", end=' ')
                elif i == 10:
                    print (i," ", "|", end=' ')
                for n in range (1,11):
                    abscisse = n
                    valeurs = tableau[abscisse, ordonnée]
                    valeurs[3] = CalculMine(abscisse,ordonnée)
                    if valeurs[1] == -4:
                        if valeurs[0] == -1:
                            print ("@"," ",end=' ')
                            a = 1
                        elif valeurs[3] == 0:
                            print ("_"," ",end=' ')
                        elif valeurs[3] == 1 or valeurs[3] ==2 or valeurs[3] ==3 or valeurs[3] ==4 or valeurs[3] ==5 or valeurs[3] ==6 or valeurs[3] ==7 or valeurs[3] ==8:
                            print (valeurs[3]," ", end=' ')
                    if valeurs[1] == -3:

                        if valeurs[2] == 0:
                            print ("."," ",end=' ')

                        if valeurs[2] == 1:
                            print ("#"," ",end=' ')


                print ("|")
            casesNonDev=0
            for abs in range(1,11):
             for ord in  range(1,11):
               Val=tableau[abs,ord]
               if Val[1]==-4:
                  casesNonDev+=1
            if casesNonDev==100-NbrMines:
              stop = "s"
              n = 1
              print ("          _          _             _ \n\
 __   __ (_)   ___  | |_    ___   (_)  _ __    ___   \n\
 \ \ / / | |  / __| | __|  / _ \  | | | '__|  / _ \  \n\
  \ V /  | | | (__  | |_  | (_) | | | | |    |  __/  \n\
   \_/   |_|  \___|  \__|  \___/  |_| |_|     \___|  ")
              heureFin = datetime.now() 
              timeFinal = heureFin - heureDebut #Calculation of final time for game time          
              print("FIN DE LA PARTIE, GAGNE EN", timeFinal)
              print("----------------------")
              donnees[0]+=1
              if donnees[2]==0 or donnees[2]>timeFinal:
                donnees[2]=timeFinal
              recommencer2 = input("Voulez vous recommencer si oui tapez  oui  ")
              if recommencer2 =="oui": 
                  print(question)
              else : 
                   exit() #stop the code --> exit
            if a == 1 :
                    stop = "s"
                    n = 1
                    print (" ____  ____  ____  _        _  _  _ \n\
/  __\/  _ \/  _ \/ \__/|  / \/ \/ \ \n\
| | //| / \|| / \|| |\/||  | || || | \n\
| |_\\\| \_/|| \_/|| |  ||  \_/\_/\_/ \n\
\____/\____/\____/\_/  \|  (_)(_)(_)  ")
                    heureFin = datetime.now()
                    timeFinal = heureFin - heureDebut
                    
                    print("FIN DE LA PARTIE, PERDU EN", timeFinal)
                    print("----------------------")
                    donnees[1]+=1
                    recommencer2 = input("Voulez vous recommencer si oui tapez  oui  ") #returns you to the menu to start the game again 
                    if recommencer2 =="oui": 
                        print(question)
                    else : 
                        exit() 
def win(tableau):
    compteur = 0
    for i in range (1, 11):
                ordonnée = i
                for n in range (1,11):
                    abscisse = n
                    val = tableau[abscisse, ordonnée]

    if val[0] == 0 and val[1] == -3:
        compteur += 1

    if compteur == 80 :
        win = 1
        n = 1

    else :
        win = 0

    if win == 1:
        print ("          _          _             _ \n\
 __   __ (_)   ___  | |_    ___   (_)  _ __    ___   \n\
 \ \ / / | |  / __| | __|  / _ \  | | | '__|  / _ \  \n\
  \ V /  | | | (__  | |_  | (_) | | | | |    |  __/  \n\
   \_/   |_|  \___|  \__|  \___/  |_| |_|     \___|  ")
        heureFin = datetime.now()
        timeFinal = heureFin - heureDebut
        print("FIN DE LA PARTIE, VICTOIRE EN", timeFinal)
        print("----------------------")
        donnees[0]+=1
        if donnees[2]==0 or donnees[2]>timeFinal:
          donnees[2]=timeFinal
        if input(print("voulez-vous recommencer?"))=="o":
          return
    else : 
        exit() 
        
        

#__________________________________________________________________
#START OF THE PARENT PROGRAM

def menu ():
    print("-------------------------------------------------") 
    print("LANCER PARTIE | REGLES DU JEU | CREDIT | STATISTIQUES | QUITTER | JOUEUR :",nomJoueur, )
    print("-----------------------------------------------------------")
donnees=[0,0,0]#dictionary for statistics 
while 1 == 1:
  menu()
  question = input("Que voulez vous faire ? ")




  if question == "lancer partie" : #refers to the launch of the game 
      recommencer = 0
      recommencer = "s"

      if recommencer == "s" :
          heureDebut =datetime.now()
          
          
          NbrMines=0
          while not (NbrMines<=99 and NbrMines>0): ##As long as the number of mines is less than or equal to 99 and greater than 0     
            NbrMines=int(input("Combien voulez vous de mines ? "))
            print(nomJoueur, "veux", NbrMines, "mines")
          heureDebut =datetime.now() 
          print("Le jeu commence maintenant")   
          tableau=créa_dico(10, 1, NbrMines)
          tableau_affichage = créa_dico (10, 0, NbrMines)
          n = 0
        
          tableau_finale (tableau, n)
          if recommencer == "t":
              exit()
            
  if question == "regles du jeu"  : #refers to the rules of the game
      print("----------------------------------------------------------")
      print('                  LES REGLES DU JEU')
      print("----------------------------------------------------------")
      print(nomJoueur,", le but du jeu est de découvrir toutes les cases libres \nsans faire exploser les mines, c'est à dire sans toucher \nles cases quiles dissimulent. Lorsque le joueur clique\nsur une case libre comportant au moins une mine dans \nl'une de ses cases avoisinantes, un chiffre apparait, \nindiquant ce nombre de mine.")
      exit() 
    
  if question == "credit": #refers to credit
      print("----------------------------")
      print('          CREDIT')
      print("----------------------------")
      print ('Nicolas')
      exit()


    

  if question == "quitter" : 
      print("Au revoir",nomJoueur)
      exit()



  if question == "statistiques" : 
    print("Nombre de parties jouées: ", donnees[0] + donnees[1])
    print("Nombre de parties gagnées: ", donnees[0])
    print("Nombre de parties perdues: ", donnees[1])
    if donnees[0]+donnees[1]!= 0:
      print("Pourcentage de victoire: ", (donnees[0])/(donnees[0]+donnees[1])*100,"%")
    print("Meilleur temps: ", donnees[2])
    5