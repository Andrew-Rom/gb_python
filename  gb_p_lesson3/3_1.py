# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
#    Напишите программу, которая определит, присутствует ли в заданном списке число,
#    полученное от пользователя.

from random import sample
import os
def clear(): return os.system('cls')


clear()

# import random

def find_number(amount, user_number):
    new_list = sample(range(1, (amount+1)*2), k=amount)
    print(new_list)
    if user_number in new_list:
        return 'yes'
    return 'no'


some_number = find_number(int(input('Enter amount - ')),
                          int(input('Enter the desired number - ')))
print(some_number)
