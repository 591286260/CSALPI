import numpy as np
np.random.seed(1337)

import csv

def storFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return

OriginalData = []

print(len(OriginalData))

LncDisease = []
counter = 0
while counter < len(OriginalData):
    Pair = []
    Pair.append(OriginalData[counter][0])
    Pair.append(OriginalData[counter][1])
    LncDisease.append(Pair)
    counter = counter + 1

print('Lnc', len(LncDisease))
print('OriginalData', len(OriginalData))

AllDisease = []
counter1 = 0
while counter1 < len(OriginalData):
    counter2 = 0
    flag = 0
    while counter2 < len(AllDisease):
        if OriginalData[counter1][1] != AllDisease[counter2]:
            counter2 = counter2 + 1
        elif OriginalData[counter1][1] == AllDisease[counter2]:
            counter2 = counter2 + 1
    if flag == 0:
        AllDisease.append(OriginalData[counter1][1])
    counter1 = counter1 + 1
print('len(All)', len(AllDisease))

counter1 = 0
counter2 = 0
counterP = 0
counterN = 0
PositiveSample = []

PositiveSample = LncDisease
print('PositiveSample)', len(PositiveSample))

NegativeSample = []
counterN = 0
while counterN < len(PositiveSample):

    while counter < len(LncDisease):
        if DiseaseAndRnaPair == LncDisease[counter]:
            flag1 = 1
            break
        counter = counter + 1
    if flag1 == 1:
        continue
    flag2 = 0
    counter1 = 0
    while counter1 < len(NegativeSample):
        if DiseaseAndRnaPair == NegativeSample[counter1]:
            flag2 = 1
            break
        counter1 = counter1 + 1
    if flag2 == 1:
        continue
    if (flag1 == 0 & flag2 == 0):
        NegativePair = []
        NegativePair.append(AllDRUG[counterR])
        NegativePair.append(AllDisease[counterD])
        NegativeSample.append(NegativePair)
        counterN = counterN + 1
print('len(NegativeSample)', len(NegativeSample))
storFile(NegativeSample, 'NegativeSample.csv')