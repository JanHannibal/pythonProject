import random
x1 = "one"
x2 = "two"
x3 = "three"
x4 = "four"
x5 = "five"
x6 = "six"
x7 = "seven"
x8 = "eight"
x9 = "nine"
x10 = "ten"
x11 = "eleven"
x12 = "twelve"
x13 = "thirteen"
x14 = "fourteen"
x15 = "fifteen"
x16 = "sixteen"
x17 = "seventeen"
x18 = "eighteen"
x19 = "nineteen"
x20 = "twenty"
x30 = "thirty"
x40 = "forty"
x50 = "fifty"
x60 = "sixty"
x70 = "seventy"
x80 = "eighty"
x90 = "ninety"
def liczebnik ():
    random_number = random.randrange(1, 21)
    poprawna_odpowiedz = ''
    if random_number == 1:
        poprawna_odpowiedz = x1
    elif random_number == 2:
        poprawna_odpowiedz = x2
    elif random_number == 3:
        poprawna_odpowiedz = x3
    elif random_number == 4:
        poprawna_odpowiedz = x4
    elif random_number == 5:
        poprawna_odpowiedz = x5
    elif random_number == 6:
        poprawna_odpowiedz = x6
    elif random_number == 7:
        poprawna_odpowiedz = x7
    elif random_number == 8:
        poprawna_odpowiedz = x8
    elif random_number == 9:
        poprawna_odpowiedz = x9
    elif random_number == 10:
        poprawna_odpowiedz = x10
    elif random_number == 11:
        poprawna_odpowiedz = x11
    elif random_number == 12:
        poprawna_odpowiedz = x12
    elif random_number == 13:
        poprawna_odpowiedz = x13
    elif random_number == 14:
        poprawna_odpowiedz = x14
    elif random_number == 15:
        poprawna_odpowiedz = x15
    elif random_number == 16:
        poprawna_odpowiedz = x16
    elif random_number == 17:
        poprawna_odpowiedz = x17
    elif random_number == 18:
        poprawna_odpowiedz = x18
    elif random_number == 19:
        poprawna_odpowiedz = x19
    elif random_number == 20:
        poprawna_odpowiedz = x20

    print(random_number)
    wybor = input()

    if wybor == poprawna_odpowiedz:
       return True
    else:
       return False


q = 0
while True:
    if liczebnik() == True:
        q = q + 1
    else:
        print('brawo zrobiłeś', q, 'odpowiedzi z rzędu')
        exit('źle')
