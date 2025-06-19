# Ex. 1: Creaza functii de calcul aritmetic, + - * /, add,
# subtract, etc, si efectueaza urmatoarele calcule:

# 100 - 300 + (7 * 80) / 2
# 7 - 8 + 3 * 4 / 10
# Inmulteste toate numerele de la 1 la 100

# Ex 2:
# Primind doua liste de date, de genul:
# [ 'Matei', 'Luca', 'Ana', 'Gabriel' ]
# [ 10, 20, 30, 15 ]
# Creaza o lista de dictionare, unde un element de dictionar arata:
# d = {
#     "Nume": "Matei",
#     "Varsta": 10
# }

# Ex 3:
# Primind lista: [10, 20, 80, 56, 2342, 5453, 7, 8 ,9]
# Folosind map(), ridica toate numerele la puterea a 2-a
# Creaza folosind filter() o lista cu toate nr pare din prima lista.

# def add(x, y):
#     return x + y
#
# def subtract (x, y):
#     return x - y
#
# def multiply(x, y):
#     return x * y
#
# def divide (x, y):
#     return x / y
#
# def power (x, y):
#     x ^ y
#
# result1 = subtract(100, add (300, divide(multiply(7, 80),2)))
# result2 = subtract(7, multiply(add( 8, 3), divide(4, 10)))
# print(result1)
# print(result2)
#
#
#
# for i in range (1, 100):
#     i *= i
# print(i)
#
#
#
#
# lst1 = [ 'Matei', 'Luca', 'Ana', 'Gabriel' ]
# lst2 = [ 10, 20, 30, 15 ]
#
# unk = list(zip(lst1, lst2))
# print(unk)
#
# lst3 = [10, 20, 80, 56, 2342, 5453, 7, 8 ,9]
#
# pwr = list(map(lambda x: x ** 2, lst3))
# print(pwr)
#
# ev_numb = list(filter(lambda x: x % 2 == 0, lst3))
# print(ev_numb)

# 1. Ai un dicționar cu prețuri ale unor produse. Folosește map și lambda pentru a mări toate prețurile cu 10%.
#
# produse = {'mere': 3.5, 'pere': 4.2, 'banane': 2.8}
#   Folosește map pentru a crea un nou dicționar cu prețurile mărite
#   Rezultat: {'mere': 3.85, 'pere': 4.62, 'banane': 3.08}
#
# def prcent (item):
#     pret, fruct = item
#
#     return pret, float(fruct) * 1.10
#
# pret_nou = list(map(prcent, produse.items()))
# print(pret_nou)

# 2. Ai un dicționar cu notele unor elevi. Folosește filter și lambda pentru a păstra doar elevii care au nota >= 7.

# note = {'Ana': 9, 'Mihai': 6, 'Ioana': 8, 'George': 5}
#
# # # Folosește filter pentru a reține doar elevii cu note peste 7
# # # Rezultat: {'Ana': 9, 'Ioana': 8}
#
# note2 = list(filter(lambda x: x[1] >= 7, note.items()))
# print(note2)

# 3.Ai un dicționar cu nume și vârste. Folosește filter și lambda
# pentru a obține doar numele persoanelor majore (>=18 ani).

# varste = {'Andrei': 17, 'Maria': 21, 'Vlad': 16, 'Elena': 19}

# major = list(filter(lambda x: x[1] > 18, varste.items()))
# print(major)

# 4. Ai un dicționar cu temperaturi în Celsius. Folosește map și lambda pentru a le converti în Fahrenheit.
# Formula: F = C * 9/5 + 32


# produse = {'mere': 3.5, 'pere': 4.2, 'banane': 2.8}
#
# produse_m = dict(map(lambda x: (x[0], x[1] * 1.10), produse.items()))
# print(produse_m)















































