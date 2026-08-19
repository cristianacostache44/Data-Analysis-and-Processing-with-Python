
def fara_vocale(x):
    vocale = "aeiouAEIOU"
    string_nou = ""
    for i in x:
        if i not in vocale:
            string_nou += i
    return string_nou
    
input_string = "Salutare, ce mai faci?"
print(fara_vocale(input_string))
