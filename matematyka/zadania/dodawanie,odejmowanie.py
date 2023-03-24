import random

print('| PROGRAM DO NAUKI DODAWANIA I ODEJMOWANIA |')

print('AUTOR: JAN HANNIBAL')

powtarzanie_petli = 1000

print(' ')
maksymalne_cyfry_w_dodawaniu = input('jaką maksymalną liczbę lub cyfre chcesz dodać  ')

while powtarzanie_petli > 0:
    try:

        powtarzanie_petli = powtarzanie_petli - 1

        znaki_dzialan_matematycznych = ['+', '-']

        wylosowany_znak = random.randint(0, 1)

        wylosowany_znak_dzialan_matematycznych = znaki_dzialan_matematycznych[wylosowany_znak]

        liczba1 = random.randint(0, int(maksymalne_cyfry_w_dodawaniu))
        liczba2 = random.randint(0, int(maksymalne_cyfry_w_dodawaniu))

        odpowiedz = int(input(str(liczba1) + ' ' + wylosowany_znak_dzialan_matematycznych + ' ' + str(liczba2) + ' = '))

        if wylosowany_znak_dzialan_matematycznych == '+':
            poprawna_odpowiedz = liczba1 + liczba2

        else:
            poprawna_odpowiedz = liczba1 - liczba2

        if odpowiedz == poprawna_odpowiedz:
            print(' ')
            print('dobrze')
            print(' ')
        else:
            print(' ')
            print('źle')
            print(' ')

        print('-----  MENU  -----')
        print('1 = następne działanie')
        print('2 = wyjdź')
        wybor_menu = input('twój wybór to: ')
        print("--------------------")

        if wybor_menu == '2':
            print('do widzenia')
            powtarzanie_petli = 0

        elif wybor_menu == '1':
            continue

        else:
            exit('błąd zrobiłeś')

    except:
        print('miałeś podać liczbę')
    print( )