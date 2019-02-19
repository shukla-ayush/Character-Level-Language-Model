from collections import Counter
import glob
import os
import fileinput
import math

new_training_set_list = list()
dict_unigram = dict()
dict_bigram = dict()
dict_trigram = dict()
len_page = 11430390
lambda1range = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
lambda2range = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
lambda3range = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

path_of_training_files = input("Enter path of folder where training files are present - ")

def create_held_out_set():
    total_training_file_count = 0
    file_count = 0
    for file in glob.glob(path_of_training_files + "/" +"*.txt"):
        total_training_file_count += 1
        new_training_count = round(0.65 * total_training_file_count)
    for file in glob.glob(path_of_training_files + "/" +"*.txt"):
        if (file_count - new_training_count) < 0:
            create_new_character_model(file)
            new_training_set_list.append(file)
        file_count += 1


def create_new_character_model(file):
    unigram_frequency(file)
    bigram_frequency(file)
    trigram_frequency(file)


def unigram_frequency(file):
    rf = open(file, "r")
    while 1:
        c = rf.read(1)
        if not c: break
        if c in dict_unigram:
            dict_unigram[c] = dict_unigram[c] + 1
        else:
            dict_unigram[c] = 1
    rf.close()

def bigram_frequency(file):
    page = ""
    rf = open(file, "r")
    page = rf.read()
    for j in range(len(page) - 1):
        if page[j:j+2] in dict_bigram:
            dict_bigram[page[j:j+2]] = dict_bigram[page[j:j+2]] + 1
        else:
            dict_bigram[page[j:j+2]] = 1
    rf.close()

def trigram_frequency(file):
    page = ""
    rf = open(file, "r")
    page = rf.read()
    for j in range(len(page) - 2):
        if page[j:j+3] in dict_trigram:
            dict_trigram[page[j:j+3]] = dict_trigram[page[j:j+3]] + 1
        else:
            dict_trigram[page[j:j+3]] = 1
    rf.close()


def determine_lambdas():
    lam1 = 1
    lam2 = 1
    lam3 = 1
    count_tri = 0
    count_first_bi = 0
    count_second_bi = 0
    count_first_uni = 0
    count_second_uni = 0
    max_score = 0
    total_characters = 0
    for key in dict_unigram:
        total_characters = total_characters + dict_unigram[key]
    print(total_characters)

    for lambda1 in lambda1range:
        for lambda2 in lambda2range:
            for lambda3 in lambda3range:
                if ((lambda1 + lambda2 + lambda3) > 0.95) and ((lambda1 + lambda2 + lambda3) < 1.05):
                    # print(lambda1, "a")
                    # print(lambda2, "b")
                    # print(lambda3, "c")
                    score = 0
                    for file in glob.glob(path_of_training_files + "/" +"*.txt"):
                        if (file not in new_training_set_list):
                            rf = open(file, "r")
                            page = rf.read()
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


                                if ((count_tri == 0) or (count_first_bi == 0)):
                                    a = 0
                                else:
                                    a = lambda1 * (count_tri/count_first_bi)


                                if ((count_second_bi == 0) or (count_first_uni == 0)):
                                    b = 0
                                else:
                                    b = lambda2 * (count_second_bi/count_first_uni)


                                if ((count_second_uni == 0) or (len_page == 0)):
                                    c = 0
                                else:
                                    c = lambda3 * (count_second_uni/total_characters)

                                abcscore = (a + b + c)

                                if((count_tri == 0) and (count_first_bi == 0) and (count_second_bi == 0) and (count_first_uni == 0) and (count_second_uni == 0) and (total_characters == 0)):
                                    print()
                                else:
                                    score = score + math.log(abcscore)

                    print(score)
                    print(lambda1)
                    print(lambda2)
                    print(lambda3)
                    # if (score > max_score):
                    #     print("Satisfied")
                    #     print(lambda1)
                    #     print(lambda2)
                    #     print(lambda3)
                    #     max_score = score
                    #     lam1 = lambda1
                    #     lam2 = lambda2
                    #     lam3 = lambda3

    rf.close()


create_held_out_set()

determine_lambdas()
