# classes we intend to use
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils

# load ascii text and convert to lowercase
fileName = "wonderland.txt"
rawText = open(fileName).read()
rawText = rawText.lower()

# get sorted list of uniquely used words
words = sorted(list(set(rawText)))
# create mapping of chars to integers
charToInt = dict((c, i) for i, c in enumerate(chars))
