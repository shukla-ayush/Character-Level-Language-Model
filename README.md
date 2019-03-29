The Language Modeling task has been divided primarily into file python files - 

1.) PreProcessing.py
2.) CharacterCount.py
3.) DetermineLambda.py
4.) AddLambdaSmoothing.py
5.) LinearInterpoolationSmoothing.py

In order to run the language model, you need to follow these steps - 

1.) Run the PreProcessing.py, It will ask you to provide the path of the folder where the training files
    are present (Gutenberg). Once you provide the path and hit enter pre-processing will take place and
    all the files will be manipulated in the sense that all double spaces, empty lines and punctuations 
    would be removed.

2.) Run the CharacterCount.py, It will again ask you to provide the path of folder of training files. The
    files that are now present in this folder will have pre-processed sentences. It will also ask you
    to provide path where you want your unigram, bigram and trigram count files to be created. Once 
    completed the 3 files will be generated with unigram, bigram and trigram counts.

3.) Run the DetermineLambda.py, It will ask you the path of folder of training files. I have used the 
    grid search method to determine the lambdas and thus running this file gives the probability score 
    on the data in files of held-out set. For each possible combination of Lambda1, Lambda2 and Lambda3
    the score is displayed, and the highest valule of probability came for
    Lambda1 - 0.8
    Lambda2 - 0.1
    Lambda3 - 0.1
    The abpve value of lambdas was chosen based on the fact that the data of held out set gave maximum probability
    for these lambdas.
    In order to split the training set into new training set and held out set, I calculated the total memory in
    KB of all the files and then split that in 80-20%, Roughly that 80% was the top 12 files in the gutenberg 
    folder, whereas the bottom 6 files formed the held out set.

4.) Run the LinearInterpolationSmoothing.py, It will ask you put the path of folder where the ngram files are 
    present and also the path of folder where the test files are present (whose perplexity you want to calculate).
    The Lambdas have been set by default as 0.8, 0.1, 0.1 in the code. Once the code has been completely run
    a file named "perplexity-linear_interpolation_smoothing.txt" will be created in the same directory as the python
    file.
    The generated file will have 50 files with highest perplexity score. I have manually verified that all of the top
    50 perplexity scores are for French files.	

5.) Run the AddLambdaSmoothing.py, It will ask you put the path of folder where the ngram files are present and also 
    the path of folder where the test files are present (whose perplexity you want to calculate). Once the code has been
    completely run a file named "perplexity-add-lambda-smoothing.txt" will be created which has 50 files with the highest
    perplexity scores.
    I have manually verified that the 50 files are french.

Note - In the current submission folder training files and test files are not present in their respective folders, you can add them there before running, or
provide path of folder where they are. If you want to regenerate the n-gram files please delete the existing n-gram files form n-grams folder or provide a 
different path for their generation.
