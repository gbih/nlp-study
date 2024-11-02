import locale
import pprint
import random
import warnings
from collections import Counter

import nltk
import numpy as np
import pandas as pd
import regex as re
import seaborn as sns
import textacy
from matplotlib import pyplot as plt
from textacy.extract.kwic import keyword_in_context
from tqdm.auto import tqdm
from watermark import watermark
from wordcloud import WordCloud
