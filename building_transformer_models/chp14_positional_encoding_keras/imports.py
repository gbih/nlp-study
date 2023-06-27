import locale
import math
import pprint
import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import tensorflow as tf
from tensorflow import convert_to_tensor
from tensorflow.data import Dataset
from tensorflow.keras.layers import Embedding
from tensorflow.keras.layers import Layer
from tensorflow.keras.layers import TextVectorization
from tqdm.auto import tqdm
from watermark import watermark
