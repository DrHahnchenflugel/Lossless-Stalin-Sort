import random
import StalinSort
'''
    Pf. of concept
'''
randomLen = random.randint(1,10)
randomList = []
initList = []

for ii in range(randomLen):
    a = random.randint(-1000,1000)
    randomList.append(a)
    initList.append(a)

print("============================")
print(f"iter:0 |{initList}")
print(StalinSort.recursively_stalining(randomList, 1))
print("from\n"+str(initList))