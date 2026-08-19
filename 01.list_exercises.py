
def more_than_five(lista):
    lista_noua = []
    for i in lista:
        if len(str(i)) > 5:
            lista_noua.append(i)
    return lista_noua 

lista = [10, 2, 3712700, 50, 300 ,1002000]
print(more_than_five(lista))