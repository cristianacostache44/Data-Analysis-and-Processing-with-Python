
# --- programare functionala - functiile pot fi pasate ca parametru

print("hello")
x = print
x("hello din x")
x = 10
del x

# --- pasarea functiilor ca si parametru

def adunare(x, y):
    return x + y

def scadere(x, y):
    return x - y

def inmultire(x, y):
    return x * y

for operatie in [adunare,scadere,inmultire]:
    print("Rezultatul", operatie, "este:", operatie(10,2))

def executa_operatia(operatie, t1, t2):
    return operatie(t1,t2)
print(executa_operatia(adunare, 2, 3))
print(executa_operatia(inmultire, 20, 3))

# --- functie anonima - lambda

def ridicare_la_putere(x, y):
    return x ** y

lambda_ridicare_la_putere = lambda x, y : x**y          # --- nu mai este anonima daca este atribuita
print(lambda_ridicare_la_putere(2,3))

print(executa_operatia(lambda x, y: x/y, 4, 2))         # --- folosire corecta 

# --- MAP
# --- Unde este folosita map

# --- varianta clasica
orase = ["Milano", "Bucuresti", "Barcelona", "Cluj", "Londra"]
lungime_orase = [ len(i) for i in orase]
print(lungime_orase)

# --- varianta cu map
def functie_de_mapare(x):
    return len(x)

print(list(map(functie_de_mapare, orase)))
print(list(map(len, orase)))                             # --- varianta corecta

# --- exemplu map in jocul boltz (numerele care l contin sau sunt multiplu de 7 trebuie inlocuite cu boltz)

def mapeaza_boltz(x):
    if x % 7 == 0 or "7" in str(x):
        return "boltz"
    return x

print(list(map(mapeaza_boltz, range(1,101))))           # --- trece prin toate valorile si aplica functia respectiva (o iterare - for)


# --- FILTER --- trebuie sa returneze TRUE sau FALSE

orase = ["Milano", "Bucuresti", "Barcelona", "Cluj", "Londra"]

def filter_orase_cu_b(x:str):
    return x.startswith("B")

print(list(filter(filter_orase_cu_b, orase)))

def mai_mic_decat_6(x):
    return len(x) < 6

print(list(filter(mai_mic_decat_6, orase)))

print(list(filter(lambda x: x.endswith("a"), orase)))   # --- lambda tine locul unei functii care returneaza orasele care se termina in a

# --- REDUCE

from functools import reduce

def suma_numerelor(x, y):
    print("x=", x, "y=", y)
    return x + y

lista = range(2,6)
print(reduce(suma_numerelor, lista))

print(reduce(lambda x, y: x if x > y else y, lista))