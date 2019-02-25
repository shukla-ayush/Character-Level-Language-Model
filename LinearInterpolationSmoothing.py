from collections import Counter
import glob
import os
import fileinput
import math
import operator

dict_unigram = dict()
dict_bigram = dict()
dict_trigram = dict()
dict_perplexity = dict()
count_tri = 0
count_first_bi = 0
count_second_bi = 0
count_first_uni = 0
count_second_uni = 0
len_page = 11185729

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


def linear_interpolation_smoothing():
    lambda1 = 0.8
    lambda2 = 0.1
    lambda3 = 0.1
    max_score = 0
    total_characters = 0
    for key in dict_unigram:
        total_characters = total_characters + int(dict_unigram[key])
    print(total_characters, "total_characters")
    for file in glob.glob(path_of_test_files + "/" + "*"):
        # print(file)
        rf = open(file, "r")
        page = rf.read()
        score = 0
        abscore = 0
        for j in range(len(page) - 2):
            if(page[j:j+3] in dict_trigram):
                count_tri = float(dict_trigram[page[j:j+3]])
            if(page[j:j+2] in dict_bigram):
                count_first_bi = float(dict_bigram[page[j:j+2]])
            if(page[j+1:j+3] in dict_bigram):
                count_second_bi = float(dict_bigram[page[j+1:j+3]])
            if(page[j+1:j+2] in dict_unigram):
                count_first_uni = float(dict_unigram[page[j+1:j+2]])
            if(page[j+2:j+3] in dict_unigram):
                count_second_uni = float(dict_unigram[page[j+2:j+3]])

            if (count_first_bi < 0.1):
                # a = 0
                if(page[j:j+1] not in dict_unigram):
                    if(("?"+str(page[j+1:j+2])) in dict_bigram):
                        count_first_bi = float(dict_bigram["?"+str(page[j+1:j+2])])
                    if(("?"+str(page[j+1:j+3])) in dict_trigram):
                        count_tri = float(dict_trigram["?"+str(page[j+1:j+3])])
                if(page[j+1:j+2] not in dict_unigram):
                    if((str(page[j:j+1]) + "?") in dict_bigram):
                        count_first_bi = float(dict_bigram[str(page[j:j+1]) + "?"])
                    if((str(page[j:j+1]) + "?" + str(page[j+2:j+3])) in dict_trigram):
                        count_tri = float(dict_trigram[str(page[j:j+1]) + "?" + str(page[j+2:j+3])])
                if(count_first_bi < 0.1):
                    a = 0
                else:
                    a = lambda1 * (count_tri/count_first_bi)

            else:
                a = lambda1 * (count_tri/count_first_bi)



            if (count_first_uni < 0.1):
                # b = 0
                if (("?" + str(page[j+2:j+3])) in dict_bigram):
                    count_second_bi = float(dict_bigram[("?" + str(page[j+2:j+3]))])
                if (count_second_bi == 0):
                    b = 0
                else:
                    b = lambda2 * (count_second_bi/float(dict_unigram["?"]))

            else:
                b = lambda2 * (count_second_bi/count_first_uni)



            if (count_second_uni < 0.1):
                c = lambda3 * (float(dict["?"])/total_characters)
            else:
                c = lambda3 * (count_second_uni/total_characters)


            abcscore = (a + b + c)


            if((count_tri == 0) and (count_first_bi == 0) and (count_second_bi == 0) and (count_first_uni == 0) and (count_second_uni == 0) and (total_characters == 0)):
                print()
            else:
                score = score - math.log(abcscore)

        x = score/len(page)
        perplexity = math.exp(x)
        dict_perplexity[file] = perplexity
        rf.close()
    print("Perplexity for all files calculated")
    print(dict_perplexity)

def write_perplexity_to_file():
    count = 0
    wf = open("perplexity-linear_interpolation_smoothing.txt", "w")
    d = sorted(dict_perplexity.items(), key=operator.itemgetter(1), reverse = True)
    for key, value in d:
        if count < 50:
            wf.write('%s,%s\n' % (key, value))
            count += 1
    print("Perplexity file created")

create_unigram_dict()

create_bigram_dict()

create_trigram_dict()

linear_interpolation_smoothing()

write_perplexity_to_file()
