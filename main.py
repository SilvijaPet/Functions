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

def num_array(arr_1):
    numbers = []
    for i in arr_1:
        if i.isdigit():
            numbers.append(int(i))
    print(numbers)

num_array("Vienas, 2, trys 4, sesi6")

print("============================ 13 uzduotis =======================")
# Sukurkite funkciją, kuri priima masyvą ir atspausdina tik sveikuosius skaičius.
# (jei pavyks, patobulinkite, kad funkcija priimtų antrą parametrą True/False kuris nuspręstų ar spausdins tik sveikuosius skaičius ar skaičius su kableliu.

def num_array(arr_2, tik_sveiki=True):
    for numm in arr_2:
        if tik_sveiki:
            if isinstance(numm, int):
                print(numm)
        else:
            if isinstance(numm, float):
                print(numm)

print("Tik sveiki:")
num_array([1, 2, 3, 4, 5, 6, 1.8, 5, -5, "tekstas"] , True)

print("Tik su kableliu:")
num_array([1, 2, 3, 4, 5, 6, 1.8, 5, -5, "tekstas"] , False)


print("============================ 14 uzduotis =======================")
# Sukurkite funkciją word_count kuri priimtų textą ir gražintų kiek jame yra žodžių

def word_count(txt):
    return len(txt.split())

print(word_count("Labas rytas"))

print("============================ 15 uzduotis =======================")
# Sukurkite funkciją kuri priima du parametrus. Skaičių masyvą ir boolean.
# Funkcija gražina prafiltruotą masyvą. Kai antras parametras True/tik poriniais skaičiais, False/tik neporiniais skaičiais.

def filtered_arr(nummm, bool):
    poriniai = []
    neporiniai = []
    for i in nummm:
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

def number_is_prime(num_):
    if num_ <= 1:
        return False
    for i in range(2, int(math.sqrt(num_))+1):
        if num_ % i == 0:
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

def longest_word(txt):
    txt = txt.split()
    longest = ""
    for word in txt:
        if len(word) > len(longest):
            longest = word
    print(longest)

longest_word("Iesokm ilgiausio zodzio sakinyje")

print("============================ SUNKESNI =========================")
print("============================ 1 uzduotis =======================")
# Parašykite funkciją, kurios argumentas būtų tekstas, kuris būtų atspausdinamas konsolėje pridedant “---” pradžioje ir gale.
# PVZ (---labas---)

def print_word(txt):
    add_sym = "---"
    print(add_sym + txt + add_sym)

print_word("labas rytas")

print("============================ 2 uzduotis =======================")
# Sugeneruokite atsitiktinį stringą iš raidžių ir skaičių (10 simbolių).
# Atspausdinkite simbolius stulpeliu.
# Jei tai skaičius apgaubkite “ [ 7 ]”.
# Jei skaičiai eina keli iš eilės, apgaubkite juos kartu.

def generate_rnd_str(length):
  symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ12345678901234567890"
  text = ""
  for i in range(length):
    text += symbols[random.randint(0,len(symbols) -1)]
  return text

rnd_string = generate_rnd_str(10)
sym = ""
for symbol in rnd_string:
    if symbol.isdigit():
        sym += symbol
    else:
        if sym:
            print("[" + sym + "]")
            sym = ""
        print(symbol)

if sym:
    print("[" + sym + "]")
print("============================ 3 uzduotis =======================")
# Parašykite funkciją, kuri skaičiuotų, ir gražintų iš kiek sveikų skaičių jos argumentas dalijasi be liekanos (išskyrus vienetą ir patį save).
# Pvz padavus 10 turi grąžinti 2, o padavus 20 gražintų 4.

def divide_num(number):
    filtered_nums = 0
    if number <= 1:
        return 0
    for i in range(2, number):
        if number % i == 0:
            filtered_nums += 1
    return filtered_nums

print(divide_num(6))

print("============================ 4 uzduotis =======================")
# Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 33 iki 77.
# Išrūšiuokite masyvą pagal daliklių be liekanos kiekį mažėjimo tvarka, panaudodami trečio uždavinio funkciją.


array = [random.randint(33,77) for _ in range(100)]
print("Pradinis masyvas:", array)

array_sorted = sorted(array, key=divide_num, reverse=True)
print("Išrūšiuotas masyvas:", array_sorted)

print("============================ 5 uzduotis =======================")
# Sugeneruokite masyvą iš 100 elementų, kurio reikšmės atsitiktiniai skaičiai nuo 333 iki 777.
# Naudodami 3 uždavinio funkciją iš masyvo suskaičiuokite kiek yra pirminių skaičių.


arr = [random.randint(333,777) for _ in range(100)]
print(arr)

prime_num_count = 0
for num in arr:
    if divide_num(num) == 0:
        prime_num_count += 1

print("Pirminiu skaiciu", prime_num_count)

print("============================ 6 uzduotis =======================")
# Sugeneruokite atsitiktinio (nuo 10 iki 20) ilgio masyvą, kurio visi, išskyrus paskutinį, elementai yra atsitiktiniai skaičiai nuo 0 iki 10,
# o paskutinis elementas masyvas, kuris generuojamas pagal tokią pat salygą kaip ir pirmasis masyvas.
# Viską pakartokite atsitiktinį nuo 10 iki 30  kiekį kartų.
# Paskutinio masyvo paskutinis elementas yra lygus 0;

def generuoti_masyva(gylis, dabartinis_gylis=1): #gyli(kiek kartu kartosis f-ja) gen random
    ilgis = random.randint(10, 20) #masyvo ilgis, kiek sk bus
    masyvas = [] # kaupsime sk

    for _ in range(ilgis - 1): # # Visi elementai, išskyrus paskutinį
        masyvas.append(random.randint(0, 10))
    if dabartinis_gylis == gylis: ## Jei pasiektas paskutinis kartojimas
        masyvas.append(0)
    else:
        masyvas.append(generuoti_masyva(gylis, dabartinis_gylis + 1))
    return masyvas

# Atsitiktinis kartų skaičius nuo 10 iki 30 (gylis)
gylis = random.randint(2, 5)

rezultatas = generuoti_masyva(gylis)

print("Kartų skaičius:", gylis)
print("Sugeneruota masyvas:")
print(rezultatas)

print("============================ 7 uzduotis =======================")
# Suskaičiuokite šešto uždavinio elementų, kurie nėra masyvai, sumą. Skaičiuoti reikia visuose masyvuose ir submasyvuose.

def sumuoti_skaicius(masyvas):
    suma = 0
    for elementas in masyvas:
        if isinstance(elementas, list):  # jei elementas yra masyvas, kviečiame funkciją rekursyviai
            suma += sumuoti_skaicius(elementas)
        else:  # jei skaičius, pridedame prie sumos
            suma += elementas
    return suma

viso_suma = sumuoti_skaicius(rezultatas)
print("Visų skaičių suma masyve ir submasyvuose:", viso_suma)

print("============================ 8 uzduotis =======================")
# Sugeneruokite masyvą iš trijų elementų, kurie yra atsitiktiniai skaičiai nuo 1 iki 33. Jeigu tarp trijų paskutinių elementų yra nors vienas ne pirminis skaičius, prie masyvo pridėkite dar vieną elementą- atsitiktinį skaičių nuo 1 iki 33. Vėl patikrinkite pradinę sąlygą ir jeigu reikia pridėkite dar vieną elementą. Kartokite, kol sąlyga nereikalaus pridėti elemento.

masyvas = [random.randint(1, 33) for _ in range(3)]

while True:
    paskutiniai_trys = masyvas[-3:]
    if all(number_is_prime(x) for x in paskutiniai_trys):
        break
    else:
        masyvas.append(random.randint(1, 33))

print("Galutinis masyvas:", masyvas)

print("============================ 9 uzduotis =======================")
# Sugeneruokite masyvą iš 10 elementų, kurie yra masyvai iš 10 elementų, kurie yra atsitiktiniai skaičiai nuo 1 iki 100.
# Jeigu tokio didelio masyvo (ne atskirai mažesnių) pirminių skaičių vidurkis mažesnis už 70, suraskite masyve mažiausią skaičių (nebūtinai pirminį) ir prie jo pridėkite 3. Vėl paskaičiuokite masyvo pirminių skaičių vidurkį ir jeigu mažesnis nei 70 viską kartokite.






print("============================ 10 uzduotis =======================")
# a)Surūšiuokite studentus pagal jų pažymių vidurkį mažėjančia tvarka.
# b) Išfiltruokite sąrašą nuo studentų kurių vidurkis nesiekia 6.0
students = [
    ["Jonas", "Jonaitis", [8, 9, 10, 7]],
    ["Asta", "Petrauskaitė", [10, 10, 9]],
    ["Tomas", "Kairys", [6, 7, 8, 7, 9]],
    ["Laura", "Kazlauskienė", [9, 9, 8, 10]],
    ["Mantas", "Vaitkus", [5, 6, 6, 6]],
    ["Greta", "Jankauskaitė", [10, 9, 10, 10]],
    ["Dovydas", "Mickus", [7, 8, 7, 9]],
    ["Eglė", "Balsytė", [2, 6, 7]],
    ["Karolis", "Petraitis", [9, 7, 6, 8, 7]],
    ["Ieva", "Norkutė", [10, 9, 10, 8]]
]

def average(student):
    return sum(student[2]) / len(student[2])

print("-----------------(a)------------------")
students_sorted = sorted(students, key = average, reverse=True)

for s in students_sorted:
    print(s[0], s[1], "Vidurkis:", round(average(s), 2))

print("-----------------(b)------------------")
students_filtered = []
for s in students:
    if average(s) >= 6.0:
        students_filtered.append(s)
        print(s[0], s[1], "Vidurkis:", round(average(s), 2))

