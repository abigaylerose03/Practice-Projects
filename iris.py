""""
@author A.R.P
@version 1.0



"""

from sklearn.datasets import load_iris
import pandas as pd
import numpy as pd
import nltk as nltk

# loads the dataset
iris_dataset = load_iris()

# gets the keys of the dataset
print("Keys of iris: \n {}".format(iris_dataset.keys()))

# gets the description of the iris
print(iris_dataset['DESCR'][:193] + "\n...")

# gets 
print(iris_dataset['feature_names'])
