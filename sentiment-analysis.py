import os

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from KaggleWord2VecUtility import KaggleWord2VecUtility

import pandas as pd
import numpy as np

import logging

from nltk.corpus import stopwords # imports various modules for string cleaning
import re
import nltk.data

from bs4 import BeautifulSoup # removes stopwords
from gensim.models import Word2Vec

from gensim import models
# nltk.download()

# Read data from files
train = pd.read_csv( "labeledTrainData.tsv", header=0,
                    delimiter="\t", quoting=3 )
test = pd.read_csv( "testData.tsv", header=0, delimiter="\t", quoting=3 )

unlabeled_train = pd.read_csv( "unlabeledTrainData.tsv", header=0,
                              delimiter="\t", quoting=3 )

print(train["review"][0])

print("Read %d labeled train reviews, %d labeled test reviews, " \
"and %d unlabled reviews \n" %
(train["review"].size,
 test["review"].size,
 unlabeled_train["review"].size))

# Function to convert a document into a sequence of words
# Optionally removing stop words
# Returns a list of words
def review_to_wordlist(review, remove_stopwords=False ):
    # Removes HTML
    review_text = BeautifulSoup(review).get_text()
    # Removes non-letters
    review_text = re.sub("[^a-zA-Z]"," ", review_text)
    # Converts words to lower case and splits them by whitecase to an array
    words = review_text.lower().split()
    # Optionally remove stop words (false by default)
    if remove_stopwords:
        stops = set(stopwords.words("english"))
        words = [w for w in words if not w in stops]
    # Returns the list of words
    return(words)

# Loads the punkt tokenizer
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle');

# Defines a function to split a review into parsed sentences
# splits a reiew into parsed sentences. Returns a list of sentences, where each
# sentence is a list of words
def review_to_sentences(review, tokenizer, remove_stopwords=False ):
    raw_sentences = tokenizer.tokenize(review.strip().decode('utf-8'))
    sentences = []
    for raw_sentence in raw_sentences:
        if len(raw_sentence) > 0:
            sentences.append(review_to_wordlist(raw_sentence, \
             remove_stopwords ))
    return sentences

sentences = [] # initialize an empty list of sentences for the review_to_sentences()

print("Parsing sentences from training set")
for review in train["review"]:
    sentences += review_to_sentences(review, tokenizer)

print("Parsing sentences from unlabled set")
for review in unlabeled_train["review"]:
    sentences += review_to_sentences(review, tokenizer)

print(len(sentences))

# Training Model

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s' , \
	level = logging.INFO);

num_features = 360 # word vector dimesionality
min_word_count = 40 # minimum word count
num_workers = 4 # number of threads to run in parallel
context = 10 # context window size
downsampling = 1e-3 # downsample setting for frequent words

print("Training model...");

model = Word2Vec(sentences, workers = num_workers, \
	size = num_features, min_count = min_word_count, \
	window = context, sample = downsampling)

model.init_sims(replace=True)
model_name = "300features_40minwords_10context"
model.save(model_name)

# Word2Vec.load("testData.tsv")

print(model.doesnt_match("man woman child kitchen".split()))
print(model.most_similar("man"))
print(model.most_similar("baby"))

# total number of words in a vocabulary created from this dataset 
model.wv.syn0.shape 

def feature_vectors(words, model, features):
    featureVec = np.zeros(num_features, dtype="float32")
    nwords = 0

    # converting index2word which is a list to set for better speed in execution
    index2word_set = set(model.wv.index2word)
    for word in words:
        if word in index2word_set:
            nwords += 1
            featureVec = np.add(featureVec, model[word])

            # diving the result by the number of words to get average
            featureVec = np.divide(featureVec, nwords)
            return featureVec

# get the average word2vec sums 
def getAvgFeatureVecs(reviews, model, numFeatures):
    counter = 0
    reviewFeatureVecs = np.zeros((len(reviews), num_features), dtype="float32")
    for review in reviews:
        # printing a status smessage every 1000th review

        if counter % 1000 == 0:
            print("Review %d of %d" % (counter, len(reviews)))

        reviewFeatureVecs[counter] = feature_vectors(review, model, num_features)
        counter += 1
        
    return reviewFeatureVecs

# calculating all the average feature vectors in the training set
clean_train_reviews = []
for review in train['review']:
    clean_train_reviews.append(review_to_wordlist(review, remove_stopwords=True))
    
trainDataVecs = getAvgFeatureVecs(clean_train_reviews, model, num_features)

""" A random forest classifier. A random forest is a meta estimator that 
fits a number of decision tree classifiers on various sub-samples of 
the dataset and uses averaging to improve the predictive accuracy and control over-fitting. """
forest = RandomForestClassifier(n_estimators = 100)

print("Fitting random forest into training data...")
forest = forest.fit(trainDataVecs, train["sentiment"])

result = forest.predict(testDataVecs)
output = pd.DataFrame(data={"id": test["id"], "sentiment": result})
output.to_csv("output.csv", index = False, quoting = 3)

