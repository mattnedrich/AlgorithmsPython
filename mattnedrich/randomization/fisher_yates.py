import random

def fisher_yates_shuffle(items):
    for i in range(len(items)):
        randomIndex = random.randint(i, len(items)-1)
        tempItem = items[randomIndex]
        items[randomIndex] = items[i]
        items[i] = tempItem
    return items
