import numpy as np
a = np.array([[2,3,4,5,6],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0],
             [0,0,0,0,0]
             ], dtype=np.float64)
#Wyświetla w typie 64 bitowym, ponieważ inaczej jest overflow
for i in range(1,5):
    for j in range(5):
        a[i][j]=a[i-1][j]*a[i-1][j]

print(a)