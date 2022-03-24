import pandas as pd
import gensim
from gensim.utils import simple_preprocess
from nltk.stem.porter import PorterStemmer
import nltk
from nltk.corpus import stopwords
import re
from tqdm import tqdm

class preprocessor:
    
    def __init__(self):
        
        self.stop_words = stopwords.words('english')
        self.stop_words.extend(['from', 'subject', 're', 'edu', 'use'])
        self.p_stemmer = PorterStemmer()
        
    def sent_to_words(self, sentence):
        return gensim.utils.simple_preprocess(str(sentence), deacc=True)
    
    def remove_stopwords(self, text):
        text = self.sent_to_words(text)
        return [self.p_stemmer.stem(word) for word in simple_preprocess(str(text)) if word not in self.stop_words]
    
    def remove_punc(self, x):
        return re.sub('[,\.!?]', '', str(x)).lower()
    
    def fit_transform(self, s : list):
        s = [' '.join(self.remove_stopwords(self.remove_punc(i))) for i in tqdm(s)]
        return s
