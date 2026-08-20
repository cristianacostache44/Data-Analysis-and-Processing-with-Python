import numpy as np

arr = np.array([2, 3, 4, 5, 6.23])
print(arr) # arr contine un float - > sunt tranformate toate in float
print(type(arr))
arr = np.array([2, 3, 4, 5, 6.23, 'string'])
print(arr) # arr contine un string - > sunt transformate toate in string

# in python putem tranforma un nr in baza 2 cu urmatoarea functie
a = 2
print(bin(a)) # 0b10 --- 0b e doar prefixul

for i in range(10):
    print("i=", i, "in baza 2 =", bin(i)[2:]) # [2:] taie 0b de la inceput

# cu 8 bits de date se poate scrie 1 byte ( 1 octet in romana )
# 8 bits = 1 byte adica daca reprezentam 2 in baza 2 ar fi 00000010 
# cel mai mare numar care poate fi reprezentat pe 8 biti este 255 = 2 ** (8(biti) -1) = 1111 1111

# arr = np.array([2, 3, 4, 5, 6, 255], dtype=np.int8)
# print(arr)
# ----- OverflowError: Python integer 255 out of bounds for int8

# uint8 = unsidned pe 8 bits de date: de la -128 pana la 127
# int8 = signed(cu semn) pe 8 bits de date de la 127
arr = np.array([2, 3, 4, 5, 6, 255], dtype=np.uint8)
print(arr)