import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

# imparte toate nr la 10
print(arr/10)

# aduna 5 la toate numerele
print(arr + 5)

arr2 = np.array([101, 202, 303, 404, 505, 606])

print(arr + arr2) # functioneaza doar daca ambele array uri au aceeasi lungime

# se creeaza o conditie pe baza careia filtreaza valorile 
print(arr % 3 == 0)

# concluzie
# numpy realizeaza operatii matematice foarte rapide