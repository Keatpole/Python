import math
import random

sort = [1, 2, 3, 5, 4, 6, 7, 9]

def bogo_sort(sort):
    '''
    Bogo sort is a simple sorting algorithm that works by shuffling the elements in the list, bla bla bla screw you pylint
    '''

    _sort = []

    tries = 0

    def is_sorted(s):
        '''
        :param:
        '''

        if len(_sort) != len(sort):
            return False

        prev = -math.inf

        '''for i in range(len(s)):
            if (s[i] > s[i + 1]):
                return False

        return True''' # Too messy

        for l in s:
            if l < prev:
                return False

            prev = l

        return True

    for _ in sort:
        _sort.append(1)

    if is_sorted(sort):
        tries += 1

        print(sort)
        print("Tries:", tries)

        exit(0)

    _sort = []

    while not is_sorted(_sort):
        tries += 1

        _sort = []
        g = []

        stop = False

        for _ in sort:
            c = random.randint(0, len(sort) - 1)

            if not c in g:
                _sort.append(sort[c])
                g.append(c)
            else:
                stop = True

                break

        if stop: continue

        print(_sort, tries)
    print("Tries:", tries)

bogo_sort(sort)