import csv
import re
import nltk
#from sastrawi?mpstemmer?indonlp?
from collections import defaultdict
from splitDataset import resultFilename
import ourStopWords as osw

def removeStopWords(token):
    stop_words = osw.stopWords
    return [tkn for tkn in token if tkn not in stop_words]

with open(resultFilename[0], 'r') as traincsv:
    csv_reader = csv.reader(traincsv)

    next(csv_reader)
    for line in csv_reader:
        no, title, artist, full, reff, emotion, *rest = line

        full = re.sub(r'[^\w\s]', '', full) # menghilangkan karakter non alfanumerikal
        reff = re.sub(r'[^\w\s]', '', reff)

        full = nltk.word_tokenize(full) #
        reff = nltk.word_tokenize(reff)

        new_full = removeStopWords(full)
        new_reff = removeStopWords(reff)

        #implementasi stemming disini ketika sudah sepakat

        #further discussion kalo pake tfidf or not
        for fElement in full:
            pass
