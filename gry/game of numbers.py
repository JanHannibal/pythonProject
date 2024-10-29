import random
i = 0
d = 0
y = 0
lev2 = 0
licz = 0
print('English , Polski')
d = input()
if d == 'English':
    licz = 1
elif d == 'Polski':
    i = 3

random_number = random.randrange(0, 50)

if d == 'English':
    print('Author czwartoklasista z laptopem https://www.youtube.com/results?search_query=czwartoklasista+z+laptopem')
elif d == 'Polski':
    print('Autor Czwartoklasista z laptopem https://www.youtube.com/results?search_query=czwartoklasista+z+laptopem')
print('wpisz jaka liczba lub cyfra się wylosowała 0-50')
print('enter the number or digit that was drawn 0-50')
while i == 3:

    y = y + 1
    p = int(input())
    if random_number == p:
        i = i + 1

    else:
        print('źle')
        if p < random_number:
            print(' to jest liczba większa niż', p)
        else:
            print('to jest liczba mniejsza niż', p)
if d == 'Polski':
    print('zgadłeś za', y, 'razem')

while licz == 1:

    y = y + 1
    t = int(input())
    if random_number == t:
        licz = licz + 1

    else:
        print('Badly')
        if t < random_number:
            print(' this is a number greater than', t)
        else:
            print('this is a number less than', t)
if d == 'English':
    print('you guessed it', y,  'time')




































































































































































































    lev2 == 1
    print('you made it to the next level')
elif y <= 3 and d == 'Polski':
    lev2 == 1
    print("dostałeś się do następnego levelu")
else:
    exit()
if lev2 == 1:
    random_number = random.randrange(0, 100)
    print('wpisz jaka liczba lub cyfra się wylosowała 0-100')
    print('enter the number or digit that was drawn 0-100')
    while i == 3:

        y = y + 1
        p = int(input())
        if random_number == p:
            i = i + 1

        else:
            print('źle')
            if p < random_number:
                print(' to jest liczba większa niż', p)
            else:
                print('to jest liczba mniejsza niż', p)
    if d == 'Polski':
        print('zgadłeś za', y, 'razem')

    while licz == 1:

        y = y + 1
        t = int(input())
        if random_number == t:
            licz = licz + 1

        else:
            print('Badly')
            if t < random_number:
                print(' this is a number greater than', t)
            else:
                print('this is a number less than', t)
    if y <= 2 and d == 'English':
        print('you win secret level')
    elif y <= 2 and d == 'Polski':
        print('wygrałeś sekretny level')
    else:
        print('przegrałeś sekretny level')
        print('you lost in secret level')
































