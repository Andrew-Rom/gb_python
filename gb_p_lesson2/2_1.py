# 1. Напишите программу, которая принимает на вход число N
# и выдаёт последовательность из N членов.
# 1, -3, 9, -27, 81.


n = int(input())

for i in range(n):
    print((-3) ** i)
