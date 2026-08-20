
def mean_func(x):
    suma = 0
    n = 0
    for i in x:
        suma += i
        n += 1
    return suma/n

lista = [10, 2, 30, 50, 300, 10]
print(mean_func(lista))

from functools import reduce

def suma_nr(x, y):
    return x + y

reduce_result = int(reduce(suma_nr, lista))
print(reduce_result/len(lista))