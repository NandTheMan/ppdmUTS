import csv
from collections import defaultdict
import math

targetFilename = 'indo-song-emot.csv'
resultFilename = ['train-data.csv', 'test-data.csv']

#dataSplit = [0.8, 0.2] #memilih pembagian data train dan test antara line 7/8
dataSplit = [0.7, 0.3]

labels = defaultdict(int)
totalLine = 0

def calcSplit(daDict): #memastikan pembagian terdistribusi dengan baik agar tidak outofrange
    global dataSplit #mengambil nilai pilihan
    newDistDict = defaultdict(list) #dictionary yang akan direturn

    for key in daDict:
        # print(key)
        tempList = list()

        trainData = math.ceil(daDict[key] * dataSplit[0])
        testData = math.floor(daDict[key] * dataSplit[1]) #memastikan data yang terbagi seimbang (bila seharusnya ada remainder)

        tempList.append(trainData)
        tempList.append(testData)
        newDistDict[key] = tempList

    return newDistDict


with open(targetFilename, 'r') as csvfile: #buka file read only, untuk tahu banyak line dan distribusi label
    csvreader = csv.reader(csvfile)
    next(csvreader) #skip first line

    for line in csvreader:
        no, title, artist, full, reff, emotion, *rest = line #inisialisasi label tiap atribut

        labels[emotion] += 1

    print(labels)
    splittedLabels = calcSplit(labels)

    csvfile.seek(0)
    csvreader = csv.reader(csvfile)
    next(csvreader) #reset pembacaan dari awal

    trainList = list()
    testList = list()

    for line in csvreader: #buat list berdasarkan nilai distribusi tadi, untuk write pada csv baru (train dan write)
        no, title, artist, full, reff, emotion, *rest = line #inisialisasi label tiap atribut

        if splittedLabels[emotion][0] != 0: #jika pada mapping 0 belumm habis, maka masukkan ke train
            trainList.append(list(line))
            splittedLabels[emotion][0] -= 1
        elif splittedLabels[emotion][1] != 0: #jika pada mapping 0 sudah habis tapi mapping 1 belum, masukkan ke test
            testList.append(list(line))
            splittedLabels[emotion][1] -= 1
        else: #print ke console untuk rerun (atau further consideration)
            print("out of bound")

    # print(trainList)
    # print(testList)

with open(resultFilename[0], 'w', newline='') as csvfile1, open(resultFilename[1], 'w', newline='') as csvfile2:
    writeTrain = csv.writer(csvfile1)
    writeTest = csv.writer(csvfile2)

    for line in trainList:
        writeTrain.writerow(line)
    for line in testList:
        writeTest.writerow(line)