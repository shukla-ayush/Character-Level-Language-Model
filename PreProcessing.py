from collections import Counter
import glob
import os
import fileinput
import re

dict_unigram = dict()
dict_bigram = dict()
dict_trigram = dict()

path_of_training_files = input("Enter path of folder where training files are present - ")

def pre_processing():

        dict_char_count = dict()
        for file in glob.glob(path_of_training_files + "/" + "*.txt"):
            rf = open(file, "r")
            while 1:
                c = rf.read(1)
                if not c: break
                # print(c)
                if c in dict_char_count:
                    dict_char_count[c] = dict_char_count[c] + 1
                else:
                    dict_char_count[c] = 1

            rf.close()

            rf = open(file, "r")
            wf = open(path_of_training_files + "/" + "temp.txt", "w+")
            for line in rf:
                if line.strip():
                    newline = line.replace("\n", " ")
                    newline2 = newline.replace(",", "").replace("!", "").replace(".", "").replace("?", "").replace(";", "").replace(":","").replace("_", "").replace("-", "").replace("[", "").replace("]", "").replace("(", "").replace(")", "").replace("{", "").replace("}", "")
                    newline3 = re.sub('  +','',newline2)
                    wf.write(newline3)

            rf.close()
            wf.close()

            os.remove(file)
            os.rename(path_of_training_files + "/" + "temp.txt", file)

        for file in glob.glob(path_of_training_files + "/" + "*.txt"):
            rf = open(file, "r")
            wf = open(path_of_training_files + "/" + "temp.txt", "w")
            while 1:
                c = rf.read(1)
                if not c: break
                if c in dict_char_count:
                    if (dict_char_count[c] <= 5):
                        print(c, dict_char_count[c])
                        c2 = "?"
                        wf.write(c2)
                    else:
                        wf.write(c)
                else:
                    wf.write(c)

            rf.close()
            wf.close()

            os.remove(file)
            os.rename(path_of_training_files + "/" +  "temp.txt", file)


pre_processing()
