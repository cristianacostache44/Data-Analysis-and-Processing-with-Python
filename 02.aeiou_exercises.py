
def fara_vocale(x):
    vocale = "aeiouAEIOU"
    string_nou = ""
    for i in x:
        if i not in vocale:
            string_nou += i
    return string_nou
    
input_string = "Salutare, ce mai faci?"
print(fara_vocale(input_string))

vocale = "aeiouAEIOU"
filter_result = list(filter(lambda i: i not in vocale, input_string))
print(filter_result)

from functools import reduce

reduce_result = reduce(lambda x, y: x + y, filter(lambda i: i not in vocale, input_string))
print(reduce_result)