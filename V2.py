# name:FORLER based on Mr. McNally's code
# date: 2020 - 04 - 10
# description: Text-based adventure game

import random
import time

def displayIntro():
    print("Jésus lui dit: ")
    print("Je te le dis en vérité, cette nuit même, avant que le coq chante, tu me renieras trois fois.")
    print("Pierre lui répondit: ")
    print("")
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("Quelle serait ta réponse? 1 Le doute ou 2 la confiance en la parole ? (1 ou 2): ")

    return path

def checkPath(chosenPath):
    print(" Comment serait-ce possible Seigneur ?")
    time.sleep(2)
    print("Quand il me faudrait mourir avec toi, je ne te renierai pas.")
    time.sleep(2)
    print("Et tous les disciples dirent la même chose.")
    print()
    time.sleep(2)

    correctPath = 1
  #  correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("Ils allèrent ensuite dans un lieu appelé Gethsémané, et Jésus dit à ses disciples:")
        print("Asseyez-vous ici, pendant que je prierai.")
    else:
        print(" Peu importe ton choix. Cela se produira.")

#Bon ensuite il s'agit simplement de rajouter des boucles mais il est 2H00 donc bonne nuit tout le monde (oui je n'ai pas pu veiller, pas même une heure ^^")


playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # choice is equal to "1" or "2"
    playAgain = input("Veux tu continuer à jouer? (y or n)")
    
