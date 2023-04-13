def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:
        SaveList.append(row)
    return

def storFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return


data = []
ReadMyCsv(data, "正负样本合集.csv")
print(np.array(data).shape)

AllSample = data

Allnode = []
ReadMyCsv(Allnode, "vec(dp).csv")
print(np.array(Allnode).shape)

SampleFeature = []
counter = 0
while counter < len(AllSample):
    counter1 = 0

    while counter1 < len(Allnode):
        if AllSample[counter][0] == Allnode[counter1][0]:
            a = []

            a.extend(Allnode[counter1][1:])
            break
        counter1 = counter1 + 1


    counter2 = 0

    while counter2 < len(Allnode):
        if AllSample[counter][1] == Allnode[counter2][0]:
            b = []

            b.extend(Allnode[counter2][1:])
        counter2 = counter2 + 1

    a.extend(b)
    SampleFeature.append(a)
    counter = counter + 1
    print(counter)

storFile(SampleFeature, 'data/SampleFeature.csv')



