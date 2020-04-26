import random
from array import *
tablica = array('d')
for i in range(10):
    tablica.append(random.uniform(-5, 5))
file = open("result.txt", "w")
file.write(str(tablica))
file.close()