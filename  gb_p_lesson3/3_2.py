# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.

from random import sample

def words_list (num, word="abc"):
    w_list = []
    for i in range(num):
        m = sample(word, k=3)
        w_list.append("".join(m))
    return w_list

def find_second (n_list, word):
    if word in n_list and n_list.count(word)>1:
        c = n_list.index(word)
        print(n_list.index(word, c+1))
    else:
        print(-1)

n = int(input('Введите число: '))

u = words_list(n)
print(u)
w = input("Введите слово: ")
find_second(u, w)
