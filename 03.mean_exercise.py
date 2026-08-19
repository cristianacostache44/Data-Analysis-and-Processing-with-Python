
def mean_func(x):
    suma = 0
    n = 0
    for i in x:
        suma += i
        n += 1
    return suma/n

lista = [10, 2, 30, 50, 300, 10]
print(mean_func(lista))