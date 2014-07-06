import random

def biased_shuffle(items):
    for i in range(len(items)):
        randomIndex = random.randint(0, len(items)-1)
        temp = items[randomIndex]
        items[randomIndex] = items[i]
        items[i] = temp
    return items
