from collections import Counter
import math
import glob
import os
import operator
import fileinput

dict_unigram = dict()
dict_bigram = dict()
dict_trigram = dict()
dict_char = dict()
dict_perplexity = dict()

path_of_ngram_files = input("Enter path of folder where Unigram, Bigram and Trigram files are present - ")
path_of_test_files = input("Enter path of folder where test files are present - ")

def create_unigram_dict():
    rf = open(path_of_ngram_files + "/" + "unigram-frequency.txt", "r")
    for line in rf:
        (key, val) = line.rstrip().split(":")
        dict_unigram[key] = val

def create_bigram_dict():
    rf = open(path_of_ngram_files + "/" + "bigram-frequency.txt", "r")
    for line in rf:
        (key, val) = line.rstrip().split(":")
        dict_bigram[key] = val

def create_trigram_dict():
    rf = open(path_of_ngram_files + "/" + "trigram-frequency.txt", "r")
    for line in rf:
        (key, val) = line.rstrip().split(":")
        dict_trigram[key] = val


def add_lambda_smoothing():
    for file in glob.glob(path_of_test_files + "/" +"*"):
        rf = open(file, "r")
        page = rf.read()
        pscore = 0
        perplexity = 0
        V = len(dict_unigram)

        for j in range(len(page) - 2):
            count_tri = 0
            count_bi = 0
            score = 0
            if page[j:j+3] in dict_trigram:
                count_tri = int(dict_trigram[page[j:j+3]])
            if page[j:j+2] in dict_bigram:
                count_bi = int(dict_bigram[page[j:j+2]])
            score = (count_tri + 0.1)/(count_bi + (0.1*V))
            pscore = pscore - math.log(score)
        x = pscore/len(page)
        perplexity = math.exp(x)
        dict_perplexity[file] = perplexity
        rf.close()
    print("Perplexity for all files calculated")
	print(dict_perplexity)

def write_perplexity_to_file():
    count = 0
    wf = open("perplexity-add-lambda-smoothing.txt", "w")
    d = sorted(dict_perplexity.items(), key=operator.itemgetter(1), reverse = True)
    for key, value in d:
        if count < 50:
            wf.write('%s,%s\n' % (key, value))
            count += 1
    print("Perplexity file created")


create_unigram_dict()

create_bigram_dict()

create_trigram_dict()

add_lambda_smoothing()

write_perplexity_to_file()
