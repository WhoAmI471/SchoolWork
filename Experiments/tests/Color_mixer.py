color1 = str(input())
color2 = str(input())

if color1 == 'красный' and color2 == 'красный':
    print('красный')
elif color1 == 'красный'and color2 == 'синий':
    print('фиолетовый')
elif color1 == 'красный' and color2 == 'желтый':
    print('оранжевый')

if color1 == 'синий' and color2 == 'синий':
    print('синий')
elif color1 == 'синий'and color2 == 'красный':
    print('фиолетовый')
elif color1 == 'синий' and color2 == 'желтый':
    print('зеленый')

if color1 == 'желтый' and color2 == 'желтый':
    print('желтый')
elif color1 == 'желтый'and color2 == 'красный':
    print('оранжевый')
elif color1 == 'желтый' and color2 == 'синий':
    print('зеленый')

if (color1 != 'красный' and color1 != 'синий' and color1 != 'желтый') or (color2 != 'красный' and color2 != 'синий' and color2 != 'желтый'):
    print('ошибка цвета')



