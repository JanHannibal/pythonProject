import random

while True:
    try:
        znaki_dzialan_matematycznych = ['+', '-']

        wylosowany_znak = random.randint(0, 1)

        wylosowany_znak_dzialan_matematycznych = znaki_dzialan_matematycznych[wylosowany_znak]

        liczba1 = random.randint(0, 10)
        liczba2 = random.randint(0, 10)

        odpowiedz = int(input(str(liczba1) + ' ' + wylosowany_znak_dzialan_matematycznych + ' ' + str(liczba2) + ' = ' ))

        if wylosowany_znak_dzialan_matematycznych == '+':
            poprawna_odpowiedz = liczba1 + liczba2

        else:
            poprawna_odpowiedz = liczba1 - liczba2

        if odpowiedz == poprawna_odpowiedz:
            print('dobrze')

        else:
            print('źle')
    except:
        print('miałeś podać liczbę')