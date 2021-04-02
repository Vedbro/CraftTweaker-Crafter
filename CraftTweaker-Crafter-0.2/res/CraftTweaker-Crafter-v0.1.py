import requests

def de():
    output = input('Предмет, который получится: ')

    cataly = input('Id катализатора (предмета): ')

    print('Выбери уровень слияния\n1. Базовый\n2. Виверна\n3. Дракон\n4. Хаос')

    lvl =  int(input(''))
    if lvl >= 4:
        print('Уровень не должен превышать значения "Хаос"! (Был установлен уровень "Хаос")')
        lvl = 4

    if lvl <= 1:
        print('Уровень не должен быть ниже значения "Базовый"! (Был установлен уровень "Базовый")')
        lvl = 1

    if lvl == 1:
        lvl = 0

    if lvl == 2:
        lvl = 1

    if lvl == 3:
        lvl = 2

    if lvl == 4:
        lvl = 3

    rf = input('Затраты энергии(RF) на рецепт: ')

    print('\nОставь строчку пустой, если хочешь закочнить рецепт\n')

    item1 = input('Первый предмет:')
    if item1 != '':
        item1 = item1
    if item1 == '':
        print('moretweaker.draconicevolution.FusionCrafting.add(', output, ',', cataly, ', ', lvl, ',', rf, ', [',item1, ']);')

        de()

    item2 = input('Второй предмет:')
    if item2 != '':
        item2 = ',' + item2
    if item2 == '':
        print('moretweaker.draconicevolution.FusionCrafting.add(', output, ',', cataly, ', ', lvl, ',', rf, ',[', item1,',', item2, ']);')

        de()

    item3 = input('Третий предмет:')
    if item3 != '':
        item3 = ',' + item3
    if item3 == '':
        print('moretweaker.draconicevolution.FusionCrafting.add(', output, ',', cataly, ', ', lvl, ',', rf, ',[', item1,item2, item3, ']);')

        de()

    item4 = input('Четвёртый предмет:')
    if item4 != '':
        item4 = ',' + item4
    if item4 == '':
        print('moretweaker.draconicevolution.FusionCrafting.add(', output, ',', cataly, ', ', lvl, ',', rf, ',[', item1,item2, item3, item4, ']);')

        de()

    item5 = input('Пятый предмет:')
    if item5 != '':
        item5 = ',' + item5
    if item5 == '':
        print('moretweaker.draconicevolution.FusionCrafting.add(', output, ',', cataly, ', ', lvl, ',', rf, ',[', item1,item2, item3, item4, item5, ']);')

        de()

    item6 = input('Шестой предмет:')
    if item6 != '':
        item6 = ',' + item6
    if item6 == '':
        print('moretweaker.draconicevolution.FusionCrafting.add(', output, ',', cataly, ', ', lvl, ',', rf, ',[', item1,item2, item3, item4, item5, item6, ']);')

        de()

    item7 = input('Седьмой предмет:')
    if item7 != '':
        item7 = ',' + item7
    if item7 == '':
        print('moretweaker.draconicevolution.FusionCrafting.add(', output, ',', cataly, ', ', lvl, ',', rf, ',[', item1,item2, item3, item4, item5, item6, item7, ']);')

        de()

    item8 = input('Восьмой предмет:')
    if item8 != '':
        item8 = ',' + item8
    if item8 == '':
        print('moretweaker.draconicevolution.FusionCrafting.add(', output, ',', cataly, ', ', lvl, ',', rf, ',[', item1,item2, item3, item4, item5, item6, item7, item8, ']);')

        de()

    item9 = input('Девятый предмет:')
    if item9 != '':
        item9 = ',' + item9
    if item9 == '':
        print('moretweaker.draconicevolution.FusionCrafting.add(', output, ',', cataly, ', ', lvl, ',', rf, ',[', item1,item2, item2, item3, item4, item5, item6, item7, item8, item9, ']);')

        de()
    item10 = input('Десятый предмет:')

    if item10 != '':
        item10 = ',' + item9
    if item10 == '':
        print('moretweaker.draconicevolution.FusionCrafting.add(', output, ',', cataly, ', ', lvl, ',', rf, ',[', item1,item2, item2, item3, item4, item5, item6, item7, item8, item9, item10, ']);')
        de()

def mods():
    print('1. Draconic Evolution')
    mque = input('Выбери мод:')
    if mque == '1':
        de()
    if mque >= '2':
        mods()
def ctshaped():
    print('Оставь строчку пустой, если нужен пропуск(значение "null") в сетке верстака')
    name = input('\nId предмета:')
    item1 = input('Первый предмет:')
    item2 = input('Второй предмет:')
    item3 = input('Третий предмет:')
    item4 = input('Четвёртый предмет:')
    item5 = input('Пятый предмет:')
    item6 = input('Шестой предмет:')
    item7 = input('Седьмой предмет:')
    item8 = input('Восьмой предмет:')
    item9 = input('Девятый предмет:')
    if name == '':
        name = 'null'
    if item1 == '':
        item1 = 'null'
    if item2 == '':
        item2 = 'null'
    if item3 == '':
        item3 = 'null'
    if item4 == '':
        item4 = 'null'
    if item5 == '':
        item5 = 'null'
    if item6 == '':
        item6 = 'null'
    if item7 == '':
        item7 = 'null'
    if item8 == '':
        item8 = 'null'
    if item9 == '':
        item9 = 'null'
    print('Форменый рецепт recipes.addShaped(',name,',[[',item1,',',item2,',',item3,'], [',item4,',',item5,',',item6,'], [',item7,',',item8,',',item9,']]);')
    ctshaped()

def ctshapeless():

    print('Оставь строчку пустой, если хочешь закочнить рецепт')
    name = input('\nId предмета:')
    item1 = input('Первый предмет:')
    if item1 != '':
        item1 = item1
    if item1 == '':
        print('recipes.addShapeless(',name,',[',item1,']);')
        ctshapeless()
    item2 = input('Второй предмет:')
    if item2 != '':
        item2 = ',' + item2
    if item2 == '':
        print('recipes.addShapeless(',name,',[',item1, item2,']);')
        ctshapeless()
    item3 = input('Третий предмет:')
    if item3 != '':
        item3 = ',' + item3
    if item3 == '':
        print('recipes.addShapeless(',name,',[',item1, item2,item3,']);')
        ctshapeless()
    item4 = input('Четвёртый предмет:')
    if item4 != '':
        item4 = ',' + item4
    if item4 == '':
        print('recipes.addShapeless(',name,',[',item1, item2,item3,item4,']);')
        ctshapeless()
    item5 = input('Пятый предмет:')
    if item5 != '':
        item5 = ',' + item5
    if item5 == '':
        print('recipes.addShapeless(',name,',[',item1, item2,item3,item4,item5,']);')
        ctshapeless()
    item6 = input('Шестой предмет:')
    if item6 != '':
        item6 = ',' + item6
    if item6 == '':
        print('recipes.addShapeless(',name,',[',item1, item2,item3,item4,item5,item6,']);')
        ctshapeless()
    item7 = input('Седьмой предмет:')
    if item7 != '':
        item7 = ',' + item7
    if item7 == '':
        print('recipes.addShapeless(',name,',[',item1, item2,item3,item4,item5,item6,item7,']);')
        ctshapeless()
    item8 = input('Восьмой предмет:')
    if item8 != '':
        item8 = ',' + item8
    if item8 == '':
        print('recipes.addShapeless(',name,',[',item1, item2,item3,item4,item5,item6,item7,item8,']);')
        ctshapeless()
    item9 = input('Девятый предмет:')
    if item9 != '':
        item9 = ',' + item9
    if item9 == '':
        print('recipes.addShapeless(',name,',[',item1, item2, item2, item3, item4, item5, item6, item7, item8, item9,']);')
        ctshapeless()

def craftingtable():
    print('Какой рецепт делаем?\n1. Форменный(Shaped)\n2. Бесформенный(Shapeless)')
    shape = input('Выбери режим из списка:')
    if shape == '1':
        ctshaped()
    if shape == '2':
        ctshapeless()
def furnace():

    put = input('\nПредмет, который нужно переплавить: ')
    output = input('Предмет, который получится на выходе: ')
    exp = input('Опыт, который получит игрок после переплавки: ')
    print('')
    if output == '':
        print('Эй! Ты не добавил(а) предмет, который получится на выходе!')
    if put == '':
        print('Эй! Ты не добавил(а) предмет, который нужно переплавить!')
    a = 1
    b = 1
    c = 0
    if exp == '':
        exp = 0
    if put != '':
        c = c + a
    if output != '':
        c = c + a
    if c == 2:
        print('furnace.addRecipe(', put, ',', output, ',', exp, ');')

    furnace()

def start():
    print('1. Ванилла\n2. Моды')
    rgque = input('Выбери режим из списка:')
    if rgque == '1':
        print('1. Верстак\n2. Печь')
        vc = input('Выбери рецепт из списка:')
        if vc == '1':
            craftingtable()
        if vc == '2':
            furnace()
    if rgque == '2':
        mods()

start()