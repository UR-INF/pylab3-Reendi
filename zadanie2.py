from array import *
tablica = array('u')
n = int(input("Ile znaków chcesz dodać do tablicy? "))
for i in range(n):
    tablica.append(input("Wprowadź znak "))
print("-------------------------")
print("Tablica przed odwróceniem")
print(tablica)
tablica.reverse()
print("-------------------------")
print("Tablica po odwróceniu")
print(tablica)