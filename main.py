'''
1. Feladat
Írj egy programot, amely 5 darab véletlenszámot generál [1;7] intervallumon, és ezeket eltárolja egy listában. Kérjen be a felhasználótól egy számot, és vizsgálja meg, hogy ez előfordul-e a listában! Az eredményről tájékoztassa a felhasználót, és írja ki a lista elemeit a képernyőre!
'''

import random

lista = [random.randint(1,7) for i in range(5)]
print(lista)


szam = int(input("Kérek egy számot:"))


if szam in lista:
  print("A szám benne van a listában")
else:
  print("A szám nincs benne a listában")
