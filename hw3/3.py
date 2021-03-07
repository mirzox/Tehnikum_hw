from random import randint
text = {
    '1': "Я загадал число на отрезке {} до {} попробуй его угадать: ",
    'cool':['твое число на много больше','твое число на много меньше'],
    'warm':['твое число больше мной загаданного','твое число меньше мной загаданного'],
    'v_w':['твое число не много больше мной загаданного','твое число не много меньше мной загаданного']    
}

def hint(level,rd,a):
    delta = abs(rd - a)
    if level == '1':
        if delta >= 5:
            print(f"Холодно {text['cool'][0] if a > rd  else text['cool'][1] }")
        elif delta < 5 and delta >=3:
            print(f"Тепло {text['warm'][0] if a > rd  else text['warm'][1] }")
        elif delta < 3:
            print(f"Очень тепло {text['v_w'][0]if a > rd  else text['v_w'][1] } ")    
    elif level == '2':
        if delta >= 20:
            print(f"Очень холодно {text['cool'][0] if a > rd  else text['cool'][1] }")
        elif delta >= 10 and delta < 20:
            print(f"Холодно {text['cool'][0] if a > rd  else text['cool'][1] }")
        elif delta < 10 and delta >=3:
            print(f"Тепло {text['warm'][0] if a > rd  else text['warm'][1] }")
        elif delta < 3:
            print(f"Очень тепло {text['v_w'][0]if a > rd  else text['v_w'][1] } ")
    elif level == '3':
        if delta >= 50:
            print(f"Очень холодно {text['cool'][0] if a > rd  else text['cool'][1] }")
        elif delta >= 10 and delta < 50:
            print(f"Холодно {text['cool'][0] if a > rd  else text['cool'][1] }")
        elif delta < 10 and delta >=5:
            print(f"Тепло {text['warm'][0] if a > rd  else text['warm'][1] }")
        elif delta < 5:
            print(f"Очень тепло {text['v_w'][0]if a > rd  else text['v_w'][1] } ")

while True:
    choice = input('''Выберите уровень сложности задания
    1 - Базовые задачи
    2 - Средние задачи
    3 - Конкурсная задача
    0 - Завершить прогу: ''')
    if choice == '1':
        try:
            num = int(input("Введите кол-во элемтов в массиве: "))
            arr = list(range(0,num))
            i = 0
            while i < len(arr):
                print(arr[i],end= ' ')
                i+=1 
            print('\n\n')
            i = 1
            arr = []
            while i:
                elem = int(input(f'Введите {i} элемент массива: '))
                if elem:
                    arr.append(elem)
                    i+=1
                else:
                    break
            print(f'Сумма элементов массива равна: {sum(arr)}\n')  
            while True:
                a = input("Введите цену за кг асфальта: ")
                if a.isdigit():
                    print(a[::-1])
                    break
                else:
                    print("Ошибка ввода!!! Введите цену асфальта заново")
        except Exception:
            print("Ошибка !!!")            
    elif choice == '2':
        try:
            n = int(input("Введите число n = "))
            s_w = 0
            s_f =  n*(n+1)/2
            i = 1
            while i<=n:
                s_w += i
                i+=1
            if s_w == s_f:
                print('Равество верное')
            else:
                print('Равенство не верное!!!')            
        except Exception:
            print("Ошибка !!!") 
    elif choice == '3':
        try:
            print("Две желтые летающие овцы: ")
            while True:
                level = input('для начала выбери уровень сложности:\n1 - легкий\n2 - средний\n3 - трудный\n0 - выход из игры ')
                if level == '1':
                    rand_num = randint(0,10)
                    print(text['1'].format(0,10))
                elif level == '2':
                    rand_num = randint(0,40)
                    print(text['1'].format(0,40))
                elif level == '3':
                    rand_num = randint(0,100)  
                    print(text['1'].format(0,100))  
                elif level == '0':
                    break   
                else:
                    print('Такого варианта не сушествует попробуйте заново') 
                    continue      
                while True:
                    a = input().strip()
                    if a.isdigit():
                        a = int(a)
                        if a == rand_num:
                            print('Поздравляем вы угадали число')
                            break
                        else:
                            hint(level,rand_num,a)
                    else:
                        print("Вы ввели не числовое значение попробуйте заново")          
        except Exception as ex:
            print(type(ex).__name__)


    elif choice == '0':
        break
    else:
        print("Ошибка ввода выберите заново")
    
