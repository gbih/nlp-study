import locale
import math
import pprint
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
import tensorflow.keras.backend as K
from scipy.special import softmax
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras import Model
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Layer
from tensorflow.keras.layers import SimpleRNN
from tensorflow.keras.metrics import mean_squared_error
from tensorflow.keras.models import Sequential
from tqdm.auto import tqdm
from watermark import watermark
