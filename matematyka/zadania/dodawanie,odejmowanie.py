import random

print('| PROGRAM DO NAUKI DODAWANIA I ODEJMOWANIA |')

print('AUTOR: JAN HANNIBAL')

powtarzanie_petli = 1000

print(' ')
maksymalne_cyfry_w_dodawaniu = input('jaką maksymalną liczbę lub cyfre chcesz dodać  ')

ilosc_poprawnych_odpowiedzi = 0

ilosc_niepoprawnych_odpowiedzi = 0

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
            ilosc_poprawnych_odpowiedzi = ilosc_poprawnych_odpowiedzi + 1
        else:
            print(' ')
            print('źle')
            print(' ')
            ilosc_niepoprawnych_odpowiedzi = ilosc_niepoprawnych_odpowiedzi + 1

        print('-----  MENU  -----')
        print('1 = następne działanie')
        print('2 = wyjdź')
        wybor_menu = input('twój wybór to: ')
        print("--------------------")

        if wybor_menu == '2':
            powtarzanie_petli = 0

        elif wybor_menu == '1':
            continue

        else:
            break

    except:
        print('miałeś podać liczbę')
    print(' ')

print('ilość poprawnych odpowiedzi: ', ilosc_poprawnych_odpowiedzi)
print('ilość niepoprawnych odpowiedzi: ', ilosc_niepoprawnych_odpowiedzi)
print('do widzenia')