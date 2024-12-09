import random
numbers = []
def get_numbers():

    n = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16,17,18,19,20]
    win = random.choice(n)
    for i in range(win):
        for j in range(1,win):
            if i % j == 0:
                numbers.append(i)

    return win

win = get_numbers()


print(win, '-', numbers)
