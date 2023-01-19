# Homework. Task 6_5.
# Реализовать функцию, возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)

import random

def get_uniq(user_value):
    return True if user_value == 'True' else False

def get_joke(n, list1, list2, list3, ind=False):
    result = []
    if ind == False:
        while n > 0:
            joke = []
            joke.append(random.choice(list1))
            joke.append(random.choice(list2))
            joke.append(random.choice(list3))
            result.append(' '.join(joke))
            n -= 1
    if ind == True:
        n = min([len(list1), len(list2), len(list3)])
        while n > 0:
            joke = []
            joke.append(list1.pop(random.randint(0, len(list1)-1)))
            joke.append(list2.pop(random.randint(0, len(list2)-1)))
            joke.append(list3.pop(random.randint(0, len(list3)-1)))
            result.append(' '.join(joke))
            n -= 1
    return result

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

value = input('Enter a number of jokes and indicator of uniqueness ("True"), if necessary (e.g. "5 True"): ')
value = value.split(' ')
q_ty = int(value[0])
uniq = False
if len(value) > 1: uniq = get_uniq(value[1])
output = get_joke(q_ty, nouns, adverbs, adjectives, uniq)
print(output)
