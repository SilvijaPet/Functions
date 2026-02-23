import math
import random
from statistics import mean

print("============================ 1 uzduotis =======================")
# Sukurkite Funkciją kuri priima du kintamuosius, skaičius. Juos susumuoja ir atspausdina.

def sumavimas(a,b):
    print(f"Suma: {a + b}")

sumavimas(43,7)

print("============================ 2 uzduotis =======================")
# Sukurkite Funkciją kuri vadinasi PISq.
# Funkcija gražina reikšmę. Reikšmė yra : 9.8596;
# Gautą reikšmę atspausdinkite.

def pisq():
    return 9.8596

print(pisq())

print("============================ 3 uzduotis =======================")
# Sukurkite Funkciją kuri priima du kintamuosius. Funkcija gražina skaičių sandaugą.; Gautą reikšmę atspausdinkite.

def sandauga(a,b):
    return a * b

print("Sandauga:", sandauga(5,5))

print("============================ 4 uzduotis =======================")
# Sukurkite Funkciją kuri priima masyvą, prasuka ciklą ir atspausdina visus elementus vienoje eilutėje.

def array_1(a, b, c, d):
    for i in range(3):
        print(a, b, c, d, end=" ")

array_1(1, 2, 3, 4)
print()

print("============================ 5 uzduotis =======================")
# Sukurkite Funkciją kuri sugeneruotų random skaičių masyvą ir jį gražintų.
# Funkcija priima tris kintamuosius, min, max ir length reikšmėms nustatyti.

def rnd_array(mi, ma, length):
    return [random.randint(mi, ma) for _ in range(length)]

print(rnd_array(5,10,3))

print("============================ 6 uzduotis =======================")
# Sukurkite Funkciją kuri panaudotų 5toje užduotyje sugeneruotą masyvą (priimtų kaip kintamąjį), susumuotų ir gražintų reikšmę.

def sum_rnd_array(mi, ma, length):
    array_2 = rnd_array(mi, ma, length)
    print("Sugeneruotas masyvas:", array_2)
    return sum(array_2)

print("Masyvo suma:", sum_rnd_array(5, 10, 3))

print("============================ 7 uzduotis =======================")
# Sukurkite Funkciją kuri priimtų 5toje užduotyje sugeneruotą masyvą ir gražintų jos skaičių vidurkį.

def avg_rnd_array(mi, ma, length):
    array_3 = rnd_array(mi, ma, length)
    print("Sugeneruotas masyvas:", array_3)
    return mean(array_3)

print("Masyvo vidurkis:", avg_rnd_array(5, 10, 3))


print("============================ 8 uzduotis =======================")
# Sukurkite Funkciją kuri priimtų du skaičius ir atspausdintų stačiakampį užpildytą žvaigždutėmis.
# Pirmas skaičius- išoriniam ciklui, antras vidiniam.

# def square(ilgis,plotis):
#     for i in range(ilgis):
#         print("*" * plotis)

def square(ilgis, plotis):
    for i in range(ilgis):
        for p in range(plotis):
            print("*", end="")
        print()

square(3,15)

print("============================ 9 uzduotis =======================")
# Sukurkite Funkciją kuri priimtų sakinį kaip kintamąjį ir atspausdintų kiek jame yra raidžių(simbolių) ir tarpų.
# Sakinys - “Šiandien labai graži diena”. (kodas turi veikti padavus bet kokį sakinį)
# (simboliu yra 23, tarpu yra 3)

def print_symbols_count(txt):
    count_symbols = len(txt)
    count_letters = len(txt) - txt.count(" ")
    count_space = count_symbols - count_letters
    print("Raidziu:", count_letters, "Tarpu:", count_space)

print_symbols_count("Šiandien labai graži diena")

print("============================ 10 uzduotis =======================")
# Sukurkite Funkciją kuri priimtų sakinį, jį užkoduotų ir grąžintų.
# Kodavimas - sakinį apsukame iš kitos pusės. Pvz “Naglis” turi gautis “silgaN”.

def text_revert(txt):
    return txt[::-1]

print(text_revert("Labas rytas"))

print("============================ 11 uzduotis =======================")
# Sukurti funkciją, kuri apsuka tik žodžius. “Labas rytas” -> “sabaL satyr” ir atspausdina rezultatą

def word_revert(txt):
    word = txt.split()
    for i in word:
        print(i[::-1], end=" ")
    print()

word_revert("Labas rytas")

print("============================ 12 uzduotis =======================")
# Sukurkite funkciją, kuri priimtų masyvą
# ir atspausdintų tik tuos elementus kurie yra skaičiai.

def num_array(arr):
    numbers = []
    for i in arr:
        if i.isdigit():
            numbers.append(int(i))
    print(numbers)

num_array("Vienas, 2, trys 4, sesi6")

print("============================ 13 uzduotis =======================")
# Sukurkite funkciją, kuri priima masyvą ir atspausdina tik sveikuosius skaičius.
# (jei pavyks, patobulinkite, kad funkcija priimtų antrą parametrą True/False kuris nuspręstų ar spausdins tik sveikuosius skaičius ar skaičius su kableliu.

def num_array(arr):
    numbers = []
    for i in arr:
        if i.isdigit() and int(i) % 2 == 0:
            numbers.append(int(i))
    print(numbers)

num_array("Vienas, 2, trys 4, sesi6, 1.8 5")

print("============================ 14 uzduotis =======================")
# Sukurkite funkciją word_count kuri priimtų textą ir gražintų kiek jame yra žodžių

def word_count(txt):
    return len(txt.split())

print(word_count("Labas rytas"))

print("============================ 15 uzduotis =======================")
# Sukurkite funkciją kuri priima du parametrus. Skaičių masyvą ir boolean.
# Funkcija gražina prafiltruotą masyvą. Kai antras parametras True/tik poriniais skaičiais, False/tik neporiniais skaičiais.

def filtered_arr(num, bool):
    poriniai = []
    neporiniai = []
    for i in num:
        if i % 2 == 0:
            poriniai.append(i)
        else:
            neporiniai.append(i)
    if bool:
        return poriniai
    else:
        return neporiniai
print(filtered_arr([1,2,3,4,5,6], True))
print(filtered_arr([1,2,3,4,5,6], False))

print("============================ 16 uzduotis =======================")
# Sukurkite funkciją number_is_prime. Funkcija priima skaičių, gražina True/False ar skaičius pirminis.

def number_is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

print(number_is_prime(10))

print("============================ 17 uzduotis =======================")
# Sukurkite funkciją kuri priima du argumentus. Gražina pirmąjį skaičių pakeltą laipsniu tokiu kaip antras skaičius.

def num_power(a,b):
    return a ** b

print(num_power(2,2))

print("============================ 18 uzduotis =======================")
# Sukurkite funkciją kuri priima skaičių masyvą ir gražina tik skirtingus elementus. (panašiai kaip sql distinct)

def diff_num_array(nums):
    diff_nums = []
    for n in nums:
        if n not in diff_nums:
            diff_nums.append(n)
    return diff_nums

print(diff_num_array([5,5,8,9,10,10]))

print("============================ 19 uzduotis =======================")
# Sukurkite funkciją kuri priima tekstą ir atspausdina tekste daugiausiai pasikartojantį simbolį.

def most_common_symbol(txt):
    txt = txt.lower()
    max_qty = 0
    most_common = ""
    for char in txt:
        qty = txt.count(char)
        if qty > max_qty:
            max_qty = qty
            most_common = char
    print(most_common)

most_common_symbol("Tekstas")

print("============================ 20 uzduotis =======================")
# Sukurkite funkciją kuri priima tekstą ir atspausdina jame esantį ilgiausią žodį.
