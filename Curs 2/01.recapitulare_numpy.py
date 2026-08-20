# biblioteca numpy se importa astfel 

import numpy as np

# cream un array cu ajutorul numpy

arr = np.array([2, 3, 4, 5, 10])
print(arr.dtype) 

# dtype vine de la data type
# printeaza int64 

print(arr - 2)

# mai sus scade 2 din fiecare element al arrayului

print(arr.sum())

# printeaza suma elementelor, sub forma de functie proprie

print(arr.mean())

# la fel se intampla si cu media aritmetica

# ---- GENERAREA NUMERELOR RANDOM CU NUMPY

print(np.random.random())
print(np.random.randint(1, 10))

# de ce folosim asta si nu modulul clasic random? deoarece putem selecta size ul

print(np.random.randint(1, 10, 3)) # returneaza un array cu 3 elemente random
print(np.random.randint(1, 10, (3,2))) # returneaza o matrice de 3 randuri si 2 coloane
print(np.random.randint(1, 10, (5,4))) # returneaza o matrice de 5 randuri si 4 coloane

# ---- GENERAREA NUMERELOR CONSECUTIVE CU NUMPY

print(np.array(range(10)))
print(np.arange(10))

print(np.arange(10, 100))

# ---- OPERATII MATEMATICE DE NUMPY

new_arr = arr + 1       # operatie matematica cu un scalar
print(new_arr)

new_arr2 = np.zeros(10)
new_arr3 = np.ones(10)

print (new_arr2 * new_arr3 )
print (new_arr2 + new_arr3 )
print (new_arr3 - new_arr2 )

# ---- OPERATII LOGICE DE NUMPY

print (arr > 2 )
