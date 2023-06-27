import locale
import math
import pprint
import warnings

import numpy as np
import tensorflow as tf
from tensorflow import cast
from tensorflow import float32
from tensorflow import linalg
from tensorflow import math
from tensorflow import ones
from tensorflow.keras import Model
from tensorflow.keras.activations import softmax
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Layer
from tensorflow.keras.layers import LayerNormalization
from tensorflow.keras.layers import ReLU
from tqdm.auto import tqdm
from watermark import watermark
