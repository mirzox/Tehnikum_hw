
def Average(a,b,c):
    if a > b > c or a < b < c:
        print(f'Число {b} является средним среди введенных чисел') 
    elif b > a > c or b < a < c:
        print(f'Число {a} является средним среди введенных чисел') 
    elif b > c > a or b < c < a:
        print(f'Число {c} является средним среди введенных чисел') 

def Max(a,b,c):
    if a > b >= c or a > c >= b:
        return a
    elif b > a >= c or b > c >= a:
        return b
    elif c > a >= b or c > b >= a:
        return c 
            
def AI_Maxmud_aka(age,gender):
    if age >= 18 and gender.lower() == 'female':
        a = input("Давайте я вас удивлю введите два числа и вы увидете как быстро я умею считать 🙃🙃🙃: ")
        b = input("А теперь введите 2-ое число: ")
        if '.' in a:
            a = float(a)
        else:
            a = int(a)
        if '.' in b:
            b = float(b)
        else:
            b = int(b)
        print(f'Сумма чисел равна: {a+b} \nРазность чисел равно: {a-b if a>=b else b-a} \nПроизведение равно: {a*b}')
        answer = input("Вам понравлось? да/нет\n")
        if answer.lower() == 'да':
            date = input("Что думаете на счет прогулки? да/нет\n")
            if date.lower() == 'да':
                print("Отлично, я вас жду в таком то место в такое то время. До скорой встречи🙂🙂🙂")
            elif date.lower() == 'нет':
                print("Прощайте 😢😢😢")
        elif answer.lower() == 'нет':
            print("Пока 😢😢😢")
    else:
        print("Простите я не смогу с вами общатся)")

print("____________________________________ Задание№1 ____________________________________")
a = input("Введите 1-ое число: ")
b = input("Введите 2-ое число: ")
c = input("Введите 3-ое число: ")  
Average(float(a) if '.' in a else int(a),float(b) if '.' in b  else int(b),float(c) if '.' in c  else int(c))


print("\n____________________________________ Задание№2 ____________________________________\n")

print(f'Число {Max(int(input("Введите 1-ое число: ")),int(input("Введите 2-ое число: ")),int(input("Введите 3-ое число: ")))} является максимальным среди введенных')

print("\n____________________________________ Задание№3 ____________________________________\n")
name = input("Привет мея зовут Махмуд ака. А вас как зовут?\n")
a = input(f'''{name.capitalize()} У вас очень красивое и редкое имя! \nМне бы хотелось узнать ваш возраст и ваш пол😅😅😅\n
Сперва введите ваш возраст: ''')
g = input("А теперь ваш пол(male/female): ")
AI_Maxmud_aka(int(a),g)
