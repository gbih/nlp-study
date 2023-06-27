import locale
import math
import pprint
import warnings
from pickle import HIGHEST_PROTOCOL
from pickle import dump
from pickle import load
from time import time

import numpy as np
import tensorflow as tf
from matplotlib.pylab import plt
from numpy import arange
from numpy import savetxt
from numpy.random import shuffle
from tensorflow import GradientTape
from tensorflow import TensorSpec
from tensorflow import argmax
from tensorflow import cast
from tensorflow import convert_to_tensor
from tensorflow import data
from tensorflow import equal
from tensorflow import float32
from tensorflow import function
from tensorflow import int64
from tensorflow import linalg
from tensorflow import math
from tensorflow import matmul
from tensorflow import maximum
from tensorflow import newaxis
from tensorflow import ones
from tensorflow import reduce_sum
from tensorflow import reshape
from tensorflow import shape
from tensorflow import train
from tensorflow import transpose
from tensorflow.keras import Model
from tensorflow.keras.backend import softmax
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Layer
from tensorflow.keras.layers import LayerNormalization
from tensorflow.keras.layers import ReLU
from tensorflow.keras.losses import sparse_categorical_crossentropy
from tensorflow.keras.metrics import Mean
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.optimizers.schedules import LearningRateSchedule
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer
from tqdm.auto import tqdm
from watermark import watermark
