import csv

import numpy as np

def storFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile, )
        writer.writerows(data)
    return

data2 = []
ReadMyCsv(data2, "NegativeSample.csv")
print(len(data2))


data_final = []
data_final = np.vstack((data1,data2))


print(data_final.shape)
print(data_final)
