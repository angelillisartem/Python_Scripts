import re

def valida_telefono(telefono):
    pattern = re.compile("^[0-9\\-\\+]*$")
    return pattern.match(telefono) is not None

telefono = int(input("Inserisci numero di telefono"))

if valida_telefono(telefono):
    print("Numero telefonico valido!")
else:
    print("Numero telefonico non valido, riprova!")