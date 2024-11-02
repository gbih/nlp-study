import glob
import locale
import logging
import os.path
import pprint
import re
import urllib.robotparser
import warnings

import feedparser
import matplotlib.pyplot as plt
import pandas as pd
import requests
import scrapy
import seaborn as sns
import xmltodict
from bs4 import BeautifulSoup
from dateutil import parser
from readability import Document
from scrapy.crawler import CrawlerProcess
from tqdm.auto import tqdm
from watermark import watermark
