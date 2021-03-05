
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
