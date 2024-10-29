import random
i = 0
d = 0
y = 0
licz = 0
print('English , Polski')
d = input()
if d == 'English':
    licz = 1
elif d == 'Polski':
    i = 3

random_number = random.randrange(0, 100)

if d == 'English':
#print('Hello, welcome to the game guess what number 0.1 beta version without graphics')
    print('Author czwartoklasista z laptopem https://www.youtube.com/results?search_query=czwartoklasista+z+laptopem')
elif d == 'Polski':
#print('Cześć, witaj w grze zgadnij jaka to liczba 0.1 wersja beta bez grafiki')
    print('Autor Czwartoklasista z laptopem https://www.youtube.com/results?search_query=czwartoklasista+z+laptopem')
print('wpisz jaka liczba lub cyfra się wylosowała')
print('enter the number or digit that was drawn')
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







































