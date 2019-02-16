from collections import Counter
import glob
import os
import fileinput
import operator

dict_unigram = dict()
dict_bigram = dict()
dict_trigram = dict()

path_of_training_files = input("Enter path of folder where training files are present - ")
path_of_ngram_files = input("Enter path of folder where you want to generate the n-gram files - ")

def unigram_frequency():
    for file in glob.glob(path_of_training_files + "/" + "*.txt"):
        rf = open(file, "r")
        while 1:
            c = rf.read(1)
            if not c: break
            if c in dict_unigram:
                dict_unigram[c] = dict_unigram[c] + 1
            else:
                dict_unigram[c] = 1



def bigram_frequency():
    for file in glob.glob(path_of_training_files + "/" + "*.txt"):
        w = Counter()
        temp = {}
        page = ""
        bigram_list = list()
        rf = open(file, "r")
        page = rf.read()
        for j in range(len(page) - 1):
            if page[j:j+2] in dict_bigram:
                dict_bigram[page[j:j+2]] = dict_bigram[page[j:j+2]] + 1
            else:
                dict_bigram[page[j:j+2]] = 1

def trigram_frequency():
    for file in glob.glob(path_of_training_files + "/" + "*.txt"):
        w = Counter()
        temp = {}
        page = ""
        rf = open(file, "r")
        page = rf.read()
        for j in range(len(page) - 2):
            if page[j:j+3] in dict_trigram:
                dict_trigram[page[j:j+3]] = dict_trigram[page[j:j+3]] + 1
            else:
                dict_trigram[page[j:j+3]] = 1



def create_unigram_file():
    wf = open(path_of_ngram_files + "/" + "unigram-frequency.txt", "w")
    d = sorted(dict_unigram.items(), key=operator.itemgetter(1), reverse = True)
    for key, value in d:
        wf.write('%s:%s\n' % (key, value))

def create_bigram_file():
    wf = open(path_of_ngram_files + "/" + "bigram-frequency.txt", "w")
    d = sorted(dict_bigram.items(), key=operator.itemgetter(1), reverse = True)
    for key, value in d:
        wf.write('%s:%s\n' % (key, value))

def create_trigram_file():
    wf = open(path_of_ngram_files + "/" + "trigram-frequency.txt", "w")
    d = sorted(dict_trigram.items(), key=operator.itemgetter(1), reverse = True)
    for key, value in d:
        wf.write('%s:%s\n' % (key, value))


unigram_frequency()

bigram_frequency()

trigram_frequency()

create_unigram_file()

create_bigram_file()

create_trigram_file()
