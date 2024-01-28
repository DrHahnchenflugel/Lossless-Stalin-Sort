import random
import StalinSort

for i in range(2000):
    randomLen = random.randint(1,1000)
    randomList = []
    capitaList = []
    initList = []

    for ii in range(randomLen):
        j = random.randint(-100000,100000)
        randomList.append(j)
        capitaList.append(j)
        initList.append(j)

    stalin = StalinSort.recursively_stalining(randomList, 1)
    capitaList.sort()
    if (stalin == capitaList):
        print(f"Test {i+1} pass!")
    else:
        print(f"Test {i+1} fail!\n List:\t\t\t{initList}\n Stalin:\t\t{stalin}\n CapitaList:\t{capitaList}")
        exit()
