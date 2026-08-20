import numpy as np

start_date = 1999
end_date = 2026

lista_ani = np.arange(start_date, end_date)

# printarea anilor dintre start date si end date

print("------LISTA ANILOR------")
print(lista_ani)
print("------------------------")

# printarea anilor BISECTI dintre start date si end date

print("------LISTA ANILOR BISECTI------")
print(lambda x: x in lista_ani and (x % 400 == 0) or (x % 4 == 0 and x % 100 != 0 ))
print("--------------------------------")