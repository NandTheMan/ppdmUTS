import csv
import re
import nltk
from nltk.corpus import stopwords
import time

with open('indo-song-emot.csv', 'r') as dataset_csv:
    start_time = time.time()
    csv_reader = csv.reader(dataset_csv)

    # header: ['', 'title', 'artist', 'full', 'reff', 'emotion']

    stop_words = stopwords.words('indonesian')
    print(stopwords)
    
    for line in csv_reader:
        no, title, artist, full, reff, emotion, *rest = line
        
        # Remove non word and non space character
        full = re.sub(r'[^\w\s]', '', full) 
        reff = re.sub(r'[^\w\s]', '', reff) 

        full = nltk.word_tokenize(full)
        reff = nltk.word_tokenize(reff)


        
        print([no, title, artist, full, emotion])

        if no == '10':
            end_time = time.time()
            print(end_time - start_time)
            break