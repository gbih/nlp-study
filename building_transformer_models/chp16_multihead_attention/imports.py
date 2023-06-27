import locale
import math
import pprint
import warnings

import numpy as np
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.activations import softmax
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Layer
from tqdm.auto import tqdm
from watermark import watermark
