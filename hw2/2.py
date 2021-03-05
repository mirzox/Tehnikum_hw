import random
import string
def delete(string):
    temp = ''
    for i in string:
        if i != ' ':
            temp += i
    return temp
def concatine(tup):
    temp = ''
    for i in tup:
        temp+=i
    return temp
def split(a):
    temp = []
    for i in a:
        if i != ' ':
            temp.append(i)
    return temp

#Составить из букв введенной строки слова
print("Составить из букв введенной строки слова\n")
a = input("Введите строку: ")
a = split(a)
for i in range(15):
    temp = ''
    random.shuffle(a)
    temp = temp.join(a)
    print(temp)

#Удалить из строки пробелы и определить, является ли она перевертышем
print("\nУдалить из строки пробелы и определить, является ли она перевертышем\n")
c = delete(input("\nВведите строку: "))
if c.lower() == c[::-1].lower():
    print("Введенная строка является полиндромом")

#Замена подстроки
print("\n________Замена подстроки________\n")
d = input("Введите строку: ")
e = input("Введите подстроку которую хотите заменить: ")
f = input("Введите замену подстроки: ")
print(d.lower().replace(e.lower(),f).capitalize())

#Удаление из строки повторяющихся символов
print("\nУдаление из строки повторяющихся символов\n")
g = input("Введите стороку: ")
h = []
for i in g:
    if i != ' ':
        h.append(i)
h = list(set(h))
print(concatine(h))

#Удаление лишних пробелов
print("\nУдаление лишних пробелов\n")

l = input("Введите строку: ").strip()
counter = 0
o = ''
for i in l:
    if i == ' ':
        counter+=1
        if counter == 1:
            o+=' '
    else:
        counter = 0
        o+= i
print(o)

#Самая длинная строка в массиве
print("\nСамая длинная строка в массиве\n")
m = []
n = int(input("Введите кол-во строк в массиве: "))
maxx = 0
for i in range(n):
    m.append(input())
    if len(m[i])>maxx:
        maxx = len(m[i])

for i in range(0,len(m)):
    if maxx == len(m[i]):
        print(f"Самая длинная строка под {i} индексом")

#Самое длинное слово в строке
print("\nСамое длинное слово в строке\n")
maxx = 0
p = input("Введите строку:").split(" ")
for i in p:
    if len(i)>maxx:
        maxx = len(i)
counter = 0
while counter <= len(p):
    if len(p[counter]) == maxx:
        print(f"Самое длинное слово это {p[counter]}") 
        break
    counter+=1

print("\nКоличество строчных и прописных букв в строке\n")
l_c = string.ascii_lowercase
u_c = string.ascii_uppercase
q = input("Введите строку: ")
count_l = 0
count_u = 0
for i in q:
    if i in l_c:
        count_l += 1
    elif i in u_c:
        count_u += 1
    else:
        pass
print(f"Количесво строчных букв в строке равно {count_l} и количество прописных букв равно {count_u}")

print("\nКоличество слов в строке\n")
r = input("Введите строку: ").split(" ")
count_index = 0
for i in r:
    if i != '':
        count_index +=1    
print(f"Количество слов в строке равно {count_index}")

