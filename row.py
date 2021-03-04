def check_user(arr,name):
    for i in arr:
        if name in arr:
            return  True
    return False
def create_user(arr,name):
    arr.append([name,'',''])
def isready(arr,name,key):
    for i in arr:
        if key == 'age' and i[1] != '':
            return True
        elif key == 'phone' and i[2] != '':
            return  True
    return False
def update(arr,name,key,value):
    for i in arr:
        if name in i :
            if key == 'age':
                i[1] == value
            elif key == 'phone':
                i[2] = value

conf = '''Условия конфиденциальности 
Использование Сервиса в любой форме означает безоговорочное согласие 
Пользователя с условиями настоящей \nПолитики конфиденциальности и указанными в 
ней условиями обработки его персональной информации. \nВ случае несогласия с условиями 
\nПолитики конфиденциальности Пользователь должен воздержаться от использования Сервиса
\nПолитика конфиденциальности (в том числе любая из ее частей) может быть изменена 
\nАдминистрацией без какого-либо специального уведомления и без выплаты какой-либо компенсации в связи с этим. 
\nНовая редакция Политики конфиденциальности вступает в силу с момента ее размещения на сайте Администрации'''
print("Задание 3 **")
database = []
while True:
    print("Добро пожаловать в бот Махмуд ака v2.0")
    agree = input("Для начала я бы хотел спросить даете ли вы согласие на обработку ваших конфиденциальных данных? да/нет")
    while True:
        if agree.lower() == 'да':
            break
        elif agree.lower() == 'нет':
            print("Давайте тогда для начала я ознакомлю вас с условиямии конфиденциальности ваших данных")
            print(conf)
            agree = input("Даете ли вы согласие на обработку ваших конфиденциальных данных? да/нет")
            if agree.lower() == 'да':
                break
            elif agree.lower() == 'нет':
                break
    if agree.lower() == 'да':
        name = input("Для начала введите свое имя: ")
        if not check_user(database,name):
            create_user(database,name)
        elif not isready(database,name,'age'):
            while True:
                try:
                    age = int(input("Введите ваш возраст: "))
                    update(database,name,'age',age)
                    break
                except Exception:
                    print("Ошибка ввода попробуйте ввести заново")
        elif not isready(database,name,'phone'):
            pass
