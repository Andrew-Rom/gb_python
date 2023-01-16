# Homework. Task 5_1.
# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# В тексте используется разделитель пробел.

import random
import os
clear = lambda: os.system('cls')
clear()

value = input("Input number of words: ")
if value.isdigit() and int(value) > 0:
    qty_words = int(value)
    del_word = "абв"
    rnd_text = ' '.join(''.join(random.sample(del_word, k=3)) for i in range(qty_words))
    print("Generated text:", rnd_text)
    mod_text = rnd_text.split(' ')
    while (del_word in mod_text): mod_text.remove(del_word)
    mod_text = ' '.join(mod_text)
    print("Output result: ", mod_text)
else:
    print('Error. Incorrect input.')


