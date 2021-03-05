while True:
    choice = input('''Выбери уровень сложности задания
    1 - Базовые задачи
    2 - Средние задачи
    3 - Конкурсные задачи
    0 - Завершить прогу: ''')
    if choice == '1':
        try:
            num = int(input("Введите кол-во элемтов в массиве: "))
            arr = list(range(0,num))
            i = 0
            while i < len(arr):
                print(arr[i],end= ' ')
                i+=1 
            
            i = 1
            arr = []
            while i:
                elem = int(input(f'Введите {i+1} элемент массива: '))
                if elem:
                    arr.append(elem)
                else:
                    break
            print(f'Сумма элементов массива равна: {sum(arr)}\n')  
            while True:
                a = input("Введите цену за кг асфальта")
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
        pass
    elif choice == '0':
        break
    else:
        print("Ошибка ввода выберите заново")
    
