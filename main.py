#Írj programot, mely beolvas két egész számot, és kiírja a képernyőre a nagyobbikat!

szam1 = int(input("Írd be az eslő számot!"))
szam2 = int(input("Írd be a második számot!"))

if szam1 < szam2:
  print(szam2)
else:
  print(szam1)