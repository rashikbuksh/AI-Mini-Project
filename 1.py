def normalpeople(n):
    if 300 >= n > 0:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*0))
    elif 400 >= n > 300:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*5))
    elif 700 >= n > 400:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*10))
    elif 1100 >= n > 700:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*15))
    elif 1600 >= n > 1100:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*20))
    else:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*25))


def womenand65people(n):
    if 350 >= n > 0:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*0))
    elif 450 >= n > 350:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*5))
    elif 750 >= n > 450:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*10))
    elif 1150 >= n > 750:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*15))
    elif 1650 >= n > 1150:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*20))
    else:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*25))


def disabledpeople(n):
    if 450 >= n > 0:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*0))
    elif 550 >= n > 450:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*5))
    elif 850 >= n > 550:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*10))
    elif 1250 >= n > 850:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*15))
    elif 1750 >= n > 1250:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*20))
    else:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*25))


def parentofdisabledpeople(n):
    if 350 >= n > 0:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*0.0))
    elif 450 >= n > 350:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*5.0))
    elif 750 >= n > 450:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*10))
    elif 1150 >= n > 750:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*15))
    elif 1650 >= n > 1150:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*20))
    else:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*25))


def freedomfighterpeople(n):
    if 475 >= n > 0:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*0))
    elif 575 >= n > 475:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*5))
    elif 875 >= n > 575:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*10))
    elif 1275 >= n > 875:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*15))
    elif 1775 >= n > 1275:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*20))
    else:
        print('Income = ' + str(n) + 'k\nTax = ' + str(n*25))


def takeInput():
    print('Enter Income(k): ')
    income = int(input())
    return income


while True:
    print('\n\033[1m Note: You must insert the values in "k" if you input 100, then The system will automatically count it as 100k.\033[0m\n')
    print('1.General')
    print('2.Woman and age greater than 65')
    print('3.Disabled')
    print('4.Freedom Fighters')
    print('5.Parent of Disabled')
    print('0.Exit')

    a = int(input())
    if a == 1:
        income = takeInput()
        normalpeople(income)
    elif a == 2:
        income = takeInput()
        womenand65people(income)
    elif a == 3:
        income = takeInput()
        disabledpeople(income)
    elif a == 4:
        income = takeInput()
        freedomfighterpeople(income)
    elif a == 5:
        income = takeInput()
        parentofdisabledpeople(income)
    elif a == 0:
        break
    else:
        print('Wrong Input')
