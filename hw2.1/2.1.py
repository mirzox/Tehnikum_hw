
def summ(f,t):
    count = f
    summ = 0
    if t <= 100:
        while count <=t:
            summ += count
            count += 1        
    else:
        summ = ((f+t)*(t-f+1))/2
    return summ

def check_operand(char):
    if char in ['+','-','*','/','0']:
        return True
    else:
        False

def operations(a,b,char):
    if char == '+':
        return a+b
    elif char == '-':
        return a-b if a>b else b-a
    elif char == '*':
        return a*b
    elif char == '/':
        try:
            return a/b
        except ZeroDivisionError:            
            return 'ZeroDivisionError'
    elif char == '0':
        return 'END'
    

print((0+10)*(10+1)/2)
print("____________________________________ Задание№1 ____________________________________\n")

print(f'Сумма чисел от 1 до 100 равна: {summ(1,100)}')

print("\n____________________________________ Задание№2 ____________________________________\n")
print(f'Сумма чисел от 1 до 14 равна: {summ(1,14)}')

print("\n____________________________________ Задание№2(advanced) ____________________________________\n")
while True:
    n = input("Введите целое число которое больще 0, чтоб найти сумму чисел до введенного вами числа: ")
    if n.isdigit():
        break
    elif '.' in n:
        try:
            n = float(n)
        except Exception as ex:
            print(ex)
            print("ERROR ошибка ввода вы ввели не числовое значение")          
        else:
            break   
    else:
        print("ERROR ошибка ввода вы ввели не числовое значение")
print(f'Сумма чисел от 0 до {int(n)} равна: {summ(0,int(n))}')

print("\n____________________________________ Задание№3 ____________________________________\n")

while True:
    try:
        a = int(input("\nВведите 1-ое число: "))
        b = int(input("Введите 2-ое число: "))
        while True:
            char = input("Выберите одно из действий  '+','-','*','/' или '0' чтоб завершить программу: ")
            if check_operand(char):
                break
            else:
                print("Такое действие отсутствует!!! Выберите заново!\n")
        answer = operations(a,b,char)
        if answer == 'ZeroDivisionError':
            print("Ошибка на нуль делить нельзя")
        elif answer != 'END' :
            print(f'{a} {char} {b} = {answer}')
        else:
            break
    except ValueError:
        print("Ошибка ввода введите числовое значение!!!")

print("\n____________________________________ Задание№3** ____________________________________\n")
import os,time
database = []

def check_user(name):
    for i in database:
        if name in i:
            return  True
    return False
def create_user(name):
    database.append([name,'',''])
def isready(name,key):
    for i in database:
        if key == 'age' and i[2] != '':
            return True
        elif key == 'phone' and i[1] != '':
            return  True
    return False
def update(name,key,value):
    for i in database:
        if name in i :
            if key == 'age':
                i[2] == value
            elif key == 'phone':
                i[1] = value

conf = '''Условия конфиденциальности 
Использование Сервиса в любой форме означает безоговорочное согласие 
Пользователя с условиями настоящей \nПолитики конфиденциальности и указанными в 
ней условиями обработки его персональной информации. \nВ случае несогласия с условиями 
Политики конфиденциальности Пользователь должен воздержаться от использования Сервиса
Политика конфиденциальности (в том числе любая из ее частей) может быть изменена 
Администрацией без какого-либо специального уведомления и без выплаты какой-либо компенсации в связи с этим. 
Новая редакция Политики конфиденциальности вступает в силу с момента ее размещения на сайте Администрации\n'''
print("Задание 3 **")

while True:
    print("Добро пожаловать в бот Махмуд ака v2.0")
    agree = input("Для начала я бы хотел спросить даете ли вы согласие на обработку ваших конфиденциальных данных? да/нет: ").lower()
    while True:
        if agree == 'да':
            break
        elif agree == 'нет':
            print("Давайте тогда для начала я ознакомлю вас с условиямии конфиденциальности ваших данных\n")
            print(conf)
            agree = input("Даете ли вы согласие на обработку ваших конфиденциальных данных? да/нет: ")
            if agree == 'да':
                break
            elif agree == 'нет':
                break
        else:
            print("Ошибка ввода")
            break
    if agree == 'да':
        name = input("Для начала введите свое имя: ")
        if not check_user(name):
            create_user(name)
        if not isready(name,'age'):
            while True:
                try:
                    age = int(input("Введите ваш возраст: "))
                    update(name,'age',age)
                    break
                except Exception:
                    print("Ошибка ввода попробуйте ввести заново")
        if not isready(name,'phone'):
            while True:
                try:
                    req = input("Согласны ли вы отправить ваш номер телефона? да/нет: ").lower()
                    if req == 'да':
                        phone = input("Введите ваш номер телефона: ")
                        update(name,'phone',phone)
                    elif req == 'нет':
                        print("\nВам будет предоставлен бонус если вы отправите ваш номер телефона, а про бонус узнаете когда отправите номер телефона🙃🙃🙃")
                    else:
                        print("Не верный ввод попробуйте заново!!!")
                    if isready(name,'phone'):
                        print('''\nВаш бонус это бесплатная подписка на бот Махмуд ака v2.0😂😂😂
Это была шутка. Ваш бонус это купон на пользование веб хостингом на 2 месяца бесплатно.
https://github.com/mirzox/Tehnikum_hw/tree/main/hw2.1 перейдите по этой ссылку там есть файл подназванием купон
отсканьте штрих код и получите ваш бонус😊😊😊''')
                        time.sleep(10)
                        os.system('cls')
                        break
                                            
                except Exception:
                    print("ERROR!!!")    
    else:
        print("Жаль нам придется прошатся 😥😥😥")
        time.sleep(2)
        os.system('cls')
    
